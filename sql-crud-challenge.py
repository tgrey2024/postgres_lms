from sqlalchemy import (
    create_engine, Column, Integer, String
)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


# executing the instructions from the "chinook" database
db = create_engine("postgresql:///chinook")
base = declarative_base()

# create a class-based model for the "Place" table
class Place(base):
    __tablename__ = "Place"
    id = Column(Integer, primary_key=True)
    place_name = Column(String)
    city = Column(String)
    country = Column(String)
    visitors_per_year = Column(Integer)

# instead of connecting to the database directly, we will ask for a session
# create a new instance of sessionmaker, then point to our engine (the db)
Session = sessionmaker(db)
# opens an actual session by calling the Session() subclass defined above
session = Session()

# creating the database using declarative_base subclass
base.metadata.create_all(db)

# creating records on the Place table
eiffel_tower = Place(
    place_name = "Eiffel Tower",
    city = "Paris",
    country = "France",
    visitors_per_year = 7000000
)

taipei101 = Place(
    place_name = "Taipei 101",
    city = "Taipei",
    country = "Taiwan",
    visitors_per_year = 1418775
)

statue_of_liberty = Place(
    place_name = "Statue of Liberty",
    city = "New York",
    country = "USA",
    visitors_per_year = 4440000
)

buckingham_palace = Place(
    place_name = "Buckingham Palace",
    city = "London",
    country = "UK",
    visitors_per_year = 50000
)

sydney_opera_house = Place(
    place_name = "Sydney Opera House",
    city = "Sydney",
    country = "Australia",
    visitors_per_year = 10900000
)


# Create:
# # add each instance of our programmers to our session
# session.add(eiffel_tower)
session.add(taipei101)
# session.add(statue_of_liberty)
# session.add(buckingham_palace)
# session.add(sydney_opera_house)

# Read:
# query the database to find all Places
# places = session.query(Place)
# for place in places:
#     print(
#         place.id,
#         place.place_name,
#         place.city,
#         place.country,
#         place.visitors_per_year,
#         sep=" | "
#     )
session.commit()    
# Update:
# updating a single record
# programmer = session.query(Programmer).filter_by(id=7).first()
# programmer.famous_for = "Computing World President"

# session.commit()

# updating a single record
# place = session.query(Place).filter_by(id=7).first()
# place.visitors_per_year = 1420000
# session.commit()
# # query the database to find all Places
# places = session.query(Place)
# for place in places:
#     print(
#         place.id,
#         place.place_name,
#         place.city,
#         place.country,
#         place.visitors_per_year,
#         sep=" | "
#     )
# session.commit()    

# Delete:
# deleting a single record
# pname = input("Enter a place name: ")
# place = session.query(Place).filter_by(place_name=pname).first()
# # defensive programming
# if place is not None:
#     print("Place found: ", place.place_name)
#     confirmation = input("Are you sure you want to delete this record (y/n)?")
#     if confirmation.lower() == "y":
#         session.delete(place)
#         session.commit()
#         print("Place has been deleted")
#     else:
#         print("No records found")
# query the database to find all Places
places = session.query(Place)
for place in places:
    print(
        place.id,
        place.place_name,
        place.city,
        place.country,
        place.visitors_per_year,
        sep=" | "
    )
session.commit()   
# programmer = session.query(Programmer).filter_by(first_name=fname, last_name=lname).first()
# # defensive programming
# if programmer is not None:
#     print("Programmer found: ", programmer.first_name, " ", programmer.last_name)
#     confirmation = input("Are you sure you want to delete this record (y/n)?")
#     if confirmation.lower() == "y":
#         session.delete(programmer)
#         session.commit()
#         print("Programmer has been deleted")
# else:
#     print("No records found")

# query the database to find all Programmers
# programmers = session.query(Programmer)
# for programmer in programmers:
#     print(
#         programmer.id,
#         programmer.first_name + " " + programmer.last_name,
#         programmer.gender,
#         programmer.nationality,
#         programmer.famous_for,
#         sep=" | "
#     )
