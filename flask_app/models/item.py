from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
from flask_app.models import user
from flask_app.models import category

class Item:
    db = 'SecondHandSourcingSchema'
    def __init__(self , data):
        self.id = data['id']
        self.item_name = data['item_name']
        self.cost = data ['cost']
        self.location = data ['location']
        self.image = data['image']
        self.brief_desc = data ['brief_desc']
        self.details = data ['details']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.user_id = data['user_id']
        self.category = data ['category']
        self.user = None
        self.category = None

    @classmethod
    def get_all(cls):
        query = """
            SELECT * 
            FROM items;
        """
        results = connectToMySQL(cls.db).query_db(query)
        items = []
        for row in results:
            items.append(cls(row))
        return items

    @classmethod
    def get_one(cls, id):
        data = {'id': id}
        query = """
        SELECT *
        FROM items
        WHERE id = %(id)s;
        ;"""
        results = connectToMySQL(cls.db).query_db(query, data)
        if len(results) < 1:
            return False
        return cls(results[0])

    @classmethod
    def save(cls, data):
        query = """
            INSERT INTO items (item_name, cost, location, image, brief_desc, details, user_id, category)
            VALUES (%(item_name)s, %(cost)s, %(location)s, %(image)s, %(brief_desc)s, %(details)s, %(user_id)s, %(category)s);
            """
        return connectToMySQL(cls.db).query_db(query, data)

    @classmethod
    def update(cls, data):
        query = """
        UPDATE items 
        SET item_name = %(item_name)s, cost = %(cost)s, location = %(location)s, image = %(image)s, brief_desc = %(brief_desc)s, details = %(details)s 
        WHERE id = %(id)s
        ;"""
        print('update', data)
        return connectToMySQL(cls.db).query_db(query, data)

    @classmethod
    def delete(cls, id):
        data = { 'id':id} 
        query = """
            DELETE FROM items
            WHERE id = %(id)s;
        """
        return connectToMySQL(cls.db).query_db(query, data)


    @staticmethod
    def validate(item):
        isValid = True
        if len(item['item_name']) < 2:
            isValid = False
            print("item_name failed")
            flash ('Please enter a name with at least 2 Characters!')
        if len(item['cost']) <= 0:
            isValid = False
            print("cost failed")
            flash ('Price must be greater than 0!')
        if len(item['location']) < 2:
            isValid = False
            print("location failed")
            flash ('Please enter a location with at least 2 Characters!')
        if len(item['brief_desc']) > 25:
            isValid = False
            print("brief_desc failed")
            flash ('Description can be a maximum of 25 characters!')
        if len(item['details']) < 2:
            isValid = False
            print("details failed")
            flash ('Please enter details with at least 2 Characters!')
        return isValid
