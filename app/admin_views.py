from app import app # import "app" folder import "app.py" file
from flask import render_template

@app.route("/admin/dashboard")
def admin_dashboard():
    return render_template("admin/dashboard.html")