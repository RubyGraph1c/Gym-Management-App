from db.run_sql import run_sql
from models.session import Session
from models.member import Member
from models.booking import Booking 
import repos.member_repo as member_repo
import repos.session_repo as session_repo
import repos.booking_repo as booking_repo

# CREATE/SAVE SESSION
def save(session):
    sql = "INSERT INTO sessions(name, day, time, id) VALUES ( %s, %s, %s,  ) RETURNING id"
    values = [session.name, session.day, session.time, session.id]
    results = run_sql( sql, values )
    session.id = results[0]['id']
    return session

# SELECT ALL SESSIONS 
def select_all():
    sessions = []

    sql = "SELECT * FROM sessions"
    results = run_sql(sql)

    for row in results:
        session = session(row['name'], row['day'], row['time'], row['id'])
        sessions.append(session)
    return sessions

# SELECT SPECIFIC SESSION 
def select(id):
    session = None
    sql = "SELECT * FROM sessions WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]

    if result is not None:
        session = session(result['name'], result['day'], result['time'], result['id'])
    return session

# DELETE ALL SESSIONS 
def delete_all():
    sql = "DELETE FROM sessions"
    run_sql(sql)
    
# DELETE INDIVIDUAL SESSION
def delete(id):
    sql = "DELETE FROM members WHERE id = %s"
    values = [id]
    run_sql(sql, values)


def members(session):
    members = []
    sql = "SELECT members.* FROM members INNER JOIN visits ON visits.member_id = members.id WHERE session_id = %s"
    values = [session.id]
    results = run_sql(sql, values)
    
    for row in results: 
        member = member(row['name'], row['id'])
        members.append(member)
    return members