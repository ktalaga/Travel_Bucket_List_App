import pdb

from models.country import Country
from models.city import City
from models.sight import Sight


import repositories.country_repository as country_repository
import repositories.city_repository as city_repository
import repositories.sight_repository as sight_repository

country_repository.delete_all()
city_repository.delete_all()
sight_repository.delete_all()


country_1 = Country('Scotland')
country_repository.save(country_1)

country_2 = Country('England')
country_repository.save(country_2)

city_1 = City('Aberdeen', country_1)
city_repository.save(city_1)

city_2 = City('London', country_2)
city_repository.save(city_2)

sight_1 = Sight('Royal Albert Hall', city_2)
sight_repository.save(sight_1)