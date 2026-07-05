from flask import render_template, request, redirect, url_for, session
from models import db, Employee


def register_routes(app):

    # ---------------- LOGIN ----------------
    @app.route("/", methods=["GET", "POST"])
    def login():

        if request.method == "POST":
            username = request.form["username"]
            password = request.form["password"]

            # SIMPLE LOGIN (for project only)
            if username == "admin" and password == "admin123":
                session["user"] = username
                return redirect(url_for("dashboard"))

            return "Invalid Credentials"

        return render_template("login.html")


    # ---------------- LOGOUT ----------------
    @app.route("/logout")
    def logout():
        session.pop("user", None)
        return redirect(url_for("login"))


    # ---------------- DASHBOARD ----------------
    @app.route("/dashboard")
    def dashboard():
        if "user" not in session:
            return redirect(url_for("login"))
        return render_template("dashboard.html")


    # ---------------- EMPLOYEES ----------------
    @app.route("/employees")
    def employees():
        if "user" not in session:
            return redirect(url_for("login"))

        employees = Employee.query.all()
        return render_template("employees.html", employees=employees)


    # ---------------- ADD EMPLOYEE ----------------
    @app.route("/add-employee", methods=["GET", "POST"])
    def add_employee():
        if "user" not in session:
            return redirect(url_for("login"))

        if request.method == "POST":

            emp = Employee(
                full_name=request.form["full_name"],
                email=request.form["email"],
                phone=request.form.get("phone"),
                department=request.form["department"],
                role=request.form["role"],
                salary=request.form.get("salary")
            )

            db.session.add(emp)
            db.session.commit()

            return redirect(url_for("employees"))

        return render_template("add_employee.html")


    # ---------------- EDIT EMPLOYEE ----------------
    @app.route("/edit-employee/<int:id>", methods=["GET", "POST"])
    def edit_employee(id):

        if "user" not in session:
            return redirect(url_for("login"))

        emp = Employee.query.get_or_404(id)

        if request.method == "POST":
            emp.full_name = request.form["full_name"]
            emp.email = request.form["email"]
            emp.phone = request.form.get("phone")
            emp.department = request.form["department"]
            emp.role = request.form["role"]
            emp.salary = request.form.get("salary")

            db.session.commit()
            return redirect(url_for("employees"))

        return render_template("edit_employee.html", emp=emp)


    # ---------------- DELETE EMPLOYEE ----------------
    @app.route("/delete-employee/<int:id>")
    def delete_employee(id):

        if "user" not in session:
            return redirect(url_for("login"))

        emp = Employee.query.get_or_404(id)

        db.session.delete(emp)
        db.session.commit()

        return redirect(url_for("employees"))
