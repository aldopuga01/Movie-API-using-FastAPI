This is a simple RESTful API created with FastAPI that allows users to perform CRUD (Create, Read, Update, Delete) operations on a movie database. The API is protected with JWT-based authentication and includes endpoints for user login and registration.

The API uses an SQLite database to store movie information, including movie name, release year, and genre. The API allows users to retrieve all movies, as well as individual movies by ID. Users can also add, update, and delete movies from the database.

The API is created with Python 3.9 and uses the FastAPI web framework, SQLAlchemy as ORM to interact with the database, and PyJWT to handle user authentication. The API is deployed locally and can be accessed at http://localhost:8000.

This API was created as part of a backend web development course, and it is intended as a learning exercise.