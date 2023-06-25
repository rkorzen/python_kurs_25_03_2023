from flask import Flask, jsonify, render_template
from sqlalchemy import create_engine
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import sessionmaker

# Create Flask app
app = Flask(__name__)

engine = create_engine('sqlite:///db.sqlite3')

Session = sessionmaker(bind=engine)
session = Session()

Base = automap_base()
Base.prepare(engine)

Course = Base.classes.courses_course

@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/courses', methods=['GET'])
def get_courses():

    courses = session.query(Course).all()
    courses_list = [
        {
            'title': row.title,
            'description': row.description,
            'start_data': str(row.start_data),
        } for row in courses
    ]

    return jsonify(courses_list)
    # return render_template('kursy.html', courses=courses_list)


if __name__ == '__main__':
    app.run()