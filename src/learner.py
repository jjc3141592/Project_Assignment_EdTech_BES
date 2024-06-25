# -*- coding: utf-8 -*-
"""
Created on Mon Jun 24 21:04:47 2024

@author: Jason Crook MySoftDev LLC

"""
from user import User

class Learner(User):
    def __init__(self, user_id, email, password):
        super().__init__(user_id, email, password)
        self.courses = []

    def enroll_course(self, course):
        if course not in self.courses:
            self.courses.append(course)

    def drop_course(self, course):
        if course in self.courses:
            self.courses.remove(course)
