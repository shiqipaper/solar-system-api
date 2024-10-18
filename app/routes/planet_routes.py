from flask import Blueprint
from ..models.planets import planets

# endpoints
planets_bp = Blueprint("planets_bp", __name__, url_prefix = "/planets")

@planets_bp.get("")
def get_all_panets():
  result = []

  for planet in planets:
    result.append(dict(
      id=planet.id,
      name=planet.name,
      description=planet.description
    ))
  return result