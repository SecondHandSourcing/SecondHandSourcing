from flask_app import app
from flask import render_template, redirect, session, request, flash
# from flask_app.models.user import User
from flask_app.models.item import Item

@app.route('/dashboard')
def itemsDashboard():
    if 'users_id' not in session:
        return redirect('/')
    else:
        data = {
            'id': session['users_id']
        }
        users = User.get_all()
        user = User.get_one(data)
        items = Item.get_all()
        return render_template('dashboard.html', user = user, users=users, items=items)

@app.route('/item/add')
def newItem():
    if 'users_id' not in session:
        return render_template('login.html')
    else:
        data = {
            'id': session['users_id']
        }
        user = User.get_one(data)
        return render_template('createItem.html', user=user)

@app.route('/item/create', methods=['POST'])
def createItem():
    isValid = Item.validate(request.form)
    if not isValid:
        return redirect('/item/add')
    else:
        data = {
            'item_name': request.form['item_name'],
            'cost': request.form['cost'],
            'location': request.form['location'],
            'image': request.form['image'],
            'brief_desc': request.form['brief_desc'],
            'details': request.form['details'],
            'user_id': request.form['user_id']
        }
        Item.save(data)
        return redirect('/dashboard')

@app.route('/item/<int:items_id>/edit')
def editItem(items_id):
    if 'users_id' not in session:
        return render_template('login.html')
    else:
        dataUser = {
            'id': session['users_id']
        }
        user = User.get_one(dataUser)
        dataItem = {
            'id': items_id
        }
        item = Item.get_one(dataItem)
        return render_template('update.html', user=user, item=item)

@app.route('/item/<int:items_id>/update', methods=['POST'])
def updateItem(items_id):
    isValid = Item.validate(request.form)
    if not isValid:
        return redirect(f"/item/{items_id}/edit")
    else:
        data = {
            'id': items_id,
            'item_name': request.form['item_name'],
            'cost': request.form['cost'],
            'location': request.form['location'],
            'image': request.form['image'],
            'brief_desc': request.form['brief_desc'],
            'details': request.form['details'],
        }
        Item.update(data)
        return redirect('/dashboard')

@app.route('/item/<int:items_id>')
def viewItem(items_id):
    if 'users_id' not in session:
        return render_template('login.html')
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
        return render_template('viewItem.html', users=users, user=user, item=item)

@app.route('/item/<int:items_id>/delete')
def deleteItems(items_id):
    dataItem = {
        'id': items_id
    }
    Item.delete(dataItem)
    return redirect('/dashboard')
