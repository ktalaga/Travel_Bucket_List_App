from db.run_sql import run_sql
from models.country import Country

def save(country):
    sql = "INSERT INTO countries(name, picture_url, visited) VALUES ( %s, %s, %s ) RETURNING id"
    values = [country.name, country.picture_url, country.visited]
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
        country = Country(row['name'], row['picture_url'], row['visited'], row['id'])
        countries.append(country)
    return countries

def select(id):
    country = None
    sql = "SELECT * FROM countries WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]

    if result is not None:
        country = Country(result['name'], result['picture_url'], result['visited'], result['id'] )
    return country

def delete(id):
    sql = "DELETE FROM countries WHERE id = %s"
    values = [id]
    run_sql(sql, values)

def update(country):
    sql = "UPDATE countries SET (name, picture_url, visited) = (%s, %s, %s) WHERE id = %s"
    values = [country.name, country.picture_url, country.visited, country.id]
    run_sql(sql, values)

def mark_visited(id):
    sql = "UPDATE countries SET visited = %s WHERE id = %s"
    values = [True, id]
    run_sql(sql, values)

def mark_notvisited(id):
    sql = "UPDATE countries SET visited = %s WHERE id = %s"
    values = [False, id]
    run_sql(sql, values)


