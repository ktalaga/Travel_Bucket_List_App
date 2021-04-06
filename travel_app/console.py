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

country_image_1 = "https://scotland5gcentre.org/wp-content/uploads/2020/06/rural-800x800.jpg"
country_1 = Country('Scotland', country_image_1, True)
country_repository.save(country_1)

country_image_2 = "https://www.wandermum.co.uk/wp-content/uploads/2017/04/Troutbeck-Park-and-Farmhouse-Cumbria.-Beatrix-Potter.-%C2%A9VisitBritain-Britain-on-View.-800x800.jpg"
country_2 = Country('England', country_image_2)
country_repository.save(country_2)

# country_3 = Country('Poland')
# country_repository.save(country_3)

# country_4 = Country('Canada')
# country_repository.save(country_4)

# country_5 = Country('Vietnam')
# country_repository.save(country_5)

# country_6 = Country('Turkey')
# country_repository.save(country_6)

# country_7 = Country('Georgia')
# country_repository.save(country_7)

# country_8 = Country('USA')
# country_repository.save(country_8)



# city_1 = City('Aberdeen', country_1)
# city_repository.save(city_1)

# city_2 = City('Glasgow', country_1)
# city_repository.save(city_2)

# city_3 = City('Edinburgh', country_1)
# city_repository.save(city_3)

# city_4 = City('Falkirk', country_1)
# city_repository.save(city_4)

# city_8 = City('Inverness', country_1)
# city_repository.save(city_8)

# city_5 = City('Perth', country_1)
# city_repository.save(city_5)

# city_6 = City('Dundee', country_1)
# city_repository.save(city_6)

# city_7 = City('Glenrothes', country_1)
# city_repository.save(city_7)



# city_9 = City('London', country_2, True)
# city_repository.save(city_9)

# city_10 = City('Manchester', country_2, True)
# city_repository.save(city_10)

# city_11 = City('Leeds', country_2, True)
# city_repository.save(city_11)

# city_12 = City('Liverpool', country_2, True)
# city_repository.save(city_12)

# city_13 = City('Newcastle', country_2, True)
# city_repository.save(city_13)

# city_14 = City('Birmingham', country_2, True)
# city_repository.save(city_14)

# city_15 = City('Sheffield', country_2, True)
# city_repository.save(city_15)

# city_16 = City('Bristol', country_2, True)
# city_repository.save(city_16)

# city_17 = City('Cracow', country_3)
# city_repository.save(city_17)



# sight_1 = Sight('Royal Albert Hall', city_9)
# sight_repository.save(sight_1)

# sight_2 = Sight('Tower Bridge', city_9)
# sight_repository.save(sight_2)

# sight_3 = Sight('Big Ben', city_9)
# sight_repository.save(sight_3)

# sight_4 = Sight('Tower of London', city_9)
# sight_repository.save(sight_4)

# sight_5 = Sight('Buckingham Palace', city_9)
# sight_repository.save(sight_5)

# sight_6 = Sight('Wawel Royal Castle', city_17)
# sight_repository.save(sight_6)

# sight_6 = Sight('The Jewish Quarter', city_17)
# sight_repository.save(sight_6)

# sight_6 = Sight('Salt Mine', city_17)
# sight_repository.save(sight_6)







pdb.set_trace()