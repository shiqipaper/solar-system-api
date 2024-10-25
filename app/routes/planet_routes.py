from flask import Blueprint, abort, make_response,request
from app.models.planets import Planet
from ..db import db
# endpoint for reading all planets info
planets_bp = Blueprint("planets_bp", __name__, url_prefix = "/planets")

@planets_bp.post("")
def create_planet():
  request_body = request.get_json()
  name = request_body["name"]
  description = request_body["description"]
  random = request_body["random"]

  new_planet = Planet(name=name, description=description, random=random)
  db.session.add(new_planet)
  db.session.commit()

  response = new_planet.to_dict()
  return response, 201


@planets_bp.get("")
def get_all_planets():
  query = db.select(Planet).order_by(Planet.id)
  planets = db.session.scalars(query)

  planets_response = [planet.to_dict() for planet in planets]

  return planets_response, 200




# def get_all_panets():
#   result = []

#   for planet in planets:
#     result.append(planet.to_dict())
#   return result

# # endpoint for reading one planet
# @planets_bp.get("/<planet_id>")
# def get_one_panet(planet_id):

#   planet = validate_planet(planet_id)

#   return planet.to_dict(), 200


# def validate_planet(planet_id):
#     try:
#         planet_id = int(planet_id)
#     except:
#         response = {"message": f"planet {planet_id} invalid"}
#         abort(make_response(response, 400))

#     for planet in planets:
#         if planet.id == planet_id:
#             return planet

#     response = {"message": f"planet {planet_id} not found"}
#     abort(make_response(response, 404))
