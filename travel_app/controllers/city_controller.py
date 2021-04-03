from flask import Flask, render_template, request, redirect
from flask import Blueprint

from models.city import City
from models.country import Country

import repositories.city_repository as city_repository
import repositories.country_repository as country_repository

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

@cities_blueprint.route("/cities/<id>")
def show(id):
    city = city_repository.select(id)
    return render_template("/cities/show.html", city = city)


@cities_blueprint.route("/cities/<id>/delete", methods=['POST'])
def delete_city(id):
    city_repository.delete(id)
    return redirect('/cities')

@cities_blueprint.route("/addcity")
def addcity():
    countries = country_repository.select_all()
    return render_template("cities/addcity.html", countries = countries)