from db.run_sql import run_sql
from models.country import Country

def save(country):
    sql = "INSERT INTO countries(name, visited) VALUES ( %s, %s ) RETURNING id"
    values = [country.name, country.visited]
    results = run_sql( sql, values )
    country.id = results[0]['id']
    return country