from flask import Flask
from flask.ext.mongoengine import MongoEngine

app = Flask(__name__)
app.config["MONGODB_SETTINGS"] = {"DB": "dating"}
app.config["SECRET_KEY"] = "KeepThisS3cr3t"

db = MongoEngine(app)

def register_blueprints(app):
    # Prevents circular imports
    from dating.views import dating
    app.register_blueprint(dating)

register_blueprints(app)

if __name__ == '__main__':
    app.run(port=3000)
