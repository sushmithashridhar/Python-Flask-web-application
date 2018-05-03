from flask import Flask, render_template, session
import flask, flask.views
app = Flask(__name__)

class Review(flask.views.MethodView):
    @app.context_processor
    def template_context():
        '''Return a dictionary of key-value pairs,
           which will be available to all views in the context'''
        if 'username' in session:
            username = session['username']
        else:
            username = 'Peter'

        return {'version':88, 'username':username}

    @app.route('/')
    def main():
        return render_template('review.html')

    if __name__ == '__main__':
        app.run(debug=True)