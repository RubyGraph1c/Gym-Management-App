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

# save NEW member
@members_blueprint.route("/members/create", methods = ['POST'])
def create_member():
    name = request.form['name']
    # Pop up not essential - not accepting empty string is:
    if name == '':
        return redirect ("/members/create")
    member = Member(name)
    member_repo.save(member)
    return redirect ("/members")


#show MEMBER (by id)

@members_blueprint.route("/members/<id>")
def show(id):
    member = member_repo.select(id)
    return render_template("members/show.html", member = member)

#EDIT member

@members_blueprint.route("/members/<id>/edit")
def edit_member(id):
    member = member_repo.select(id)
    return render_template('members/show.html', member = member)

#UPDATE member
@members_blueprint.route("/members/<id>", methods=["POST"])
def update_member(id):
    name = request.form["name"]
    if name == '':
        return redirect ("/members/" + id + "/edit")
    member = Member(name, id)
    member_repo.update(member)
    return redirect("/members")

#delete member by id - NO NOT CHANGE - FULLY FUNCTIONAL
@members_blueprint.route("/members/<id>/delete", methods = ['GET'])
def delete_member(id):
    member_repo.delete(id)
    return redirect('/members')

# Book member onto specific session

@members_blueprint.route("/members/<member_id>/book")
def bookings(member_id):
    sessions = session_repo.select_all()
    return render_template ('/members/session.html', member_id = member_id, sessions = sessions)

@members_blueprint.route("/members/<member_id>/book/save", methods = ['POST'])
def book_member_to_session(member_id):
    session_id = request.form["session_id"]
    member_repo.book(member_id, session_id)
    return redirect ('/members')


