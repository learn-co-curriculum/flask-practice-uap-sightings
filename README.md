# UAP Sightings API Flask App

<img src="./assets/uapid.png" width="200" height="200" alt="UAPID logo"/>

## Objective

Since the government is now officially acknowledging the existence of Unexplained Arial Phenomena (UFOs), it is creating a portal for citizens to report sightings of UAPs, and you have been hired to set up the backend.  You will create a simple Flask app for the Unexplained Arial Phenomena Investigation Division (UAPID) to their specifications using your knowledge of the request-response cycle, GET HTTP requests, status codes, Flask, SQLAlchemy, dynamic routes, and request hooks.

## Deliverables

### Part 1: Set up the Flask App
1. Initialize a new Flask app in the `app.py` file.
2. Create a route for the home page (`/`) that returns a welcome message in JSON format.  Use the `@app.route` decorator and the `make_response` function from the flask module. The welcome message should be a string that says "The UAPID welcome our new extraterrestrial overlords!" and response should include a status code of 200.

### Part 2: Create a Database
1. Configure the app to use a SQLite database.
2. Create an instance of the SQLAlchemy class in `models.py` and import it into `app.py`.
3. Initialize Flask-Migrate with the app and the database instance.
4. Initialize the database with the app.
5. Create a model called "Sighting" in `models.py` with the following columns:
    - id (Integer, primary key, autoincrement)
    - date (String)
    - time (String)
    - location (String)
    - shape_of_craft (String)
    - approximate_size (Integer)
    - approximate_speed (Integer)
    - description (String)
    - reporter (String)
    - reporter_reliable_witness (Boolean)
- 5b. Optional: add a `__repr__` method to the Sighting model that returns a string representation of the model instance.
6. Make the Sighting model inherit SerializerMixin.
7. Create a migration and upgrade the database.
8. Create at least 3 seed sightings in `seeds.py` and run the seeds file to populate the sightings table.

### Part 3: Create a Route to Get All Sightings
1. Create a route (`/sightings`) that returns all sightings in the database in JSON format.
2. Use the `@app.route` decorator and the `make_response` function from the flask module.
3. Use the Sighting model to query the database for all sightings.
4. Create a list of dictionaries from the query results using the `to_dict` method from the SerializerMixin class in a list comprehension.
5. Return the list of dictionaries as a response in JSON format with a status code of 200.

### Part 4: Create a Route to Get a Single Sighting
1. Create a route (`/sightings/<int:id>`) that returns a single sighting by its id in JSON format.
2. Use the `@app.route` decorator and the `make_response` function from the flask module.
3. Use the Sighting model to query the database for a single sighting by its id.
4. Return the sighting (converted to a dictionary) as a response in JSON format with a status code of 200.

### Part 5: Create a Route to Get Sightings by Location
1. Create a route (`/sightings/location/<string:location>`) that returns all sightings in the database by location in JSON format.
2. Use the `@app.route` decorator and the `make_response` function from the flask module.
3. Use the Sighting model to query the database for all sightings by location.
4. Create a list of dictionaries from the query results using the `to_dict` method from the SerializerMixin class in a list comprehension.
5. Return the list of dictionaries as a response in JSON format with a status code of 200.

### Stretch Goals

#### `before_request` Hook
Use the` @app.before_request` decorator to create a function that logs the total number of sightings in the database to the console before each request. The log should be in the format "Total sightings: <number>".

#### BONUS: Create a Route to Get Siggtings by Location and Date
Create a route that returns all sightings in the database by location and date in JSON format. The route will be in the format `/sightings/location/<string:location>/date/<string:date>`.
