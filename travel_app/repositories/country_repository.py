from db.run_sql import run_sql
from models.country import Country

def save(country):
    sql = "INSERT INTO countries(name, visited) VALUES ( %s, %s ) RETURNING id"
    values = [country.name, country.visited]
    results = run_sql( sql, values )
    country.id = results[0]['id']
    return country

def delete_all():
    sql = "DELETE FROM countries"
    run_sql(sql)

def select_all():
    countries = []

    sql = "SELECT * FROM countries"
    results = run_sql(sql)

    for row in results:
        country = Country(row['name'], row['visited'], row['id'])
        countries.append(country)
    return countries

def select(id):
    country = None
    sql = "SELECT * FROM countries WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]

    if result is not None:
        country = Country(result['name'], result['visited'])
    return country