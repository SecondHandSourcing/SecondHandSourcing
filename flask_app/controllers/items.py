from flask_app import app
from flask import render_template, redirect, session, request, flash
# from flask_app.models.user import User
from flask_app.models.item import Item

@app.route('/new/item')
def newItem():
    if 'users_id' not in session:
        return render_template('logreg.html')
    else:
        data = {
            'id': session['users_id']
        }
        user = User.get_one(data)
        return render_template('create.html', user=user)

@app.route('/create/item', methods=['POST'])
def createItem():
    isValid = Item.validate(request.form)
    if not isValid:
        return redirect('/new/item')
    else:
        data = {
            'item_name': request.form['item_name'],
            'cost': request.form['cost'],
            'location': request.form['location'],
            'image': request.form['image'],
            'breif_desc': request.form['breif_desc'],
            'details': request.form['details'],
            'user_id': request.form['user_id']
        }
        Item.save(data)
        return redirect('/dashboard')

@app.route('/edit/<int:items_id>')
def editItem(items_id):
    if 'users_id' not in session:
        return render_template('logreg.html')
    else:
        dataUser = {
            'id': session['users_id']
        }
        user = User.get_one(dataUser)
        dataItem = {
            'id': items_id
        }
        item = Item.get_one(dataItem)
        return render_template('edit.html', user=user, item=item)

@app.route('/item/update/<int:items_id>', methods=['POST'])
def updateItem(items_id):
    isValid = Item.validate(request.form)
    if not isValid:
        return redirect(f"/edit/{items_id}")
    else:
        data = {
            'id': items_id,
            'item_name': request.form['item_name'],
            'cost': request.form['cost'],
            'location': request.form['location'],
            'image': request.form['image'],
            'breif_desc': request.form['breif_desc'],
            'details': request.form['details'],
        }
        Item.update(data)
        return redirect('/dashboard')

@app.route('/item/view/<int:items_id>')
def viewSasquatch(items_id):
    if 'users_id' not in session:
        return render_template('logreg.html')
    else:
        dataUser = {
            'id': session['users_id']
        }
        dataItem = {
            'id': items_id
        }
        users = User.get_all()
        user = User.get_one(dataUser)
        item = Item.get_one(dataItem)
        return render_template('view.html', users=users, user=user, item=item)

@app.route('/item/delete/<int:items_id>')
def deleteItems(items_id):
    dataItem = {
        'id': items_id
    }
    Item.delete(dataItem)
    return redirect('/dashboard')
