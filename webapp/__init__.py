from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return """
    <html>
        <head>
            <title>Home-barman</title>
        </head>
    </htm>
    """

if __name__ == "__main__":
    app.run()