from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.booking import Booking
import repos.booking_repo as booking_repo
import repos.member_repo as member_repo
import repos.session_repo as session_repo

bookings_blueprint = Blueprint("bookings", __name__)

@bookings_blueprint.route("/bookings")
def bookings():
    bookings = booking_repo.select_all()
    return render_template("bookings/index.html", bookings = bookings)

@bookings_blueprint.route("/bookings/new", methods=['GET'])
def new_task():
    members = member_repo.select_all()
    bookings = booking_repo.select_all()
    return render_template("bookings/new.html", members = members, bookings = bookings)

@bookings_blueprint.route("/bookings",  methods=['POST'])
def create_task():
    member_id = request.form['member_id']
    booking_id = request.form['booking_id']
    confirmation = request.form['confirmation']
    member = member_repo.select(member_id)
    booking = booking_repo.select(booking_id)
    booking = booking(member, booking, confirmation)
    booking_repo.save(booking)
    return redirect('/bookings')

@bookings_blueprint.route("/bookings/<id>/delete", methods=['POST'])
def delete_task(id):
    booking_repo.delete(id)
    return redirect('/bookings')