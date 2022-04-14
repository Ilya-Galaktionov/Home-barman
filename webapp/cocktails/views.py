from flask import Blueprint, g, render_template, redirect, url_for
from requests import request
from sqlalchemy.sql.expression import func
from webapp.cocktails.models import Cocktails
from webapp.user.forms import SearchForm


blueprint = Blueprint('cocktail', __name__)


@blueprint.route('/')
def index():
    page_title = 'Home-barman'
    cocktails = Cocktails.query.order_by(func.random()).limit(3).all()
    return render_template('index.html', page_title=page_title, cocktails=cocktails)


@blueprint.route('/recipe')
def recipe():
    return render_template('recipe.html')


@blueprint.route('/cocktail/<int:id>')
def cocktail(id):
    cocktail = Cocktails.query.filter_by(id=id).first()
    return render_template('cocktails/cocktail.html', cocktail=cocktail)



