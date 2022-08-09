
from flask import Blueprint, render_template, redirect, url_for
from sqlalchemy.sql.expression import func
from webapp.cocktails.models import Cocktails, Tags
from webapp.user.forms import SearchForm
from webapp import db


blueprint = Blueprint('cocktail', __name__)


@blueprint.route('/')
def index():
    page_title = 'Home-barman'
    cocktails = Cocktails.query.order_by(func.random()).limit(12).all()
    return render_template('index.html', page_title=page_title, cocktails=cocktails)


@blueprint.route('/recipe')
def recipe():
    return render_template('recipe.html')

@blueprint.route('/cocktail/<int:cocktail_id>')
def single_cocktail(cocktail_id):
    my_cocktail = Cocktails.query.filter(Cocktails.id == cocktail_id).first()
    tags_list = []
    if my_cocktail:
        for tags in Tags.query.filter(Tags.cocktail_id == cocktail_id):
            tags_list.append(tags)
    return render_template('cocktails/single_cocktail.html', page_title=my_cocktail.title,
                            my_cocktail=my_cocktail, tags_list=tags_list)


@blueprint.context_processor
def base():
    form = SearchForm()
    return dict(form=form)


@blueprint.route('/search', methods=['GET', 'POST'])
def search():
    form = SearchForm()
    cocktails = Cocktails.query
    if form.validate_on_submit():
        single_cocktail.searched = form.searched.data
        cocktails = cocktails.filter((Cocktails.tags.like('%' + single_cocktail.searched + '%') |
                                     (Cocktails.title.like('%' + single_cocktail.searched + '%'))))
        return render_template('cocktails/search.html', form=form,
                               searched=single_cocktail.searched, cocktails=cocktails)
    else:
        return redirect(url_for('cocktail.index'))

