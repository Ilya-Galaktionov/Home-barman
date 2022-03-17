from turtle import title
from flask import Flask, render_template, url_for

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

#@app.route('recept')
#def recept():
 #   return render_template('your_recept.html')


@app.route('/user/<string:name>/<int:id>')
def user(name, id):
    return "User page:" + name +" - " + str(id)

if __name__ == "__main__":
    app.run(debug=True)