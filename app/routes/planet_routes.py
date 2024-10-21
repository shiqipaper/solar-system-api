from flask import Blueprint, abort, make_response
from ..models.planets import planets

# endpoint for reading all planets info
planets_bp = Blueprint("planets_bp", __name__, url_prefix = "/planets")

@planets_bp.get("/")
def get_all_panets():
  result = []

  for planet in planets:
    result.append(planet.to_dict())
  return result

# endpoint for reading one planet
@planets_bp.get("/<planet_id>")
def get_one_panet(planet_id):

  planet = validate_planet(planet_id)

  return planet.to_dict(), 200


def validate_planet(planet_id):
    try:
        planet_id = int(planet_id)
    except:
        response = {"message": f"planet {planet_id} invalid"}
        abort(make_response(response, 400))

    for planet in planets:
        if planet.id == planet_id:
            return planet

    response = {"message": f"planet {planet_id} not found"}
    abort(make_response(response, 404))
