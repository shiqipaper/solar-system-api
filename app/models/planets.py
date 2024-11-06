from sqlalchemy.orm import Mapped, mapped_column
from ..db import db
from sqlalchemy import Integer, String, BIGINT

class Planet(db.Model):
  id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
  name: Mapped[str] = mapped_column(String(100), nullable=False)
  surface_area: Mapped[int] = mapped_column(BIGINT, nullable=False)
  moons_num: Mapped[int] = mapped_column(Integer, nullable=False)
  distance_from_sun: Mapped[int] = mapped_column(BIGINT, nullable=False)
  description: Mapped[str] = mapped_column(String(1000))

  def to_dict(self):
    return dict(
    id=self.id,
    name=self.name,
    surface_area=self.surface_area,
    moons_num=self.moons_num,
    distance_from_sun=self.distance_from_sun,
    description=self.description)

  @classmethod
  def from_dict(cls, planet_data):
    return cls(
      name=planet_data["name"],
      surface_area=planet_data["surface_area"],
      moons_num=planet_data["moons_num"],
      distance_from_sun=planet_data["distance_from_sun"],
      description=planet_data["description"],
    )

# ALTER TABLE table_name RENAME COLUMN old_column_name TO new_column_name;

# ALTER TABLE table_name ALTER COLUMN column_name SET DATA TYPE new_data_type;
