from flask import Flask, render_template, request, redirect
from flask import Blueprint

from models.country import Country

import repositories.country_repository as country_repository

countries_blueprint = Blueprint("countries", __name__)

@countries_blueprint.route("/countries")
def countries():
    countries = country_repository.select_all()
    return render_template("countries/index.html", countries = countries)

@countries_blueprint.route("/addcountry")
def addcountry():
    return render_template("countries/addcountry.html")


@countries_blueprint.route("/countries", methods=["POST"])
def newccountry():
    name = request.form["country"]
    visited = request.form["visited"]
    country = Country(name, visited)
    country_repository.save(country)
    return redirect("/countries")


@countries_blueprint.route("/countries/<id>/edit")
def edit(id):
    country = country_repository.select(id)
    return render_template("/countries/edit.html", country = country)
