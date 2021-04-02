from db.run_sql import run_sql
from models.city import City

def save(city):
    sql = "INSERT INTO cities(name, visited, country_id) VALUES ( %s, %s, %s ) RETURNING id"
    values = [city.name, city.visited, city.country.id]
    results = run_sql( sql, values )
    city.id = results[0]['id']
    return city

def delete_all():
    sql = "DELETE FROM cities"
    run_sql(sql)