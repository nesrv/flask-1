from flask import Flask, render_template, url_for
from admin.admin import admin
from vektor_app.vektor_app import vektor_app
from os import urandom

app = Flask(__name__)

app.register_blueprint(vektor_app)
app.register_blueprint(admin, url_prefix='/admin')

  



if __name__ == '__main__':
    app.config['SECRET_KEY'] = urandom(20).hex()
    app.run(debug=True)