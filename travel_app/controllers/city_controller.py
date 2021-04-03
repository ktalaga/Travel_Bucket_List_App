from flask import Flask, render_template, request, redirect
from flask import Blueprint

from models.city import City

import repositories.city_repository as city_repository

cities_blueprint = Blueprint("cities", __name__)

@cities_blueprint.route("/cities")
def cities():
    cities = city_repository.select_all()
    return render_template("cities/index.html", cities = cities)


@cities_blueprint.route("/cities/notvisited")
def not_visited():
    cities = city_repository.select_all()
    return render_template("cities/not_visited.html", cities = cities)

@cities_blueprint.route("/cities/visited")
def visited():
    cities = city_repository.select_all()
    return render_template("cities/visited.html", cities = cities)

@cities_blueprint.route("/cities/<id>/visited", methods=['POST'])
def mark_visited(id):
    city_repository.mark_visited(id)
    return redirect("/cities/notvisited")


