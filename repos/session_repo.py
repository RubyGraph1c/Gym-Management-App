from db.run_sql import run_sql
from models.session import Session


# CREATE/SAVE SESSION
def save(session):
    sql = "INSERT INTO sessions(name, day, time) VALUES ( %s, %s, %s) RETURNING id"
    values = [session.name, session.day, session.time]
    run_sql( sql, values )


# SELECT ALL SESSIONS 
def select_all():
    sessions = []

    sql = "SELECT * FROM sessions ORDER BY \
        CASE\
            WHEN Day = 'Monday' THEN 1\
            WHEN Day = 'Tuesday' THEN 2\
            WHEN Day = 'Wednesday' THEN 3\
            WHEN Day = 'Thursday' THEN 4\
            WHEN Day = 'Friday' THEN 5\
            WHEN Day = 'Saturday' THEN 6\
            WHEN Day = 'Sunday' THEN 7\
        END"
    results = run_sql(sql)

    for row in results:
        session = Session(row['name'], row['day'], row['time'], row['id'])
        sessions.append(session)
    return sessions


# SELECT SPECIFIC SESSION 
def select(id):
    session = None
    sql = "SELECT * FROM sessions WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)

    if result is not None:
        session = Session(result[0]['name'], result[0]['day'], result[0]['time'], result[0]['id'])
    return session


# DELETE ALL SESSIONS 
def delete_all():
    sql = "DELETE FROM sessions"
    run_sql(sql)
    
    
# DELETE INDIVIDUAL SESSION
def delete(id):
    sql = "DELETE FROM sessions WHERE id = %s"
    values = [id]
    run_sql(sql, values)
    
    
# UPDATE SESSION
def update(session):
    sql = "UPDATE sessions SET name = %s, day = %s, time = %s WHERE id = %s"
    values = [session.name, session.day, session.time, session.id]
    run_sql(sql, values)