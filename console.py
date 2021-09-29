import pdb
from models.session import Session
from models.member import Member
from models.booking import Booking

import repos.session_repo as session_repo
import repos.member_repo as member_repo
import repos.booking_repo as booking_repo

booking_repo.delete_all()
session_repo.delete_all()
member_repo.delete_all()

pdb.set_trace()

print(member_repo.select_all()[0].id)
print(member_repo.sessions(member1))
# print(session_repo.members(session2))





