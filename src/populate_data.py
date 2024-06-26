# -*- coding: utf-8 -*-
"""
Created on Mon Jun 24 22:23:05 2024

@author: Jason Crook MySoftDev LLC

"""

from backend import SLTechBackend
from learner import Learner #depreciated
from instructor import Instructor #depreciated
from course import Course #depreciated
from enrollment import Enrollment #depreciated
from db_helper import DBHelper

def populate_data(backend):
    db_helper = DBHelper()

    # Add users
    db_helper.add_user("L001", "learner1@example.com", "password123", "learner")
    db_helper.add_user("L002", "learner2@example.com", "password456", "learner")
    db_helper.add_user("L003", "learner3@example.com", "password955", "learner")
    db_helper.add_user("L004", "learner4@example.com", "password458", "learner")
    db_helper.add_user("L005", "learner5@example.com", "password658", "learner")
    
    db_helper.add_user("I001", "instructor1@example.com", "password789", "instructor")

    # Add courses
    db_helper.add_course("C001", "Python Programming")
    db_helper.add_course("C002", "Data Science")
    db_helper.add_course("M101", "Math 101")
    db_helper.add_course("M102", "Math 102")
    db_helper.add_course("E101", "English 101")
    db_helper.add_course("E102", "English 102")

    # Enroll learners
    db_helper.enroll_learner("E001", "L001", "C001")
    db_helper.enroll_learner("E002", "L001", "C002")
    db_helper.enroll_learner("E003", "L002", "C002")

    return backend

if __name__ == "__main__":
    backend = SLTechBackend()
    backend = populate_data(backend)
    print("Data populated successfully!")
