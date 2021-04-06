from db.run_sql import run_sql
from models.city import City
from models.country import Country

import repositories.country_repository as country_repository

def save(city):
    sql = "INSERT INTO cities(name, picture_url, visited, country_id) VALUES ( %s, %s, %s, %s ) RETURNING id"
    values = [city.name, city.picture_url, city.visited, city.country.id]
    results = run_sql( sql, values )
    city.id = results[0]['id']
    return city


def delete_all():
    sql = "DELETE FROM cities"
    run_sql(sql)


def select_all():
    cities = []

    sql = "SELECT * FROM cities"
    results = run_sql(sql)

    for row in results:
        country = country_repository.select(row['country_id'])
        city = City(row['name'], row['picture_url'], country, row['visited'], row['id'])
        cities.append(city)
    return cities

def mark_visited(id):
    sql = "UPDATE cities SET visited = %s WHERE id = %s"
    values = [True, id]
    run_sql(sql, values)


def select(id):
    city = None
    sql = "SELECT * FROM cities WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]

    if result is not None:
        country = country_repository.select(result['country_id'])
        city = City(result['name'], result['picture_url'], country, result['visited'], result['id'] )
    return city

def delete(id):
    sql = "DELETE FROM cities WHERE id = %s"
    values = [id]
    run_sql(sql, values)

def update(city):
    sql = "UPDATE cities SET (name, picture_url, country_id, visited) = (%s, %s, %s, %s) WHERE id = %s"
    values = [city.name, city.picture_url, city.country.id, city.visited, city.id]
    run_sql(sql, values)

def mark_notvisited(id):
    sql = "UPDATE cities SET visited = %s WHERE id = %s"
    values = [False, id]
    run_sql(sql, values)