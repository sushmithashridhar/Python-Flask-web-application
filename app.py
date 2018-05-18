"""
A simple reviews flask app.
Data is stored in a SQLite database that looks something like the following:

+--------------+-------------+----------------------+------------+---------+-------+
| termoffered | yearoffered | yearoftheweekoffered | instructor | review | rating |
+-------------+-------------+----------------------+------------+---------+-------+
| Fall       |      2017   | Monday               | XYZ        |  Good  | 10     |
+------------+------------------+------------+----------------+

This can be created with the following SQL (see bottom of this file):

    create table reviews (termoffered text, yearoffered text, timeoftheweekoffered text, instructor text, review text, rating text;

"""

from flask import Flask, render_template, flash, request
from main import Main
from review import Review
from model import AppModel
from view_header import Route
from presenter import Presenter

app = Flask(__name__)
model = AppModel()
presenter = Presenter(model)


def create_template(route):
    route_name = route.get_name()

    route_arg = route.get_args()
    if (route_arg == None):
        return render_template(route_name)
    return render_template(route_name, **(route_arg))
"""
This is a create_template function.

:param route: Specifies the route the html url containes.
:returns: returns the route.
"""


def render_view(view):
    return create_template(view.get_route())
"""
This is a render_view function.

:param view: View for route.
:returns: returns the view for the route.
"""

@app.route('/')
def index():
    return render_template(presenter.index())
"""
This is a index function.

:param: No parameter passed.
:returns: returns the url from index function from presenter.
"""

@app.route('/review')
def review():
    return render_view(presenter.review())
"""
This is a review function.

:param: No parameter passed.
:returns: returns the url from review function from presenter.
"""

@app.route('/insert', methods = ['GET', 'POST'])
def insert():
    requestmethod = request.method == 'POST'
    return render_template(presenter.insert(requestmethod, request.form))
"""
This is a insert function.

:param: No parameter passed.
:returns: returns the url after inserting data to the database.
"""

if __name__ == '__main__':
    app.run(host = '0.0.0.0', port=8000)
