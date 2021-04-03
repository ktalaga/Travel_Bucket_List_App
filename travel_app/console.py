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

country_3 = Country('Poland')
country_repository.save(country_3)

country_4 = Country('Canada')
country_repository.save(country_4)

country_5 = Country('Vietnam')
country_repository.save(country_5)

country_6 = Country('Turkey')
country_repository.save(country_6)

country_7 = Country('Georgia')
country_repository.save(country_7)

country_8 = Country('USA')
country_repository.save(country_8)



city_1 = City('Aberdeen', country_1)
city_repository.save(city_1)

city_2 = City('Glasgow', country_1)
city_repository.save(city_2)

city_3 = City('Edinburgh', country_1)
city_repository.save(city_3)

city_4 = City('Falkirk', country_1)
city_repository.save(city_4)

city_8 = City('Inverness', country_1)
city_repository.save(city_8)

city_5 = City('Perth', country_1)
city_repository.save(city_5)

city_6 = City('Dundee', country_1)
city_repository.save(city_6)

city_7 = City('Glenrothes', country_1)
city_repository.save(city_7)



city_2 = City('London', country_2)
city_repository.save(city_2)



sight_1 = Sight('Royal Albert Hall', city_2)
sight_repository.save(sight_1)

sight_2 = Sight('Tower Bridge', city_2)
sight_repository.save(sight_2)

sight_3 = Sight('Big Ben', city_2)
sight_repository.save(sight_3)

sight_4 = Sight('Tower of London', city_2)
sight_repository.save(sight_4)

sight_5 = Sight('Buckingham Palace', city_2)
sight_repository.save(sight_5)







pdb.set_trace()