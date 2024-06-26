# -*- coding: utf-8 -*-
"""
Created on Mon Jun 24 21:08:04 2024

@author: Jason Crook MySoftDev LLC.

"""

class Course:
    """

    Implements 3 methods: add_learner, remove_learner and list_learners
    
    #Obsolete see db_helper class
    
    """
    def __init__(self, course_id, title):
        self.course_id = course_id
        self.title = title
        self.learners = []

# these methods were re-written in the db_helper class as CRUD database operations
    def add_learner(self, learner):
        if learner not in self.learners:
            self.learners.append(learner)
# obsolete see above
    def remove_learner(self, learner):
        if learner in self.learners:
            self.learners.remove(learner)
# obsolete see above
    def list_learners(self):
        return self.learners
