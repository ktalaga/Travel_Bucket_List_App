from flask import Flask, render_template, request, redirect
from flask import Blueprint

from models.sight import Sight
from models.city import City

import repositories.sight_repository as sight_repository
import repositories.city_repository as city_repository

sights_blueprint = Blueprint("sights", __name__)

@sights_blueprint.route("/sights")
def sights():
    sights = sight_repository.select_all()
    return render_template("sights/index.html", sights = sights)


@sights_blueprint.route("/sights/notvisited")
def not_visited():
    sights = sight_repository.select_all()
    return render_template("sights/not_visited.html", sights = sights)

@sights_blueprint.route("/sights/visited")
def visited():
    sights = sight_repository.select_all()
    return render_template("sights/visited.html", sights = sights)

@sights_blueprint.route("/sights/<id>/visited", methods=['POST'])
def mark_visited(id):
    sight_repository.mark_visited(id)
    return redirect("/sights/notvisited")

@sights_blueprint.route("/sights/<id>")
def show(id):
    sight = sight_repository.select(id)
    return render_template("/sights/show.html", sight = sight)


@sights_blueprint.route("/sights/<id>/delete", methods=['POST'])
def delete_sight(id):
    sight_repository.delete(id)
    return redirect('/sights')


@sights_blueprint.route("/addsight")
def addsight():
    cities = city_repository.select_all()
    return render_template("sights/addsight.html", cities = cities)


@sights_blueprint.route("/addsight", methods=["POST"])
def newsight():
    name = request.form["sight"]
    visited = request.form["visited"]
    city_id = request.form["city_id"]
    city = city_repository.select(city_id)
    sight = Sight(name, city, visited)
    sight_repository.save(sight)
    return redirect("/sights")

@sights_blueprint.route("/sights/<id>/edit")
def edit(id):
    sight = sight_repository.select(id)
    cities = city_repository.select_all()
    return render_template("/sights/edit.html", sight = sight, cities = cities)


@sights_blueprint.route("/sights/<id>", methods=["POST"])
def update(id):
    name = request.form["sight"]
    city_id = request.form["city_id"]
    visited = request.form["visited"]
    city = city_repository.select(city_id)
    sight = Sight(name, city, visited, id)
    sight_repository.update(sight)
    return redirect(f"/sights/{id}")