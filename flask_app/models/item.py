from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
# from flask_app.models import user
from flask_app.models import category

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
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
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
    def get_user_items_by_user_id(cls, data):
        # Left join statement for items and users relationship
        query = """
                SELECT * 
                FROM users
                LEFT JOIN items
                ON users.id = items.user_id
                WHERE id = %(id)s
                """

        result = connectToMySQL(cls.db).query_db(query, data)

        user_with_items = cls(result[0])
        for each_item in result:
            item_data = {
                'id' : each_item['item.id'],
                'item_name' : each_item['item_name'],
                'cost' : each_item['cost'],
                'location' : each_item['location'],
                'image' : each_item['image'],
                'breif_desc' : each_item['breif_desc'],
                'details' : each_item['details'],
                'created_at' : each_item['created_at'],
                'updated_at' : each_item['updated_at'],
                'user_id' : each_item['user_id'],
                'categories_id' : each_item['categories_id']
        }
        single_item = Item(item_data)
        user_with_items.item_list.append(single_item)
        return user_with_items
            




        pass

    @classmethod

    @staticmethod
    def validate(item):
        pass
