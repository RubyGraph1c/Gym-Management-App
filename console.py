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

member1 = Member('Lucinda Shale')
member_repo.save(member1)

member2 = Member('Murray Grant')
member_repo.save(member2)

member3 = Member('Dominique Haig')
member_repo.save(member3)

# session1 = Session('Body Pump', 'Weight-lifting')
# session_repo.save(session1)

# session2 = Session('Body Balance', 'Yoga/Pilates')
# session_repo.save(session2)

# booking1 = Booking(member1, session1)


pdb.set_trace()

print(member_repo.select_all()[0].id)
print(member_repo.sessions(member1))
# print(session_repo.members(session2))





