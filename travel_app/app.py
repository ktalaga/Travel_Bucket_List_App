from flask import Flask, render_template

from controllers.country_controller import countries_blueprint
from controllers.city_controller import cities_blueprint
from controllers.sight_controller import sights_blueprint
from controllers.main_page_controller import main_page_blueprint


from models.country import Country
import repositories.country_repository as country_repository

from models.city import City
import repositories.city_repository as city_repository

app = Flask(__name__)

app.register_blueprint(countries_blueprint)
app.register_blueprint(cities_blueprint)
app.register_blueprint(sights_blueprint)
app.register_blueprint(main_page_blueprint)



if __name__ == '__main__':
    app.run(debug=True)