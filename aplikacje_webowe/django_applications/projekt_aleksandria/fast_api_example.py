from fastapi import FastAPI

from sqlalchemy import create_engine
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import sessionmaker

# Create Flask app
app = FastAPI()

engine = create_engine('sqlite:///db.sqlite3')

Session = sessionmaker(bind=engine)
session = Session()

Base = automap_base()
Base.prepare(engine)

Course = Base.classes.courses_course



@app.get("/")
async def hello_world():
    return {"message": "Hello World"}



@app.get('/courses')
async def get_courses():

    courses = session.query(Course).all()
    courses_list = [
        {
            'title': row.title,
            'description': row.description,
            'start_data': str(row.start_data),
        } for row in courses
    ]

    return courses_list