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

@cities_blueprint.route("/cities/<id>/notvisited", methods=['POST'])
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


@cities_blueprint.route("/addcity", methods=["POST"])
def newcity():
    name = request.form["city"]
    visited = request.form["visited"]
    country_id = request.form["country_id"]
    country = country_repository.select(country_id)
    city = City(name, country, visited)
    city_repository.save(city)
    return redirect("/cities")

@cities_blueprint.route("/cities/<id>/edit")
def edit(id):
    city = city_repository.select(id)
    countries = country_repository.select_all()
    return render_template("/cities/edit.html", city = city, countries = countries)


@cities_blueprint.route("/cities/<id>", methods=["POST"])
def update(id):
    name = request.form["city"]
    country_id = request.form["country_id"]
    visited = request.form["visited"]
    country = country_repository.select(country_id)
    city = City(name, country, visited, id)
    city_repository.update(city)
    return redirect(f"/cities/{id}")

@cities_blueprint.route("/cities/<id>/visited", methods=['POST'])
def mark_notvisited(id):
        city_repository.mark_notvisited(id)
        return redirect("/cities/visited")