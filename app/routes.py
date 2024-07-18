
from flask import render_template, redirect, url_for, request, flash, session
from app import app, db, bcrypt
from app.forms import LoginForm, RegisterForm, AddbookForm
from app.models import User, db, Bookshelf


@app.route("/")
def home():
    return render_template('home.html', title='Home')
@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()

    if request.method == 'POST':
        user = User.query.filter_by(username=form.username.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            session.clear()
            session['user_id'] = user.id
            session['username'] = user.username
            flash(f'You are now logged in as {user.username}!', 'success')
            return redirect(url_for('user_menu'))
        else:
            flash('Username or password is incorrect.', 'danger')

    return render_template('login.html', form=form)
@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()

    if request.method == 'POST' and form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode("utf-8")

        new_user = User(
            username=form.username.data,
            email=form.email.data,
            password=hashed_password)

        db.session.add(new_user)
        db.session.commit()
        flash('You are now registered!', 'success')
        return redirect(url_for('login'))

    return render_template('register.html', form=form)
@app.route("/logout")
def logout():
   session.pop('user.id', None)
   session.pop('user.username', None)
   session.pop('user.email', None)
   session.pop('user.password', None)
   return redirect(url_for('login'))

@app.route('/user_menu', methods=['GET', 'POST'])
def user_menu():
    if 'user_id' not in session:
        flash('You need to login first.', 'danger')
        return redirect(url_for('login'))

    user = User.query.get(session['user_id'])
    if not user:
        flash('User not found.', 'danger')
        return redirect(url_for('login'))

    return render_template('usermenu.html', user=user)

def delete_account():
    if 'user_id' not in session:
        flash('You need to login first.', 'danger')
        return redirect(url_for('login'))

    user = User.query.get(session['user_id'])
    if not user:
        flash('User not found.', 'danger')
        return redirect(url_for('login'))

    db.session.delete(user)
    db.session.commit()

    session.clear()
    flash('Your account has been deleted.', 'success')
    return redirect(url_for('login'))

@app.route('/add_book', methods=['GET', 'POST'])
def add_book():
   if request.method == 'GET':
        return render_template('add_book.html')
   else:

    form = AddbookForm()
    if request.method == 'POST' and form.validate_on_submit():
     book=Bookshelf(title=form.title.data, author=form.author.data,pages=form.page_counts)
     db.session.add(book)
     db.session.commit()
     flash('You are now Created!', 'success')
   return redirect(url_for('user_menu'))


@app.route('/my_books', methods=['GET', 'POST'])
def my_books():
    pass
@app.route('/update', methods=['GET', 'POST'])
def update_book():
    pass
@app.route('/delete', methods=['GET', 'POST'])
def delete_book():
    pass