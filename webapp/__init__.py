from flask import Flask, render_template

def create_app():
    app = Flask(__name__)

    @app.route('/')
    def index():
        page_title = 'Home-barman'
        return render_template('index.html' ,page_title=page_title)
    
    
    return app