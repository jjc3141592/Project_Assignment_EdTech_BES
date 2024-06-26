# -*- coding: utf-8 -*-
"""
Created on Mon Jun 24 21:07:25 2024

@author: Jason Crook MySoftDev LLC.

"""

from user import User

class Instructor(User):
    """
    
    Builds the user class upon which of the user types are based.
    
    Implements 2 methods: add_course and remove_course
    
    """
    def __init__(self, user_id, email, password):
        super().__init__(user_id, email, password)
        self.courses_taught = []

    def add_course(self, course):
        if course not in self.courses_taught:
            self.courses_taught.append(course)

    def remove_course(self, course):
        if course in self.courses_taught:
            self.courses_taught.remove(course)
