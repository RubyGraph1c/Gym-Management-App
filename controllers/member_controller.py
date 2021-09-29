from flask import render_template, request, redirect
from flask import Blueprint
from models.member import Member
import repos.member_repo as member_repo
import repos.session_repo as session_repo

members_blueprint = Blueprint("members", __name__)

# SELECT ALL MEMBERS
@members_blueprint.route("/members")
def members():
    members = member_repo.select_all()
    return render_template("members/members_list.html", members = members)

# CREATE NEW MEMBERS
@members_blueprint.route("/members/create", methods = ['GET'])
def new_member():
    members = member_repo.select_all()
    return render_template("members/create.html", members = members)

# SAVE NEW MEMBER
@members_blueprint.route("/members/create", methods = ['POST'])
def create_member():
    name = request.form['name']
    # Ideally, here I would have a pop up to inform user of invalid input when attempting to input an empty string
    if name == '':
        return redirect ("/members/create")
    member = Member(name)
    member_repo.save(member)
    return redirect ("/members")


# SELECT MEMBER BY ID
@members_blueprint.route("/members/<id>")
def show(id):
    member = member_repo.select(id)
    return render_template("members/show.html", member = member)

# EDIT EXISTING MEMBER
@members_blueprint.route("/members/<id>/edit")
def edit_member(id):
    member = member_repo.select(id)
    return render_template('members/show.html', member = member)

# SAVE EXISTING MEMBER UPDATE
@members_blueprint.route("/members/<id>", methods=["POST"])
def update_member(id):
    name = request.form["name"]
    if name == '':
        return redirect ("/members/" + id + "/edit")
    member = Member(name, id)
    member_repo.update(member)
    return redirect("/members")

# DELETE MEMBER BY ID
@members_blueprint.route("/members/<id>/delete", methods = ['GET'])
def delete_member(id):
    member_repo.delete(id)
    return redirect('/members')

# CREATE BOOKING (SELECT SESSION TO BOOK SPECIFIC MEMBER TO)
@members_blueprint.route("/members/<member_id>/book")
def bookings(member_id):
    sessions = session_repo.select_all()
    return render_template ('/members/session.html', member_id = member_id, sessions = sessions)

# SAVE BOOKING (SAVE MEMBER TO SPECIFIC SESSION)
@members_blueprint.route("/members/<member_id>/book/save", methods = ['POST'])
def book_member_to_session(member_id):
    session_id = request.form["session_id"]
    member_repo.book(member_id, session_id)
    return redirect ('/members')


