from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
# from flask_app.models import user
from flask_app.models import categories

class Item:
    db = 'SecondHandSourcing'
    def __init__(self , data):
        self.id = data['id']
        self.item_name = data['item_name']
        self.cost = data ['cost']
        self.location = data ['location']
        self.image = data['image']
        self.breif_desc = data ['breif_desc']
        self.details = data ['details']
        self.user_id = data['user_id']
        self.categories_id = data ['categories_id']
        self.user = None
        self.category = None

    @classmethod
    def get_all(cls):
        query = 'SELECT * FROM items;'
        results = connectToMySQL(cls.db).query_db(query)
        items = []
        for row in results:
            items.append(cls(row))
        return items

    @classmethod
    def get_one(cls, data):
        query = 'SELECT * FROM items WHERE id = %(id)s;'
        results = connectToMySQL(cls.db).query_db(query, data)
        if len(results) < 1:
            return False
        return cls(results[0])

    @classmethod
    def save(cls, data):
        query = 'INSERT INTO items (item_name, cost, location, image, breif_desc, details, user_id, categories_id) VALUES (%(item_name)s, %(cost)s, %(location)s, %(image)s, %(breif_desc)s, %(details)s, %(user_id)s, %(categories_id)s);'
        return connectToMySQL(cls.db).query_db(query, data)

    @classmethod
    def update(cls, data):
        query = 'UPDATE items SET item_name = %(item_name)s, cost = %(cost)s, location = %(location)s, image = %(image)s, breif_desc = %(breif_desc)s, details = %(details)s WHERE id = %(id)s'
        print('update', data)
        return connectToMySQL(cls.db).query_db(query, data)

    @classmethod
    def delete(cls, data):
        query = "DELETE FROM items WHERE id = %(id)s"
        return connectToMySQL(cls.db).query_db(query, data)

    @classmethod
    def itemUser(cls, data):
        # Left join statement for items and users relationship
        pass

    @staticmethod
    def validate(item):
        pass
