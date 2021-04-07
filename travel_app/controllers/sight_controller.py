from flask import Flask, render_template, request, redirect
from flask import Blueprint

from models.sight import Sight
from models.city import City

import repositories.sight_repository as sight_repository
import repositories.city_repository as city_repository

sights_blueprint = Blueprint("sights", __name__)


@sights_blueprint.route("/sights/notvisited")
def not_visited():
    sights = sight_repository.select_all()
    return render_template("sights/not_visited.html", sights = sights)

@sights_blueprint.route("/sights/visited")
def visited():
    sights = sight_repository.select_all()
    return render_template("sights/visited.html", sights = sights)

@sights_blueprint.route("/sights/<id>/notvisited", methods=['POST'])
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
    return redirect('/')


@sights_blueprint.route("/addsight")
def addsight():
    cities = city_repository.select_all()
    return render_template("sights/addsight.html", cities = cities)


@sights_blueprint.route("/addsight", methods=["POST"])
def newsight():
    new_name = request.form["sight"]
    picture_url = request.form["picture_url"]
    visited = request.form["visited"]
    city_id = request.form["city_id"]
    city = city_repository.select(city_id)
    sight = Sight(new_name, picture_url, city, visited)
    sights = sight_repository.select_all()
    names = [sight.name for sight in sights]
    if new_name not in names:
        sight_repository.save(sight)
    else:
        return render_template("/exception.html")
    if sight.visited == "True":
        return redirect("/sights/visited")
    elif sight.visited == "False":
        return redirect("/sights/notvisited")

@sights_blueprint.route("/sights/<id>/edit")
def edit(id):
    sight = sight_repository.select(id)
    cities = city_repository.select_all()
    return render_template("/sights/edit.html", sight = sight, cities = cities)


@sights_blueprint.route("/sights/<id>", methods=["POST"])
def update(id):
    name = request.form["sight"]
    picture_url = request.form["picture_url"]
    city_id = request.form["city_id"]
    visited = request.form["visited"]
    city = city_repository.select(city_id)
    sight = Sight(name, picture_url, city, visited, id)
    sight_repository.update(sight)
    return redirect(f"/sights/{id}")


@sights_blueprint.route("/sights/<id>/visited", methods=['POST'])
def mark_notvisited(id):
        sight_repository.mark_notvisited(id)
        return redirect("/sights/visited")