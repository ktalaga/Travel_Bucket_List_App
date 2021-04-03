from flask import Flask, render_template, request, redirect
from flask import Blueprint

from models.city import City

import repositories.city_repository as city_repository

cities_blueprint = Blueprint("cities", __name__)

@cities_blueprint.route("/cities")
def cities():
    cities = city_repository.select_all()
    return render_template("cities/index.html", cities = cities)

@cities_blueprint.route("/addcity")
def addcity():
    return render_template("cities/addcity.html")

@cities_blueprint.route("/cities/visited")
def cities_visited():
    cities = city_repository.select_all()
    return render_template("/cities/visited.html", cities=cities)

@cities_blueprint.route("/cities/notvisited")
def cities_notvisited():
    cities = city_repository.select_all()
    return render_template("/cities/notvisited.html", cities=cities)

