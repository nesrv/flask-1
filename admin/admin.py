from os import urandom
from flask import Blueprint, request, redirect, url_for, session, render_template, flash
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import LoginManager, login_user, login_required, logout_user, current_user
from .UserLogin import UserLogin

users = {
    "admin": "scrypt:32768:8:1$L79A2dzeYEs2oadu$4f365638b691bb0df592b9f0b5a04ebdeeba87247289cdb854f7ef26e4e3204d66f5d42b8834395ed6f0b1db648afb732ff1d338fce2067e19bc089413a7c89b",
    "user": "scrypt:32768:8:1$vfIa46715CnfB57i$7d2604a1fb0ef829fd62119096e62038acba12ecca56dc043a89c029d24204ab41e54ad91be63d6e9bdac92cd70a18a06a88befa9cb1064d68b85394b584883a"
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
