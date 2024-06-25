'''
Course End Project: EdTech Backend System
@author: Jason Crook MySoftDev LLC.
This file: Incorporates classes to support backend system

'''


    
from learner import Learner
from instructor import Instructor
from course import Course
from enrollment import Enrollment

class SLTechBackend:
    def __init__(self):
        self.users = {}
        self.courses = {}
        self.enrollments = {}

    def add_user(self, user):
        self.users[user.user_id] = user

    def add_course(self, course):
        self.courses[course.course_id] = course

    def enroll_learner(self, enrollment):
        enrollment.enroll()
        self.enrollments[enrollment.enrollment_id] = enrollment

    def drop_learner(self, enrollment):
        enrollment.drop()
        del self.enrollments[enrollment.enrollment_id]

    def get_enrolled_learners(self, course_id):
        if course_id in self.courses:
            return self.courses[course_id].list_learners()

    def get_enrolled_courses(self, learner_id):
        if learner_id in self.users and isinstance(self.users[learner_id], Learner):
            return self.users[learner_id].courses
