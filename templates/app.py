from flask import Flask
from models import db
from routes import register_routes

app = Flask(__name__)

# Database
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///cloudops.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

# Secret key (for sessions/login)
app.secret_key = "cloudops-secret-key"

db.init_app(app)

register_routes(app)

with app.app_context():
    db.create_all()

if __name__ == "__main__":
    app.run(debug=True, port=5001)
