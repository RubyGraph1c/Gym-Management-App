from flask import render_template, request, redirect
from flask import Blueprint
from models.session import Session
import repos.session_repo as session_repo
import repos.member_repo as member_repo

sessions_blueprint = Blueprint("sessions", __name__)

# SELECT ALL SESSIONS
@sessions_blueprint.route("/sessions")
def sessions():
    sessions = session_repo.select_all()
    return render_template("sessions/index.html", sessions=sessions)


# SELECT SESSION BY ID
@sessions_blueprint.route("/sessions/<id>")
def show(id):
    session = session_repo.select(id)
    sessions = session_repo.sessions(session)
    return render_template("sessions/show.html", session=session, sessions=sessions)


# CREATE NEW SESSION
@sessions_blueprint.route("/sessions/create", methods=["GET"])
def new_session():
    return render_template("sessions/create.html")


# SAVE NEW SESSION
@sessions_blueprint.route("/sessions/create/new", methods=["POST"])
def create_session():
    name = request.form["name"]
    if name == "":
        return redirect("/sessions/create")
    day = request.form["day"]
    time = request.form["time"]
    session = Session(name, day, time)
    session_repo.save(session)
    return redirect("/sessions")


# EDIT EXISTING SESSION
@sessions_blueprint.route("/sessions/<id>/edit")
def edit_session(id):
    session = session_repo.select(id)
    return render_template("sessions/show.html", session=session)


# SAVE EXISTING SESSION UPDATE
@sessions_blueprint.route("/sessions/<id>", methods=["POST"])
def update_session(id):
    name = request.form["name"]
    if name == "":
        return redirect("/sessions/" + id + "/edit")
    day = request.form["day"]
    time = request.form["time"]
    session = Session(name, day, time, id)
    session_repo.update(session)
    return redirect("/sessions")


# DELETE SESSION BY ID
@sessions_blueprint.route("/sessions/<id>/delete", methods=["GET"])
def delete_session(id):
    session_repo.delete(id)
    return redirect("/sessions")


# SHOW ALL MEMBERS BOOKED TO SPECIFIC SESSION 
@sessions_blueprint.route("/sessions/<id>/bookings")
def show_members_booked(id):
    members = member_repo.get_members_booked(id)
    return render_template("/sessions/bookings.html", members=members)
