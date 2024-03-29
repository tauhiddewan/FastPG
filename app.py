from sqlalchemy.orm import sessionmaker

from models import User, engine

Session = sessionmaker(bind=engine)

session = Session()


# *CREATE
user1 = User(name="Amit", age=25)
user2 = User(name="Mobin", age=27)
user3 = User(name="Santu", age=28)
user4 = User(name="Morgan", age=40)

# ? the following lines actually save the data to the database
# session.add(user1)
# session.add_all([user2, user3, user4])
# session.commit() 


# *READ
# users = session.query(User).all()
user = session.query(User).filter_by(id=4).one_or_none()
print(f"User ID : {user.id}, Name: {user.name}, Age: {user.age}")

# *UPDATE
user.age = 35
print(f"Updated User ID : {user.id}, Name: {user.name}, Age: {user.age}")
# session.commit() 

# *DELETE
session.delete(user)
# session.commit()