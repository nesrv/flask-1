from flask import Blueprint, render_template,  redirect


vektor_app = Blueprint("vektor_app", __name__,template_folder="templates", static_folder="static")


@vektor_app.route("/")
def index():
    return '+'

@vektor_app.route("/home")
def home():
    return "home"


