from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.booking import Booking
from models.session import Session
import repos.booking_repo as booking_repo
import repos.session_repo as session_repo
import repos.session_repo as session_repo

sessions_blueprint = Blueprint("sessions", __name__)

# List all sessions
@sessions_blueprint.route("/sessions")
def sessions():
    sessions = session_repo.select_all()
    return render_template("sessions/index.html", sessions = sessions)

#create new session
@sessions_blueprint.route("/sessions/create", methods = ['GET'])
def new_session():
    sessions = session_repo.select_all()
    return render_template("sessions/create.html", sessions = sessions)

# NEW session
@sessions_blueprint.route("/sessions/create", methods = ['POST'])
def create_session():
    name = request.form['name']
    session = Session(name)
    session_repo.save(session)
    return redirect ("/sessions")

#show session (by id)

@sessions_blueprint.route("/sessions/<id>")
def show(id):
    session = session_repo.select(id)
    sessions = session_repo.sessions(session)
    return render_template("sessions/show.html", session = session, sessions = sessions)

#EDIT session

@sessions_blueprint.route("/sessions/<id>/edit")
def edit_session(id):
    session = session_repo.select(id)
    return render_template('sessions/show.html', session = session)

#UPDATE session
@sessions_blueprint.route("/sessions/<id>", methods=["POST"])
def update_session(id):
    name = request.form(["name"]["day"]["time"])
    session = Session(name, day, time, id)   # BUG!
    session_repo.update(session)
    return redirect("/sessions")

#delete session by id - NO NOT CHANGE - FULLY FUNCTIONAL
@sessions_blueprint.route("/sessions/<id>/delete", methods = ['GET'])
def delete_session(id):
    session_repo.delete(id)
    return redirect('/sessions')