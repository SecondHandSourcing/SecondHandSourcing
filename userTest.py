from flask_app.models import user, item

user1 = {
    'first_name' : 'marge',
    'last_name' : 'simpson',
    'email' : 'ms@gmail.com',
    'password' : 'password',
    'birthdate' : '2000-01-01',
    'confirm_password' : 'password'
} 

user2 = {
    'first_name' : 'homer',
    'last_name' : 'simpson',
    'email' : 'hs@gmail.com',
    'password' : 'password1',
    'birthdate' : '2000-02-02',
    'confirm_password' : 'password1'
} 

user3 = {
    'id': 2,
    'first_name' : 'maggie',
    'last_name' : 'simpson',
    'email' : 'ms@gmail.com',
    'password' : 'password3',
    'birthdate' : '2000-03-03',
    'confirm_password' : 'password3'
} 

# user.User.create_user(user1)
# print(user1)

# user.User.create_user(user2)
# print(user2)

# print(user.User.get_user_by_email('ms@gmail.com'))

# print(user.User.update_user(user3))

# print(user.User.get_user_items_by_user_id(1))

# user.User.delete_user(1)