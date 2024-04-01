# FastPG

The main goal of this repository is to learn about SQLAlchemy's Object Relational Mapper (ORM), which is used to link user-defined Python classes with database tables, synchronizing changes in object and row states.

**Declaration of Mapping:**

1. **Setting up Engine:** Use `create_engine()` to establish an engine object for database operations. It connects to the database and generates activity logs if `echo` is set to `True`. Example:
   ```python
   from sqlalchemy import create_engine
   engine = create_engine('sqlite:///sales.db', echo=True)
   ```

2. **Configurational Process:** Begin by describing database tables and defining classes to map to these tables. This is done using SQLAlchemy's Declarative system, where classes include directives to describe the corresponding database tables.
   - Create a base class using `declarative_base()` from `sqlalchemy.ext.declarative`.
   - Define mapped classes with `__tablename__` attribute and Column definitions.
   - Each mapped class must have a primary key column.
   Example:
   ```python
   from sqlalchemy import Column, Integer, String
   from sqlalchemy.ext.declarative import declarative_base

   Base = declarative_base()

   class Customers(Base):
       __tablename__ = 'customers'
       id = Column(Integer, primary_key=True)
       name = Column(String)
       address = Column(String)
       email = Column(String)
   ```

3. **Table Metadata and Creation:** The Declarative system generates table metadata, represented by Table objects. These objects are associated with classes via a Mapper object. Use `Base.metadata.create_all(engine)` to create tables in the database based on the defined classes.
   Example:
   ```python
   Base.metadata.create_all(engine)
   ```