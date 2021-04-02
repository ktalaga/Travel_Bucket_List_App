import pdb

from models.country import Country


import repositories.country_repository as country_repository





country_1 = Country('Scotland')
country_repository.save(country_1)