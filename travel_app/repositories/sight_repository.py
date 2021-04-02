from db.run_sql import run_sql
from models.sight import Sight

def save(sight):
    sql = "INSERT INTO sights(name, visited) VALUES ( %s, %s ) RETURNING id"
    values = [sight.name, sight.visited]
    results = run_sql( sql, values )
    sight.id = results[0]['id']
    return sight

def delete_all():
    sql = "DELETE FROM cities"
    run_sql(sql)