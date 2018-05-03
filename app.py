from flask import Flask, render_template, flash
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

    if route.is_redirect():
        return redirect(url_for(route_name))
    else:
        route_arg = route.get_args()
        if (route_arg == None):
            return render_template(route_name)
        return render_template(route_name, **(route_arg))

def present_flash(f):
    if (not (f == None)):
        flash(f.get_msg(), f.get_msg_type().value)

def render_view(view):
    present_flash(view.get_flash())
    return create_template(view.get_route())

# Index
@app.route('/')
def index():
    return render_template(presenter.index())

@app.route('/review')
def review():
    return render_view(presenter.review())

if __name__ == '__main__':
	app.run(host = '0.0.0.0', port=8000)
