from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
from flask_app.models import item

class Category:
    db = 'SecondHandSourcing'
    def __init__(self , data):
        self.id = data['id']
        self.name = data['name']














