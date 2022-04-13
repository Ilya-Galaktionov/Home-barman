from flask import Blueprint, render_template
from requests import request
from sqlalchemy.sql.expression import func
from webapp.cocktails.models import Cocktails
from webapp.user.forms import SearchForm

blueprint = Blueprint('cocktail', __name__)


@blueprint.route('/')
def index():
    page_title = 'Home-barman'
    cocktails_list = Cocktails.query.order_by(func.random()).limit(3).all()
    return render_template('index.html', page_title=page_title, cocktails_list=cocktails_list)


@blueprint.route('/recipe')
def recipe():
    return render_template('recipe.html')


@blueprint.route('/ingredients/<int:id>')
def single_cocktail(id):
    cocktail_id = Cocktails.query.filter_by(id=id).first()
    return render_template('cocktails/single_cocktail.html', cocktail_id=cocktail_id)

@blueprint.route('/cocktails/<int:id>')
def cocktails(id):
    cocktail = Cocktails.query.get_or_404(id)
    return render_template('cocktails/single_cocktail.html', cocktail=cocktail)


@blueprint.route('/search', methods=['POST'])
def search():
    form = SearchForm()
    cocktails = Cocktails.query
    if form.validate_on_submit():
        cocktail.searched = form.searched.data
        cocktails = Cocktails.filter(Cocktails.title.like('%' + cocktail.searched + '%')).all()
    return render_template('cocktails/search_results.html',
        form=form,
        searched = cocktail.searched,
        cocktails = cocktails)
