from flask import Blueprint, render_template
from  sqlalchemy.sql.expression import func
from webapp.cocktails.models import Cocktails

blueprint = Blueprint('cocktail', __name__)


@blueprint.route('/')
def index():
    page_title = 'Home-barman'
    cocktails_list = Cocktails.query.order_by(func.random()).limit(6).all()
    return render_template('index.html', page_title=page_title, cocktails_list=cocktails_list)


@blueprint.route('/recipe')
def recipe():
    return render_template('recipe.html')


@blueprint.route('/ingredients/<int:id>')
def single_cocktail(id):
    cocktail_id = Cocktails.query.filter_by(id=id).first()
    return render_template('cocktails/single_cocktail.html', cocktail_id=cocktail_id)


@blueprint.route('/search')
def search():
    return render_template('search.html')
