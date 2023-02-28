"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
from flask import Flask, request, jsonify, url_for, Blueprint
from api.models import db, User, Character, Planet, Vehicle, Fav_char, Fav_planet, Fav_veh
from api.utils import generate_sitemap, APIException
import json
from flask_jwt_extended import create_access_token
from flask_jwt_extended import get_jwt_identity
from flask_jwt_extended import jwt_required
from flask_jwt_extended import JWTManager


api = Blueprint('api', __name__)


@api.route('/hello', methods=['POST', 'GET'])
def handle_hello():

    response_body = {
        "message": "Hello! I'm a message that came from the backend, check the network tab on the google inspector and you will see the GET request"
    }

    return jsonify(response_body), 200

@api.route('/all_characters', methods=['GET'])
def all_characters():

    char = Character.query.all()
    char_list =  list(map(lambda x: x.serialize(), char))
    response = jsonify(char_list)
    
    return response

@api.route('/all_planets', methods=['GET'])
def all_planets():

    plan = Planet.query.all()
    plan_list =  list(map(lambda x: x.serialize(), plan))
    response = jsonify(plan_list)
    
    return response

@api.route('/all_vehicles', methods=['GET'])
def all_vehicles():

    veh = Vehicle.query.all()
    veh_list =  list(map(lambda x: x.serialize(), veh))
    response = jsonify(veh_list)
    
    return response

@api.route('/character/<int:position>', methods=['GET'])
def specific_char(position):

    char = Character.query.filter_by(id=position).first()
    return jsonify(char.serialize())

@api.route('/planet/<int:position>', methods=['GET'])
def specific_planet(position):

    plan = Planet.query.filter_by(id=position).first()
    return jsonify(plan.serialize())

@api.route('/vehicle/<int:position>', methods=['GET'])
def specific_veh(position):

    veh = Vehicle.query.filter_by(id=position).first()
    return jsonify(veh.serialize())
