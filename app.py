from flask import Flask
from solutions import solutions
from view import view

app = Flask(__name__)
app.register_blueprint(solutions)
app.register_blueprint(view)

if __name__ == "__main__":
    app.run()
    # did i commit the wrong crap?