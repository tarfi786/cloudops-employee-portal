from flask import render_template, request, redirect, url_for, session
from models import db, Employee
from s3_config import s3, AWS_BUCKET_NAME
import uuid


def register_routes(app):

    # ---------------- HOME ROUTE (FIXED 404 ISSUE) ----------------
    @app.route("/")
    def home():
        # If user not logged in, send to login page
        if "user" not in session:
            return redirect(url_for("login"))

        return render_template("dashboard.html")

    # ---------------- ADD EMPLOYEE ----------------
    @app.route("/add-employee", methods=["GET", "POST"])
    def add_employee():

        if "user" not in session:
            return redirect(url_for("login"))

        if request.method == "POST":

            file = request.files.get("profile_pic")
            image_url = None

            # Upload image only if file exists
            if file and file.filename != "":

                filename = str(uuid.uuid4()) + "_" + file.filename

                s3.upload_fileobj(
                    file,
                    AWS_BUCKET_NAME,
                    filename,
                    ExtraArgs={"ACL": "public-read"}
                )

                image_url = f"https://{AWS_BUCKET_NAME}.s3.amazonaws.com/{filename}"

            emp = Employee(
                full_name=request.form["full_name"],
                email=request.form["email"],
                phone=request.form.get("phone"),
                department=request.form["department"],
                role=request.form["role"],
                salary=request.form.get("salary"),
                profile_pic=image_url
            )

            db.session.add(emp)
            db.session.commit()

            return redirect(url_for("employees"))

        return render_template("add_employee.html")

    # ---------------- EMPLOYEES LIST ----------------
    @app.route("/employees")
    def employees():

        if "user" not in session:
            return redirect(url_for("login"))

        all_employees = Employee.query.all()
        return render_template("employees.html", employees=all_employees)

    # ---------------- LOGIN ROUTE (BASIC SAFE CHECK) ----------------
    @app.route("/login", methods=["GET", "POST"])
    def login():

        if request.method == "POST":
            session["user"] = request.form["username"]
            return redirect(url_for("home"))

        return render_template("login.html")

    # ---------------- LOGOUT ----------------
    @app.route("/logout")
    def logout():
        session.pop("user", None)
        return redirect(url_for("login"))
