import os
from sqlalchemy import create_engine
from sqlalchemy.orm.session import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

sqlite_file = './database.sqlite'    # name of the sqlite database file
base_dir = os.path.dirname(os.path.dirname(__file__)) # Directory of the Module

# Define the full path to your database
database_url = 'sqlite:///' + os.path.join(base_dir, sqlite_file)

engine = create_engine(database_url, echo=True) # Create the database

# Create session to connect to the database
Session = sessionmaker(bind=engine)

# Create a base class for the models
Base = declarative_base()