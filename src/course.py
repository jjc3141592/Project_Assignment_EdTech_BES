# -*- coding: utf-8 -*-
"""
Created on Mon Jun 24 21:08:04 2024

@author: Jason Crook MySoftDev LLC.

"""

class Course:
    def __init__(self, course_id, title):
        self.course_id = course_id
        self.title = title
        self.learners = []

    def add_learner(self, learner):
        if learner not in self.learners:
            self.learners.append(learner)

    def remove_learner(self, learner):
        if learner in self.learners:
            self.learners.remove(learner)

    def list_learners(self):
        return self.learners
