from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
from flask_app.models import item

class Category:
    db = 'SecondHandSourcingSchema'
    def __init__(self , data):
        self.id = data['id']
        self.name = data['name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def createCategory(cls, data):
        query = """
            INSERT INTO categories (name)
            VALUES (%(name)s);
            """
        return connectToMySQL(cls.db).query_db(query, data)














