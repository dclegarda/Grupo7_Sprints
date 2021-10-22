import os
from flask import Flask, render_template, g, flash, request, session, url_for,send_file,make_response
from flask.ctx import AppContext
from werkzeug.security import generate_password_hash, check_password_hash
from werkzeug.utils import redirect
from db import close_db, get_db

app = Flask(__name__)

@app.route('/login', methods=('GET', 'POST'))
def login():
    try:
        if request.method == 'POST':
            db = get_db()
            error = None
            username = request.form['username']
            password = request.form['password']
            if not username:
                error = 'You must enter your username'
                flash( error )
                return render_template( 'login.html' )
        if not password:
                error = 'Password required'
                flash( error )
                return render_template( 'login.html' )
        user = db.execute(
                'SELECT * FROM usuario WHERE usuario = ?', (username,)
        ).fetchone()
        contrasena_almacenada=user[4]
        resultado=check_password_hash(contrasena_almacenada,password)
        flash(resultado)
        
        if user is None:
                error = 'Consulta realizada : Usuario o contraseña inválidos'
        else:
                error = 'Consulta realizada : Usuario valido'
                session.clear()
                session["user_id"]=user[0]
                resp = make_response(redirect( url_for( 'send' ) ) )
                resp.set_cookie( 'username', username )
                return resp
        flash( error )
        return render_template('signIn.html')
    except:
        return render_template('signIn.html')


@app.route('/login/signIn')
def signIn():
    return render_template('mainWeb.html')

@app.route('/login/signIn/create')
def createPage():
    return render_template('createPage.html')

@app.route('/login/signIn/create/createuser')
def createUser():
    return render_template('createUser.html')

@app.route('/login/signIn/create/createproduct')
def createProduct():
    return render_template('createProduct.html')

@app.route('/login/signIn/create/createprovider')
def createProvider():
    return render_template('createProvider.html')

   
   
@app.route('/login/signIn/edit')
def editPage():
    return render_template('editPage.html')

@app.route('/login/signIn/edit/edituser')
def editUser():
    return render_template('editUser.html')

@app.route('/login/signIn/edit/editproduct')
def editProduct():
    return render_template('editProduct.html')

@app.route('/login/signIn/edit/editprovider')
def editProvider():
    return render_template('editProvider.html')



@app.route('/login/signIn/delete')
def deletePage():
    return render_template('deletePage.html')

@app.route('/login/signIn/delete/deleteuser')
def deleteUser():
    return render_template('deleteUser.html')

@app.route('/login/signIn/delete/deleteproduct')
def deleteProduct():
    return render_template('deleteProduct.html')

@app.route('/login/signIn/delete/deleteprovider')
def deleteProvider():
    return render_template('deleteProvider.html')


@app.route('/login/signIn/search')
def search():
    return render_template('search.html')

@app.route('/login/signIn/search/product')
def searchProduct():
    return render_template('productDescription.html')

@app.route('/login/signIn/search/provider')
def searchProvider():
    return render_template('providerDescription.html')