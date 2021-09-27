class Booking:

    def __init__(self, member_id, session_id, confirmation, id = None ):
        self.member_id = member_id
        self.session_id = session_id
        self.confirmation = confirmation
        self.id = id