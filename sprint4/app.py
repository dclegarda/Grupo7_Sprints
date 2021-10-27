import os
from flask import Flask, render_template, g, flash, request, session, url_for,send_file,make_response
from flask.ctx import AppContext
from werkzeug.security import generate_password_hash, check_password_hash
from werkzeug.utils import redirect
from db import close_db, get_db

app = Flask(__name__)

app.secret_key=os.urandom(24)

@app.route('/', methods=('GET', 'POST'))
@app.route('/signIn', methods=('GET', 'POST'))
def signIn():
    #TODO
    try:
        if request.method == 'POST':
            print('Beginning')
            db = get_db()
            error = None
            print('before of the beginning')
            username = request.form['username']
            password = request.form['password']            
            if not username:
                error = 'You must enter your username'
                flash(error)
                return render_template('signIn.html')           
            if not password:
                error = 'password required'
                flash(error)
                return render_template('signIn.html')
            print('Tester2')   
            user = db.execute(
                'SELECT * FROM user WHERE username = ?', (username,)).fetchone()
            print(user)
            if user is None:
                error = 'User not found'
                flash(error)
                print("User not found")                
            else:
                print("Usuario encontrado", user)
                
                print(user)
                stored_passwords=user[5]                
                print(stored_passwords)
                print(generate_password_hash(password))
                result=check_password_hash(stored_passwords,password)
                print(result)              
                if (result==False):
                    error = 'Consulta realizada: Usuario o contraseña inválidos'
                    print('Consulta realizada: Usuario o contraseña inválidos')
                    return render_template('createUser.html')
                else:
                    error = 'Consulta realizada: Usuario valido'
                    print("Usuario y contraseña correctos")
                    session.clear()
                    session["user_id"]=user[0]
                    session["username"]=user[1]
                    # session["rol"]=user[1]
                    return render_template('mainWeb.html') 
        return render_template('signIn.html')
    except:
        return render_template('signIn.html')


@app.route('/mainWeb')
def mainWeb():
    user_id = session.get( 'user_id' )
    if user_id is None:
        return redirect( url_for( 'signIn' ) )
    else:
        #if (session.get( 'rol' )=='cliente'):
            return render_template('mainWeb.html')

@app.route('/create')
def createPage():
    return render_template('createPage.html')

@app.route('/createuser', methods=('GET', 'POST'))
def createUser():    

    #TODO
    try:
        if request.method=='POST':
            print("inicia")
            username=request.form['username']
            firstName=request.form['first_name']  
            lastName=request.form['last_name'] 
            email=request.form['email']         
            password=request.form['password']           
            error=None
            db = get_db()
            print("base de datos conectada")    
            if error is not None:
                return render_template("signIn.html")
            else:
                db.execute("INSERT INTO user (username, first_name, last_name, email, password) VALUES (?,?,?,?,?)",
                     (username, firstName, lastName, email, generate_password_hash (password)))
                db.commit()
        return render_template('createUser.html')
    except:
        return render_template('createUser.html')

@app.route('/createproduct', methods=('GET', 'POST'))
def createProduct():
    return render_template('createProduct.html')

@app.route('/createprovider', methods=('GET', 'POST'))
def createProvider():
    return render_template('createProvider.html')

   
@app.route('/edit', methods=('GET', 'POST'))
def editPage():
    return render_template('editPage.html')

@app.route('/edituser', methods=('GET', 'POST'))
def editUser():
    return render_template('editUser.html')

@app.route('/editproduct', methods=('GET', 'POST'))
def editProduct():
    return render_template('editProduct.html')

@app.route('/editprovider', methods=('GET', 'POST'))
def editProvider():
    return render_template('editProvider.html')



@app.route('/delete', methods=('GET', 'POST'))
def deletePage():
    return render_template('deletePage.html')

@app.route('/deleteuser', methods=('GET', 'POST'))
def deleteUser():
    return render_template('deleteUser.html')

@app.route('/deleteproduct', methods=('GET', 'POST'))
def deleteProduct():
    return render_template('deleteProduct.html')

@app.route('/deleteprovider', methods=('GET', 'POST'))
def deleteProvider():
    return render_template('deleteProvider.html')


@app.route('/search', methods=('GET', 'POST'))
def search():
    return render_template('search.html')

@app.route('/product', methods=('GET', 'POST'))
def searchProduct():
    return render_template('productDescription.html')

@app.route('/provider', methods=('GET', 'POST'))
def searchProvider():
    return render_template('providerDescription.html')

if __name__=='__main__':
    app.run(debug=True)