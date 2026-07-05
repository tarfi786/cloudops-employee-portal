from flask import Flask
from models import db
from routes import register_routes

app = Flask(__name__)

# SQLite database (FREE, no AWS cost)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///cloudops.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.secret_key = "cloudops-secret-key"

db.init_app(app)

register_routes(app)

with app.app_context():
    db.create_all()

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)
