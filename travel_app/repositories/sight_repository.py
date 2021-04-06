from db.run_sql import run_sql
from models.sight import Sight
from models.city import City

import repositories.city_repository as city_repository

def save(sight):
    sql = "INSERT INTO sights(name, picture_url, visited, city_id) VALUES ( %s, %s, %s, %s) RETURNING id"
    values = [sight.name, sight.picture_url, sight.visited, sight.city.id]
    results = run_sql( sql, values )
    sight.id = results[0]['id']
    return sight


def delete_all():
    sql = "DELETE FROM sights"
    run_sql(sql)


def select_all():
    sights = []

    sql = "SELECT * FROM sights"
    results = run_sql(sql)

    for row in results:
        city = city_repository.select(row['city_id'])
        sight = Sight(row['name'],row['picture_url'], city, row['visited'], row['id'])
        sights.append(sight)
    return sights

def mark_visited(id):
    sql = "UPDATE sights SET visited = %s WHERE id = %s"
    values = [True, id]
    run_sql(sql, values)


def select(id):
    sight = None
    sql = "SELECT * FROM sights WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]

    if result is not None:
        city = city_repository.select(result['city_id'])
        sight = Sight(result['name'], result['picture_url'], city, result['visited'], result['id'] )
    return sight

def delete(id):
    sql = "DELETE FROM sights WHERE id = %s"
    values = [id]
    run_sql(sql, values)

def update(sight):
    sql = "UPDATE sights SET (name, picture_url, city_id, visited) = (%s, %s, %s, %s) WHERE id = %s"
    values = [sight.name, sight.picture_url, sight.city.id, sight.visited, sight.id]
    run_sql(sql, values)

def mark_notvisited(id):
    sql = "UPDATE sights SET visited = %s WHERE id = %s"
    values = [False, id]
    run_sql(sql, values)