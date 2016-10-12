from app import app
from flask import render_template, flash, redirect
from app.forms import LoginForm

@app.route('/')
@app.route('/index')
def index():
    user = {'nickname':'hanyu'}
    posts = [
        {
            'author':{'nickname':'John'},
            'body':'Beautiful day in Portland!'
        },
        {
            'author':{'nickname':'Susan'},
            'body':'The Avengers movies was so cool!'
        }
    ]
    return render_template("index.html",title='myhome',user=user,posts=posts)
@app.route('/login',methods=['GET','POST'])
def login():
    form =  LoginForm()
    if form.validate_on_submit():
        flash('Login request for Name:'+form.name.data)
        flash('passwd:'+str(form.password.data))
        flash('remember_me:'+str(form.remember_me.data))
        return redirect('/index')
    return render_template('login.html',title='sign in',form=form)