from webapp import create_app
from cocktails import get_data


app = create_app()
with app.app_context():
    get_data('cocktails_urls.txt')
