from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.booking import Booking
import repos.booking_repo as booking_repo
import repos.member_repo as member_repo
import repos.session_repo as session_repo

members_blueprint = Blueprint("members", __name__)

@members_blueprint.route("/members")
def members():
    members = member_repo.select_all()
    return render_template("members/members_list.html", members = members)

@members_blueprint.route("/members/<id>")
def show(id):
    member = member_repo.select(id)
    sessions = member_repo.sessions(member)
    return render_template("members/show.html", member=member, sessions = sessions)

@members_blueprint.route("/members/<id>/delete", methods = ['GET'])
def delete_member(id):
    member_repo.delete(id)
    return redirect('/members/members_list.html')
