from db.run_sql import run_sql
from models.member import Member


# SAVE/CREATE MEMBER
def save(member):
    sql = "INSERT INTO members( name ) VALUES ( %s )"
    values = [member.name]
    run_sql(sql, values)
    
    
# SHOW ALL MEMBERS
def select_all():
    members = []

    sql = "SELECT * FROM members"
    results = run_sql(sql)
    for row in results:
        member = Member(row['name'], row['id'])
        members.append(member)
    return members


# SELECT INDIVIDUAL MEMBER
def select(id):
    member = None
    sql = "SELECT * FROM members WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)

    if result is not None and len(result) > 0:
        member = Member(result[0]['name'], result[0]['id'])
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


#UPDATE MEMBER
def update(member):
    sql = "UPDATE members SET name = %s WHERE id = %s"
    values = [member.name, member.id]
    run_sql(sql, values)


# BOOK MEMBER ONTO SPECIFIC SESSION
def book(member, session):
    sql = "INSERT INTO bookings( member_id, session_id ) VALUES ( %s, %s )"
    values = [member, session]
    run_sql(sql, values)
    
# GET MEMBERS BOOKED ONTO SPECIFIC SESSION
def get_members_booked(session_id):
    members = []
    sql = "SELECT members.* from members INNER JOIN bookings ON bookings.member_id = members.id WHERE bookings.session_id = %s;"
    values = [session_id]
    results = run_sql(sql, values)
    for row in results:
        member = Member(row['name'], row['id'])
        members.append(member)
    return members 

