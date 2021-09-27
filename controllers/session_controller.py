from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.booking import Booking
import repos.booking_repo as booking_repo
import repos.member_repo as member_repo
import repos.session_repo as session_repo

sessions_blueprint = Blueprint("sessions", __name__)

@sessions_blueprint.route("/sessions")
def sessions():
    sessions = session_repo.select_all()
    return render_template("sessions/index.html", sessions = sessions)

@sessions_blueprint.route("/sessions/<id>")
def show(id):
    session = session_repo.select(id)
    members = session_repo.members(session)
    return render_template("sessions/show.html", session=session, members = members)