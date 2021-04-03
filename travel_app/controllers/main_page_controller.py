from flask import Flask, render_template, request, redirect
from flask import Blueprint

from models.country import Country
import repositories.country_repository as country_repository

from models.city import City
import repositories.city_repository as city_repository

from models.sight import Sight
import repositories.sight_repository as sight_repository

main_page_blueprint = Blueprint("main_page", __name__)



@main_page_blueprint.route("/")
def main_page():
    countries = country_repository.select_all()
    cities = city_repository.select_all()
    sights = sight_repository.select_all()
    return render_template("index.html", countries = countries, cities = cities, sights = sights)