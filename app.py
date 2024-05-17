from flask import Flask, render_template, url_for, redirect, request, flash
from admin.admin import admin
from vektor_app.vektor_app import vektor_app
from os import urandom
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import LoginManager, login_user, login_required, logout_user, current_user
from UserLogin import UserLogin

menu = [{'url': '.index', 'title': 'Панель'},
        {'url': '.logout', 'title': 'Выйти'}]

users = {
    "admin": {"id": 1, "name": "admin", "psw": "12345"},
    "user": {"id": 1, "name": "user", "psw": "12345"}
}

DEBUG = True
SECRET_KEY = 'fdgfh78@#5?>gfhf89dx,v06k'
app = Flask(__name__)
app.config.from_object(__name__)

login_manager = LoginManager(app)
login_manager.login_view = 'login'
login_manager.login_message = "Авторизуйтесь для доступа к закрытым страницам"
login_manager.login_message_category = "success"



@login_manager.user_loader
def load_user(user_id):
    print("load_user", user_id, users)
    print(UserLogin.fromJson(user_id, users))
    #ищет по id а у нас словарь по имени admin user и тп
    return UserLogin.fromJson(user_id, users)

@app.route("/index")
def index():
    print("="*40)
    return render_template("index.html")  
  
@app.route("/login", methods=["POST", "GET"])
def login():
    print("login")
    if current_user.is_authenticated:
        print('аутентифицирован')
        return redirect(url_for('index'))

    if request.method == "POST":
        user = users[request.form['email']]
        print(user)
        # if user and check_password_hash(user['psw'], request.form['psw']):
        if user:
            userlogin = UserLogin().create(user)
            rm = True if request.form.get('remainme') else False
            login_user(userlogin, remember=rm)
            print('ok')
            return redirect(url_for("index"))

        flash("Неверная пара логин/пароль", "error")

    return render_template("login.html", menu=menu, title="Авторизация")  


@app.route("/register")
def register():
    return render_template("register.html", menu=menu, title="Регистрация")

# app.register_blueprint(vektor_app)
# app.register_blueprint(admin, url_prefix='/admin')

if __name__ == '__main__':
    app.config['SECRET_KEY'] = urandom(20).hex()
    app.run(debug=True)