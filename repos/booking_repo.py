from db.run_sql import run_sql
from models.session import Session
from models.member import Member
from models.booking import Booking 
import repos.member_repo as member_repo
import repos.session_repo as session_repo
import repos.booking_repo as booking_repo

# CREATE/SAVE BOOKING
# def save(booking):
#     sql = "INSERT INTO bookings (member_id, session_id, confirmation) VALUES (%s, %s, %s) RETURNING id"
#     values = [booking.member.id, booking.session.id, booking.confirmation]
#     results = run_sql( sql, values )
#     booking.id = results[0]['id']
#     return booking

# SHOW ALL BOOKINGS
def select_all():
    bookings = []

    sql = "SELECT * FROM bookings"
    results = run_sql(sql)

    for row in results:
        member = member_repo.select(row['member_id'])
        session = session_repo.select(row['session_id'])
        booking = booking(member, session, row['confirmation'], row['id'])
        bookings.append(booking)
    return bookings

# DELETE ALL BOOKINGS 

def delete_all():
    sql = "DELETE FROM bookings"
    run_sql(sql)

# DELETE INDIVIDUAL BOOKING
# def delete(id):
#     sql = "DELETE FROM bookings WHERE id = %s"
#     values = [id]
#     run_sql(sql, values)