Travel_Bucket_List_App - The app was designed and created by Konrad Talaga as part of the immersive Professional Software Development Course at Codeclan. This is the first full stack app I've ever created having learned coding for just 4 weeks. 
--------------------------------------------------------------------------------------------------------------------------------------------------------------------
The Project Brief:

Travel Bucket List

Build an app to track someone's travel adventures.

MVP:

The app should allow the user to track countries and cities they want to visit and those they have visited.
The user should be able to create and edit countries
Each country should have one or more cities to visit
The user should be able to create and delete entries for cities
The app should allow the user to mark destinations as visited or still to see
Possible Extensions:

Have separate pages for destinations visited and those still to visit
Add sights to the destination cities
Search for destination by continent, city or country
Any other ideas you might come up with
--------------------------------------------------------------------------------------------------------------------------------------------------------------------
Rules:

The project must be built using only:

HTML / CSS
Python
Flask
PostgreSQL and the psycopg
--------------------------------------------------------------------------------------------------------------------------------------------------------------------
To run the app:

1. Save the app locally
2. Open up the travel_app directory in Visual Studio Code
3. Set up travel_app as a working directory
4. You will ideally need 3 terminal windows open
5. In Terminal 1, run the following commands:
        5.1 createdb travel_app
        5.2 psql -d travel_app -f db/travel_app.sql;
6. In Terminal 2:
        6.1 python3 console.py
7. In Terminal 3:
        7.1 flask run
8. Open http://localhost:5000/ in google chrome

You should now see Travel Bucket List App main page in your browser. Enjoy! 
Please keep in mind Terminal 3 (the one running flask app) must stay open when the app is being used.
--------------------------------------------------------------------------------------------------------------------------------------------------------------------
Key features:

- View visited countries and countries on the bucket list
- Show visited cities and cities on the bucket list
- Display visited sights and sights on the bucket list
- User can add, edit and delete countries, cities, and sights
- Visited destinatons can be marked as unvisited and moved to the bucket list
- Destinations on the bucket list can be marked as visited
- User can search for destinations by country
- Pictures of the destinations are stored in DB as URL links. To add destination, pass url link of the photo you want to use into the add/edit form

Additional features:

- When adding destinations, if destination exists, the app will not duplicate the record. The same feature is prestent when editing destinations
- When country is deleted, cities and sights existing in the country are deleted as well
