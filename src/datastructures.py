
"""
update this file to implement the following already declared methods:
- add_member: Should add a member to the self._members list
- delete_member: Should delete a member from the self._members list
- update_member: Should update a member from the self._members list
- get_member: Should return a member from the self._members list
"""
from random import randint

class FamilyStructure:
    def __init__(self, last_name):
        self.last_name = last_name
        # example list of members
        self._members = [
            {"id":"1",
            "first_name":"John",
            "age":33,
            "lucky_numbers":[7, 13, 22]},
            {"id":"2",
            "first_name":"Jane",
            "age":35,
            "lucky_numbers":[10, 14, 3]},
            {"id":"3",
            "first_name":"Jimmy",
            "age":5,
            "lucky_numbers":[1]}
        ]

    # read-only: Use this method to generate random members ID's when adding members into the list
    def _generateId(self):
        return len(self._members) + 1

    def add_member(self, member):
        if not member.get("id"):
            member["id"] = str(self._generateId()) 
        self._members.append(member)
        return member

    def delete_member(self, id):
        for i, member in enumerate(self._members):
            
            if member["id"] == id: #if member["id"] == str(id):
                print("Deleting member", member)
                del self._members[i]
                return {'done': True}
        print("Member not deleted")
        return {'done': False} 

    def get_member(self, id):
        print("id: ",id)
        for member in self._members:
            print("memberID: ",member["id"], "id: ",id, member["id"] == (id))
            if member["id"] == id: #if member["id"] == str(id):
                return {
                    'name':member['first_name'],
                    'id': member['id'],
                    'age': member['age'],
                    'lucky_numbers': member['lucky_numbers']
                }
        print("Member not found")
        return {'message': "Member not found"}

    # this method is done, it returns a list with all the family members
    def get_all_members(self):
        return self._members
