import unittest
from models.member import Member
from models.session import Session

class TestMember(unittest.TestCase):
    
    def setUp(self):
        self.member = Member("Sheldon Cooper")
    
    def test_member_has_name(self):
        self.assertEqual("Sheldon Cooper", self.member.name)
    
    # Test member can be created 
    
    # Test member can be edited 
    # Test one member be deleted
    # Test all members can be deleted 
    # Test member can join specific session    
    # Test member can create booking 

    # def test_member_can_reduce_cash(self):
    #     self.member.reduce_cash(500)
    #     self.assertEqual(500, self.member.cash)

    # def test_pets_start_at_0(self):
    #     self.assertEqual(0, self.member.pet_count())

    # def test_can_add_pet(self):
    #     self.member.add_pet(self.pet)
    #     self.assertEqual(1, self.member.pet_count())

    # def test_can_get_total_pet_cost(self):
    #     self.member.add_pet(self.pet)
    #     self.member.add_pet(self.pet)
    #     self.member.add_pet(self.pet)

    #     self.assertEqual(1500, self.member.get_total_value_of_pets())