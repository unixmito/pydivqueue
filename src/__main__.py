""""
    File: __main__.py
    Description:
        Starts flask application
"""

import flask

# Initialize app context
app = flask.Flask(__name__)

@app.route('/')
def index():
    return """

        Test
    """

if __name__ == "__main__":
    app.run(debug=True)

