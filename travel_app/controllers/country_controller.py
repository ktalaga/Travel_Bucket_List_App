from flask import Flask, render_template, request, redirect
from flask import Blueprint

from models.country import Country

import repositories.country_repository as country_repository
import repositories.city_repository as city_repository
import repositories.sight_repository as sight_repository

countries_blueprint = Blueprint("countries", __name__)


@countries_blueprint.route("/countries/notvisited")
def not_visited():
    countries = country_repository.select_all()
    return render_template("countries/not_visited.html", countries = countries)

@countries_blueprint.route("/countries/visited")
def visited():
    countries = country_repository.select_all()
    return render_template("countries/visited.html", countries = countries)


@countries_blueprint.route("/addcountry")
def addcountry():
    return render_template("countries/addcountry.html")


@countries_blueprint.route("/addcountry", methods=["POST"])
def newccountry():
    new_name = request.form["country"]
    picture_url = request.form["picture_url"]
    visited = request.form["visited"]
    country = Country(new_name, picture_url, visited)
    countries = country_repository.select_all()
    names = [country.name for country in countries]
    if new_name not in names:
        country_repository.save(country)
    else:
        return render_template("/exception.html")
    if country.visited == "True":
        return redirect("/countries/visited")
    elif country.visited == "False":
        return redirect("/countries/notvisited")


@countries_blueprint.route("/countries/<id>")
def show(id):
    country = country_repository.select(id)
    cities = city_repository.select_all()
    sights = sight_repository.select_all()
    return render_template("/countries/show.html", country = country, cities = cities, sights = sights)


@countries_blueprint.route("/countries/<id>/edit")
def edit(id):
    country = country_repository.select(id)
    return render_template("/countries/edit.html", country = country)


@countries_blueprint.route("/countries/<id>", methods=["POST"])
def update(id):
    new_name = request.form["country"]
    picture_url = request.form["picture_url"]
    visited = request.form["visited"]
    country = Country(new_name, picture_url, visited, id)
    

    countries = country_repository.select_all()
    names = [country.name for country in countries]
    if new_name not in names:
        country_repository.update(country)
    else:
        return render_template("/exception.html")
    if country.visited == "True":
        return redirect("/countries/visited")
    elif country.visited == "False":
        return redirect("/countries/notvisited")



@countries_blueprint.route("/countries/<id>/delete", methods=['POST'])
def delete_country(id):
    country_repository.delete(id)
    return redirect('/')


@countries_blueprint.route("/countries/<id>/notvisited", methods=['POST'])
def mark_visited(id):
        country_repository.mark_visited(id)
        return redirect("/countries/notvisited")


@countries_blueprint.route("/countries/<id>/visited", methods=['POST'])
def mark_notvisited(id):
        country_repository.mark_notvisited(id)
        return redirect("/countries/visited")


@countries_blueprint.route("/search/bycountry")
def bycountry():
    countries = country_repository.select_all()
    return render_template("countries/search_by_country.html", countries = countries)

@countries_blueprint.route("/bycountry", methods=['POST'])
def search_by_country():
    print(request.form)
    id = request.form["country_id"]
    country_repository.select(id)
    return redirect(f"/countries/{id}")
