from flask import Flask , flash, redirect

# from flask.templating import render_template_string
from flask.templating import render_template, render_template_string
from datetime import datetime
from mymodel import db        
from mymodel import User        
from forms  import LoginForm, SearchUserByName

app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'

app.debug = True
app.config['SECRET_KEY'] = 'a really really really really long secret key 12345 '

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:test1234@localhost/flask_app_db'
# manager = Manager(app)

# db = SQLAlchemy(app)
# db = SQLAlchemy()
db.init_app(app)

 

@app.route('/index')
@app.route('/')
@app.route('/list')
def list():
    users = User.query.all()
    return  render_template('list.html',users=users) 

@app.route('/view/<userid>')
def view(userid):    
    user = User.query.filter_by(id=userid).first_or_404()
    return render_template('show_user.html', user=user)

@app.route('/createdb')
def createdb():
    db.create_all()
    db.session.commit()
    return render_template_string( '{% include "_header.html" %}db create all table' \
    ) 

@app.route('/insert101')
def insert101():
    u = User(id=101,username='user1',email="u1@mail.test")
    db.session.add(u)
    db.session.commit()
    return "insert 101 ok "

@app.route('/insert202')
def insert102():
    u = User(id=202,username='user202',email="u202@mail.test")
    db.session.add(u)
    db.session.commit()
    return "insert 202 ok "

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    # if form.validate(): 
    if form.validate_on_submit():
        flash('Login requested for user {}, remember_me={}'.format(
            form.username.data, form.remember_me.data))
        return redirect('/index')
    return render_template('login.html', title='Sign In', form=form)

@app.route('/login_do', methods=[ 'POST'])
def login_do():
    form = LoginForm()
    # if form.validate(): 
    if form.validate_on_submit():
        flash('Login requested for user {}, remember_me={}'.format(
            form.username.data, form.remember_me.data))
        return redirect('/index')
    return redirect('/list')

@app.route('/user/search', methods=['GET','POST'])
def user_search():
    form = SearchUserByName()
    error_msg = "no-error "  + datetime.now().strftime("%H:%M:%S") + " :: " 
    # if form.validate(): 
    if form.validate_on_submit():
        error_msg += "> on_submit"
        # flash('Login requested for user {}, remember_me={}'.format(
        #     form.username.data, form.remember_me.data))
        # return redirect('/index')
        u1 = User.query.filter_by(username=form.username.data).first()
        if u1  : 
            return redirect('/view/' +  str(u1.id) )
        else: 
            # flash()
            error_msg = 'Not Found  /' +  form.username.data   + "/"
    else:
        error_msg += " / (Not Valid Input) "

    return render_template('user_searh.html', title='User ค้นหา', form=form ,error_msg = error_msg)


if __name__ =="__main__":
    app.run(debug=True)
    

# Flask คืออะไร  ติดตั้ง รัน บน Apache 
# REF https://saixiii.com/python-flask-web-application/
#pip install Flask

#REF https://stackpython.co/tutorial/flask-sqlalchemy-orm
#pip install flask_sqlalchemy


#Flask alchemy  
# REF https://stackpython.co/tutorial/flask-sqlalchemy-orm
# REF https://flask-sqlalchemy.palletsprojects.com/en/2.x/quickstart/#a-minimal-application
# REF https://flask-sqlalchemy.palletsprojects.com/en/2.x/quickstart/#a-minimal-application

# venv 
# REF https://docs.python.org/3/library/venv.html

# Why python 
# Blog  https://www.imaginarycloud.com/blog/why-use-python-for-web-development/

# Node.js vs Python as WebApp 
# Blog  https://www.guru99.com/node-js-vs-python.html 

# Run python web app in production  
#  waitress
# REF https://stackoverflow.com/questions/51025893/flask-at-first-run-do-not-use-the-development-server-in-a-production-environmen

# templating 
# REF https://www.fullstackpython.com/flask-templating-render-template-string-examples.html
# REF https://flask.palletsprojects.com/en/1.1.x/quickstart/ 

#templating for loop 
# REF https://www.geeksforgeeks.org/python-using-for-loop-in-flask/
# REF https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-ii-templates

# session in flask 
#  REF https://overiq.com/flask-101/sessions-in-flask/

# Flask database model and MySQL 
# REF https://overiq.com/flask-101/database-modelling-in-flask/

# install pymysql for use with mysql 
# example : 
# >Script\activate      ; activate venv  
# >pip install pymysql  

# Run Flask shell 
# REF  https://stackoverflow.com/questions/48125990/db-create-all-not-creating-tables-in-flask-sqlaclchemy/48134006
#  Example :  (venv) $ py -m flask shell

# Separate Model in another python file (very importance )
# REF  https://stackoverflow.com/questions/9692962/flask-sqlalchemy-import-context-issue/9695045#9695045

# Flask form helper (WTF)
# REF  https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-iii-web-forms 
# Example install :  (venv) $ pip install flask-wtf

# Flask form Validate , with custom validate 
# https://stackabuse.com/flask-form-validation-with-flask-wtf