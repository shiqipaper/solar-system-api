from app import create_app, db
from app.models.planets import Planet

my_app = create_app()
with my_app.app_context():
    db.session.add(Planet(id=1, name="Mercury",surface_area=2888,moons_num=0,distance_from_sun=3598, description="Roman god of travelers, aka Hermes.")),
    db.session.add(Planet(id=2,name="Venus",surface_area=1777, moons_num=0,distance_from_sun=6724, description="Roman goddess of love, aka Aphrodite.")),
    db.session.add(Planet(id=3,name="Earth",surface_area=9296,moons_num=1,distance_from_sun=9296, description="A variation on the word ""ground"" in several languages.")),
    db.session.add(Planet(id=4, name="Mars",surface_area=5591,moons_num=2,distance_from_sun=1416, description="Roman god of war, aka Ares.")),
    db.session.add(Planet(id=5,name="Jupiter",surface_area=2371,moons_num=79,distance_from_sun=4833, description="Jupiters father and titan aka, Chronos.")),
    db.session.add(Planet(id=6, name="Saturn",surface_area=2941,moons_num=62,distance_from_sun=8907, description="King of the Roman gods, aka Zeus.")),
    db.session.add(Planet(id=7, name="Uranus", surface_area=3121, moons_num=27, distance_from_sun=1787, description="Greek personification of the sky or heavens, aka Caelus.")),
    db.session.add(Planet(id=8,name="Neptune", surface_area=2941, moons_num=14, distance_from_sun=2798, description="Roman god of the sea aka, Poseidon."))
    db.session.commit()

