class Planet:
    def __init__(self, id, name, description):
        self.id = id
        self.name = name
        self.description = description

    def to_dict(self):
        return dict(
        id=self.id,
        name=self.name,
        description=self.description)



planets = [
    Planet(1, "Mercury", "Smallest planet"),
    Planet(2, "Venus", "Earth's closet planet"),
    Planet(3, "Earth", "It has 71% of water"),
    Planet(4, "Mars", "It's red and has life"),
    Planet(5, "Jupiter", "It is a red planet"),
    Planet(6, "Saturn", "It is a gas planet"),
    Planet(7, "Uranus", "It is an ice planet"),
    Planet(8, "Neptune", "It is farthest from the sun"),
    Planet(9, "Pluto", "It's a dwarf planet")
]