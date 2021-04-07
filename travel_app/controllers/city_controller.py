from flask import Flask, render_template, request, redirect
from flask import Blueprint

from models.city import City
from models.country import Country

import repositories.city_repository as city_repository
import repositories.country_repository as country_repository

cities_blueprint = Blueprint("cities", __name__)


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
    city = city_repository.select(id)
    country_id = city.country.id
    country_repository.mark_visited(country_id)
    return redirect("/cities/notvisited")

@cities_blueprint.route("/cities/<id>")
def show(id):
    city = city_repository.select(id)
    return render_template("/cities/show.html", city = city)


@cities_blueprint.route("/cities/<id>/delete", methods=['POST'])
def delete_city(id):
    city_repository.delete(id)
    return redirect('/')


@cities_blueprint.route("/addcity")
def addcity():
    countries = country_repository.select_all()
    return render_template("cities/addcity.html", countries = countries)


@cities_blueprint.route("/addcity", methods=["POST"])
def newcity():
    new_name = request.form["city"]
    picture_url = request.form['picture_url']
    visited = request.form["visited"]
    country_id = request.form["country_id"]
    country = country_repository.select(country_id)
    city = City(new_name, picture_url, country, visited)
    cities = city_repository.select_all()
    names = [city.name for city in cities]
    if new_name not in names:
        city_repository.save(city)
    else:
        return render_template("/exception.html")
    if city.visited == "True":
        return redirect("/cities/visited")
    elif city.visited == "False":
        return redirect("/cities/notvisited")

@cities_blueprint.route("/cities/<id>/edit")
def edit(id):
    city = city_repository.select(id)
    countries = country_repository.select_all()
    return render_template("/cities/edit.html", city = city, countries = countries)


@cities_blueprint.route("/cities/<id>", methods=["POST"])
def update(id):
    new_name = request.form["city"]
    picture_url = request.form['picture_url']
    country_id = request.form["country_id"]
    visited = request.form["visited"]
    country = country_repository.select(country_id)
    city = City(new_name, picture_url, country, visited, id)
    cities = city_repository.select_all()
    names = [city.name for city in cities]
    if new_name not in names:
        city_repository.update(city)
    else:
        return render_template("/exception.html")
    if city.visited == "True":
        return redirect("/cities/visited")
    elif city.visited == "False":
        return redirect("/cities/notvisited")

@cities_blueprint.route("/cities/<id>/visited", methods=['POST'])
def mark_notvisited(id):
        city_repository.mark_notvisited(id)
        return redirect("/cities/visited")







