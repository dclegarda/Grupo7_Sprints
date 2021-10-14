from flask import Flask, render_template

app = Flask(__name__)

@app.route('/login')
def login():
    return render_template('signIn.html')

@app.route('/login/signin')
def signin():
    return render_template('mainWeb.html')

@app.route('/login/signin/create')
def createPage():
    return render_template('createPage.html')

@app.route('/login/signin/create/createuser')
def createUser():
    return render_template('createUser.html')

@app.route('/login/signin/create/createproduct')
def createProduct():
    return render_template('createProduct.html')

@app.route('/login/signin/create/createprovider')
def createProvider():
    return render_template('createProvider.html')

   
   
@app.route('/login/signin/edit')
def editPage():
    return render_template('editPage.html')

@app.route('/login/signin/edit/edituser')
def editUser():
    return render_template('editUser.html')

@app.route('/login/signin/edit/editproduct')
def editProduct():
    return render_template('editProduct.html')

@app.route('/login/signin/edit/editprovider')
def editProvider():
    return render_template('editProvider.html')



@app.route('/login/signin/delete')
def deletePage():
    return render_template('deletePage.html')

@app.route('/login/signin/delete/deleteuser')
def deleteUser():
    return render_template('deleteUser.html')

@app.route('/login/signin/delete/deleteproduct')
def deleteProduct():
    return render_template('deleteProduct.html')

@app.route('/login/signin/delete/deleteprovider')
def deleteProvider():
    return render_template('deleteProvider.html')


@app.route('/login/signin/search')
def search():
    return render_template('search.html')

@app.route('/login/signin/search/product')
def searchProduct():
    return render_template('productDescription.html')

@app.route('/login/signin/search/provider')
def searchProvider():
    return render_template('providerDescription.html')