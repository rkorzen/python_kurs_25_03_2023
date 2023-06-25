from datetime import datetime, timedelta

from sqlalchemy import create_engine, inspect
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///db.sqlite3')

inspector = inspect(engine)

Base = automap_base()
Base.prepare(engine, reflect=True)

# for table_name in inspector.get_table_names():
#     table = Base.classes.get(table_name)
#     if table:
#         print("Nazwa tabeli:", table_name)
#         print("Nazwy kolumn:")
#         for column in inspector.get_columns(table_name):
#             print(column['name'])
#         print("-------------")

Course = Base.classes.courses_course

Session = sessionmaker(bind=engine)
session = Session()

courses = session.query(Course).all()

for course in courses:
    print(course.title, course.start_data)

one_month_ago = datetime.now() - timedelta(days=30)

courses = session.query(Course).filter(Course.start_data > one_month_ago).all()

for course in courses:
    print("x", course.title)