from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
from flask_app.models import item

class Category:
    db = 'SecondHandSourcing'
    def __init__(self , data):
        self.id = data['id']
        self.furniture = data['furniture']
        self.clothing = data ['clothing']
        self.electronics = data ['electronics']
        self.outdoors = data['outdoors']
        self.toys = data ['toys']
        self.home = data ['home']
        self.pet_supply = data['pet_supply']
        self.cars = data['cars']
        self.cleaning = data['cleaning']
        self.miscellanous = data['miscellanous']
        self.categories_id = data ['categories_id']
        self.category = None