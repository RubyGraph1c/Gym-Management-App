from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.booking import Booking
from models.member import Member
import repos.booking_repo as booking_repo
import repos.member_repo as member_repo
import repos.session_repo as session_repo

members_blueprint = Blueprint("members", __name__)

# List all members
@members_blueprint.route("/members")
def members():
    members = member_repo.select_all()
    return render_template("members/members_list.html", members = members)

#create new member
@members_blueprint.route("/members/create", methods = ['GET'])
def new_member():
    members = member_repo.select_all()
    return render_template("members/create.html", members = members)

# NEW
@members_blueprint.route("/members/create", methods = ['POST'])
def create_member():
    name = request.form['name']
    member = Member(name)
    member_repo.save(member)
    return redirect ("/members")

#show MEMBER (by id)

@members_blueprint.route("/members/<id>")
def show(id):
    member = member_repo.select(id)
    sessions = member_repo.sessions(member)
    return render_template("members/show.html", member=member, sessions = sessions)


#delete member by id - NO NOT CHANGE - FULLY FUNCTIONAL
@members_blueprint.route("/members/<id>/delete", methods = ['GET'])
def delete_member(id):
    member_repo.delete(id)
    return redirect('/members')
