from sqlalchemy.orm import sessionmaker

from models import User, engine

Session = sessionmaker(bind=engine)

session = Session()


# * Create
user1 = User(name="Amit", age=25)
user2 = User(name="Mobin", age=27)
user3 = User(name="Santu", age=28)
user4 = User(name="Morgan", age=40)

# ? the following lines actually save the data to the database
# session.add(user1)
# session.add_all([user2, user3, user4])
# session.commit() 


# * Read
users = session.query(User).all()
print(users)
for user in users:
    print(f"User ID : {user.id}, Name: {user.name}, Age: {user.age}")