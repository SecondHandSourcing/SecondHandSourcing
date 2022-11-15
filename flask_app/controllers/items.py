from flask_app import app
from flask import render_template, redirect, session, request, flash
from flask_app.models.user import User
from flask_app.models.item import Item

@app.route('/dashboard')
def itemsDashboard():
    if 'user_id' not in session:
        return redirect('/')
    else:
        data = {
            'id': session['user_id']
        }
        users = User.get_all()
        user = User.get_one(data)
        items = Item.get_all()
        return render_template('dashboard.html', user = user, users=users, items=items)

@app.route('/item/add')
def newItem():
    if 'user_id' not in session:
        return render_template('login.html')
    return render_template('createItem.html')

@app.route('/item/create', methods=['POST'])
def createItem():
    isValid = Item.validate(request.form)
    if not isValid:
        print("Item not saved")
        return redirect('/item/add')
    else:
        data = {
            'item_name': request.form['item_name'],
            'cost': request.form['cost'],
            'location': request.form['location'],
            'image': request.form['image'],
            'brief_desc': request.form['brief_desc'],
            'details': request.form['details'],
            'user_id': request.form['user_id'],
            'category': request.form['category']
        }
        Item.save(data)
        return redirect('/dashboard')

@app.route('/item/<int:id>/edit')
def edit_item_page(id):
    if 'user_id' not in session:
        return render_template('login.html')
    else:
        dataUser = {
            'id': session['user_id']
        }
        user = User.get_one(dataUser)
        dataItem = {
            'id': id
        }
        item = Item.get_item_by_id(id)
        return render_template('update.html', user=user, item=item)

@app.route('/item/<int:id>/update', methods=['POST'])
def update_item_by_id(id):
    isValid = Item.validate(request.form)
    if not isValid:
        return redirect(f"/item/{id}/edit")
    else:
        data = {
            'id': id,
            'item_name': request.form['item_name'],
            'cost': request.form['cost'],
            'location': request.form['location'],
            'image': request.form['image'],
            'brief_desc': request.form['brief_desc'],
            'details': request.form['details'],
        }
        Item.update_item_by_id(data)
        return redirect('/dashboard')

@app.route('/item/<int:id>')
def viewItem(id):
    if 'user_id' not in session:
        return render_template('login.html')
    item = Item.get_item_by_id(id)
    return render_template('viewItem.html', item=item)

@app.route('/item/<int:id>/delete')
def delete_item_by_id(id):
    dataItem = {
        'id': id
    }
    Item.delete_item_by_id(dataItem)
    return redirect('/dashboard')
