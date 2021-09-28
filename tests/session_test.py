import unittest
from models.member import Member
from models.session import Session
from models.booking import Booking 

class TestSession(unittest.TestCase):
    
    def setUp(self):
        self.session = Session("Dance", "Monday", "9AM")
    
    def test_session_has_name(self):
        self.assertEqual("Dance", self.session.name)
        
    def test_session_has_day(self):
        self.assertEqual("Monday", self.session.day)
        
    def test_session_has_time(self):
        self.assertEqual("9AM", self.session.time)