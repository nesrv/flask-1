from os import urandom
from flask import Blueprint, request, redirect, url_for, session, render_template, flash
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import LoginManager, login_user, login_required, logout_user, current_user
from .UserLogin import UserLogin

users = {
    "admin": "12345",
    "user": "12345"
}

menu = [{'url': '.index', 'title': 'Панель'},
        {'url': '.logout', 'title': 'Выйти'}]




admin = Blueprint('admin', __name__,
                  template_folder='templates', static_folder='static')
# admin.config['SECRET_KEY'] = urandom(20).hex()

login_manager = LoginManager()
login_manager.login_view = 'login'
login_manager.login_message = "Авторизуйтесь для доступа к закрытым страницам"
login_manager.login_message_category = "success"


@login_manager.user_loader
def load_user(user_id):
    print("load_user")
    return UserLogin().fromJson(user_id, users)



def login_admin():
    session['admin_logged'] = 1


def isLogged():
    return True if session.get('admin_logged') else False


def logout_admin():
    session.pop('admin_logged', None)




@admin.route('/')
@admin.route('/index')
def index():
    if not isLogged():
        return redirect(url_for('.login'))

    return render_template('admin/index.html', menu=menu, title='Админ-панель')


@admin.route("/home")
def home():
    return "home"


@admin.route('/login', methods=["POST", "GET"])
def login():
    if request.method == "POST":
        if request.form['user'] == "admin" and request.form['psw'] == "12345":
            user = request.form['user']
            login_admin()
            userlogin = UserLogin().create(user)
            # login_user(userlogin, remember=True)
            return redirect(url_for('.index'))
        else:
            flash("Неверная пара логин/пароль", "error")

    return render_template('admin/login.html', title='Админ-панель')


@admin.route('/logout', methods=["POST", "GET"])
def logout():
    if not isLogged():
        return redirect(url_for('.login'))

    logout_admin()

    return redirect(url_for('.login'))
