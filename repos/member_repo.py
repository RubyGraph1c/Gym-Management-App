from db.run_sql import run_sql
from models.session import Session
from models.member import Member
from models.booking import Booking 
import repos.member_repo as member_repo
import repos.session_repo as session_repo
import repos.booking_repo as booking_repo

# SAVE/CREATE MEMBER
def save(member):
    sql = "INSERT INTO members( name ) VALUES ( %s ) RETURNING id"
    values = [member.name]
    results = run_sql( sql, values )
    member.id = results[0]['id']
    return member

# SHOW ALL MEMBERS

def select_all():
    members = []

    sql = "SELECT * FROM members"
    results = run_sql(sql)
    for row in results:
        member = member(row['name'], row['id'])
        members.append(member)
    return members

# SELECT INDIVIDUAL MEMBER
def select(id):
    member = None
    sql = "SELECT * FROM members WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]

    if result is not None:
        member = member(result['name'], result['id'] )
    return member

#DELETE ALL MEMBERS

def delete_all():
    sql = "DELETE FROM members"
    run_sql(sql)
    
# DELETE INDIVIDUAL MEMBER
def delete(id):
    sql = "DELETE FROM members WHERE id = %s"
    values = [id]
    run_sql(sql, values)


def sessions(member):
    sessions = []
    sql = "SELECT sessions.* FROM sessions INNER JOIN bookings ON bookings.session_id = sessions.id WHERE member_id = %s"
    values = [member.id]
    results = run_sql(sql, values)
    for row in results:
        session = session(row['name'], row['category'], row['day'], row['time'], row['id'])
        sessions.append(session)
    return sessions