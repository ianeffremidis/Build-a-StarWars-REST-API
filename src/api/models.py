import os
import sys
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine

db = SQLAlchemy()

class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), unique=False, nullable=False)
    last_name = db.Column(db.String(120), unique=False, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(80), unique=False, nullable=False)
    phone = db.Column(db.Integer, unique=True, nullable=False)

    def __repr__(self):
        return f'<User {self.email}>'

    def serialize(self):
        return {
            "id": self.id,
            "email": self.email,
            "phone": self.phone,
            "name": self.name,
            # do not serialize the password, its a security breach
        }
    def __init__(self, name, last_name, email, password, phone):
        self.name = name
        self.last_name = last_name
        self.email = email
        self.password = password
        self.phone = phone

class Character(db.Model):
    __tablename__ = 'character'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), unique=False, nullable=False)
    birth_year = db.Column(db.String(100), unique=False, nullable=False)
    gender = db.Column(db.String(100),  unique=False, nullable=False)
    height = db.Column(db.String(100), unique=False, nullable=False)
    skin_color = db.Column(db.String(100),  unique=False, nullable=False)
    eye_color = db.Column(db.String(100),  unique=False, nullable=False)
    image = db.Column(db.Text, unique=False, nullable=True)

    def __repr__(self):
        return f'<Character {self.name}>'

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "birth_year": self.birth_year,
            "gender": self.gender,
            "height":self.height,
            "skin_color": self.skin_color,
            "eye_color": self.eye_color,
            "image": self.image
        }
    def __init__(self, name, birth_year, gender, height, skin_color, eye_color, image):
        self.name = name
        self.birth_year = birth_year
        self.gender = gender
        self.height = height
        self.skin_color = skin_color
        self.eye_color = eye_color
        self.image = image

class Planet(db.Model):
    __tablename__ = 'planet'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True, nullable=False)
    population = db.Column(db.String(100), unique=False, nullable=False)
    rotation_period = db.Column(db.String(100), unique=False, nullable=False)
    surface_water = db.Column(db.String(100), unique=False, nullable=False)
    gravity = db.Column(db.String(100), unique=False, nullable=False)
    climate = db.Column(db.String(100), unique=False, nullable=False)
    image = db.Column(db.Text, unique=False, nullable=True)

    def __repr__(self):
        return f'<Planet {self.name}>'
    
    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "population":self.population,
            "rotation_period": self.rotation_period,
            "surface_water": self.surface_water,
            "gravity": self.gravity,
            "climate": self.climate,
            "image": self.image
        }
    def __init__(self, name, population, rotation_period, surface_water, gravity, climate, image):
        self.name = name
        self.population = population
        self.rotation_period = rotation_period
        self.surface_water = surface_water
        self.gravity = gravity
        self.climate = climate
        self.image = image    

class Vehicle(db.Model):
    __tablename__ = 'vehicle'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True, nullable=False)
    model = db.Column(db.String(100), unique=False, nullable=False)
    manufacturer = db.Column(db.String(100), unique=False, nullable=False)
    cost_in_credits = db.Column(db.Integer, unique=False, nullable=False)
    crew = db.Column(db.Integer, unique=False, nullable=False)
    passengers = db.Column(db.Integer, unique=False, nullable=False)
    image = db.Column(db.Text, unique=False, nullable=True)

    def __repr__(self):
        return f'<Vehicle {self.name}>'
    
    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "model":self.model,
            "manufacturer": self.manufacturer,
            "cost_in_credits": self.cost_in_credits,
            "crew": self.crew,
            "passengers": self.passengers,
            "image": self.image
        }
    def __init__(self, name, model, manufacturer, cost_in_credits, crew, passengers, image):
        self.name = name
        self.model = model
        self.manufacturer = manufacturer
        self.cost_in_credits = cost_in_credits
        self.crew = crew
        self.passengers = passengers
        self.image = image    

class Fav_char(db.Model):
    __tablename__ = 'fav_char'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, ForeignKey('user.id'))
    char_id = db.Column(db.Integer, ForeignKey('character.id'))

    def __repr__(self):
        return f'<Fav_car {self.char_id}>'
    
    def serialize(self):
        return {
            "id": self.id,
            "user_id": self.user_id,
            "char_id":self.char_id,
        }
    def __init__(self, user_id, char_id):
        self.user_id = user_id
        self.char_id = char_id

class Fav_planet(db.Model):
    __tablename__ = 'fav_planet'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, ForeignKey('user.id'))
    planet_id = db.Column(db.Integer, ForeignKey('planet.id'))

    def __repr__(self):
        return f'<Fav_planet {self.planet_id}>'
    
    def serialize(self):
        return {
            "id": self.id,
            "user_id": self.user_id,
            "planet_id":self.planet_id,
        }
    def __init__(self, user_id, planet_id):
        self.user_id = user_id
        self.planet_id = planet_id

class Fav_veh(db.Model):
    __tablename__ = 'fav_veh'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, ForeignKey('user.id'))
    veh_id = db.Column(db.Integer, ForeignKey('vehicle.id'))

    def __repr__(self):
        return f'<Fav_veh {self.veh_id}>'
    
    def serialize(self):
        return {
            "id": self.id,
            "user_id": self.user_id,
            "veh_id":self.veh_id,
        }
    def __init__(self, user_id, veh_id):
        self.user_id = user_id
        self.veh_id = veh_id
                   