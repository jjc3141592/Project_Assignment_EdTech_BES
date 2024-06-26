# -*- coding: utf-8 -*-
"""
Created on Mon Jun 24 21:08:29 2024

@author: Jason Crook MySoftDev LLC.

"""

class Enrollment:
    """

    Implements 2 methods: enroll and drop
    
    #Obsolete see db_helper class
    
    """
# these methods were re-written in the db_helper class as CRUD database operations
    def __init__(self, enrollment_id, learner, course):
        self.enrollment_id = enrollment_id
        self.learner = learner
        self.course = course

    def enroll(self):
        self.course.add_learner(self.learner)
        self.learner.enroll_course(self.course)

    def drop(self):
        self.course.remove_learner(self.learner)
        self.learner.drop_course(self.course)
