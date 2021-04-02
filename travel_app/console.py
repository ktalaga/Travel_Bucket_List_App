import pdb

from models.country import Country
from models.city import City
from models.sight import Sight


import repositories.country_repository as country_repository
import repositories.city_repository as city_repository

country_repository.delete_all()



country_1 = Country('Scotland')
country_repository.save(country_1)

city_1 = City('Aberdeen')
city_repository.save(city_1)