from flask_app import app
from flask import render_template, redirect, session ,request
from flask_app.models.user_model import user_model

@app.route("/")
def index():
    users_list = user_model.get_all()
    return render_template("index.html", data = users_list)

@app.route("/add_user")
def add_user():
    return render_template("create_user.html")

@app.route("/create_user", methods = ["post"])
def create_user():
    results = user_model.create_user(request.form)
    print(request.form)
    return redirect("/")

@app.route("/show_user_info/<int:id>")
def show_user(id):
    data = {"id":id}
    one_user = user_model.one_user_function(data)
    return render_template("one_user_page.html", data=one_user)

@app.route("/transit_edit_user_info/<int:id>")
def transit_edit_user(id):
    data = {"id":id}
    one_user = user_model.one_user_function(data)
    print(id)
    return render_template("edit_user.html", data=one_user)

@app.route("/edit_user_info", methods = ["post"])
def edit_user():
    edit_one_user = user_model.edit_user_info(request.form)
    print(request.form)
    return redirect("/")

@app.route("/delete_user/<int:id>")
def delete_user(id):
    data = {"id":id}
    delete_one_user = user_model.delete_user_info(data)
    return redirect("/")
    