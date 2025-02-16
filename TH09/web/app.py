from flask import Flask, render_template, request, redirect, url_for, flash, session
from db import get_db_connection
from flask_bcrypt import Bcrypt
from flask_login import LoginManager, UserMixin, login_user, logout_user, login_required

app = Flask(__name__)
app.config.from_object('config.Config')
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'

class User(UserMixin):
    def __init__(self, id, username):
        self.id = id
        self.username = username

@login_manager.user_loader
def load_user(user_id):
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM users WHERE id = %s", (user_id,))
    user = cursor.fetchone()
    conn.close()
    if user:
        return User(user["id"], user["username"])
    return None

@app.route('/')
def home():
    username  = session.get('username')
    return render_template('home.html', username=username)

from mysql.connector import Error

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username'].strip()
        email = request.form['email'].strip()
        password = request.form['password']

        # Kiểm tra username hoặc email đã tồn tại chưa
        conn = get_db_connection()
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM users WHERE username = %s OR email = %s", (username, email))
        existing_user = cursor.fetchone()

        if existing_user:
            flash("Tên đăng nhập hoặc email đã tồn tại!", "danger")
            conn.close()
            return redirect(url_for('register'))

        # Mã hóa mật khẩu
        hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')

        try:
            # Chèn dữ liệu vào database
            cursor.execute("INSERT INTO users (username, email, password) VALUES (%s, %s, %s)", 
                           (username, email, hashed_password))
            conn.commit()
            flash("Đăng ký thành công!", "success")
            return redirect(url_for('login'))
        except Error as e:
            flash(f"Lỗi đăng ký: {e}", "danger")
        finally:
            conn.close()

    return render_template('register.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        conn = get_db_connection()
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM users WHERE username = %s", (username,))
        user = cursor.fetchone()
        print("User tìm thấy trong database:", user)  # In ra để kiểm tra
        conn.close()

        if user and bcrypt.check_password_hash(user['password'], password):
            user_obj = User(user["id"], user["username"])
            session['username'] = user["username"]
            login_user(user_obj)
            flash("Đăng nhập thành công!", "success")
            return redirect(url_for('home'))
        else:
            flash("Sai tên đăng nhập hoặc mật khẩu!", "danger")
    
    return render_template('login.html')

@app.route('/logout')
@login_required
def logout():
    logout_user()
    flash("Đăng xuất thành công!", "success")
    return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(debug=True)
