from db.run_sql import run_sql
from models.sight import Sight

def save(sight):
    sql = "INSERT INTO sights(name, visited, city_id) VALUES ( %s, %s, %s ) RETURNING id"
    values = [sight.name, sight.visited, sight.city.id]
    results = run_sql( sql, values )
    sight.id = results[0]['id']
    return sight

def delete_all():
    sql = "DELETE FROM cities"
    run_sql(sql)

def select_all():
    sights = []

    sql = "SELECT * FROM sights"
    results = run_sql(sql)

    for row in results:
        sight = Sight(row['name'], row['visited'], row['id'])
        sights.append(sight)
    return sights