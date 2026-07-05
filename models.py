from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Employee(db.Model):
    id = db.Column(db.Integer, primary_key=True)

    full_name = db.Column(db.String(120), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    phone = db.Column(db.String(20))

    department = db.Column(db.String(50))
    role = db.Column(db.String(80))

    salary = db.Column(db.Integer)

    # NEW FIELD 👉 profile image URL (S3 link)
    profile_pic = db.Column(db.String(255))

    def __repr__(self):
        return f"<Employee {self.full_name}>"
