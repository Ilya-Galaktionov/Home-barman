from webapp import create_app
from cocktails import get_all_cocktails


app = create_app()
with app.app_context():
    get_all_cocktails('webapp/cocktails_urls.txt')
