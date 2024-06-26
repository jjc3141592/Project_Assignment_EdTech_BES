'''
Course End Project: EdTech Backend System
@author: Jason Crook MySoftDev LLC.
This file: Incorporates classes to support backend system

'''

from db_helper import DBHelper
from tabulate import tabulate

class SLTechBackend:
    """
    
    Uses a custom database helper class to run methods to update records in 
    the sqlite database
    
    Implements 7 methods: add_user, add_course, enroll_learner, get_users,
        get_courses, get_enrollments, and generate_report
    
    """
    
    def __init__(self):
        self.db_helper = DBHelper()

    def add_user(self, user):
        user_type = 'learner' if isinstance(user, Learner) else 'instructor'
        self.db_helper.add_user(user.user_id, user.email, user.password, user_type)

    def add_course(self, course):
        self.db_helper.add_course(course.course_id, course.title)

    def enroll_learner(self, enrollment):
        self.db_helper.enroll_learner(enrollment.enrollment_id, 
                                      enrollment.learner.user_id, 
                                      enrollment.course.course_id)
        
    def update_password(self, user_id, new_password):
        self.db_helper.update_password(user_id, new_password)

    def validate_credentials(self, email, password):
        return self.db_helper.validate_credentials(email, password)

    def get_users(self):
        return self.db_helper.get_users()

    def get_courses(self):
        return self.db_helper.get_courses()

    def get_enrollments(self):
        return self.db_helper.get_enrollments()
    
    def update_email(self, user_id, new_email):
        self.db_helper.update_email(user_id, new_email)


    def generate_report(self):
        users = self.get_users()
        courses = self.get_courses()
        enrollments = self.get_enrollments()
        
        users_table = tabulate(users, headers=["User ID", "Email", "Password", "User Type"], tablefmt="grid")
        courses_table = tabulate(courses, headers=["Course ID", "Title"], tablefmt="grid")
        enrollments_table = tabulate(enrollments, headers=["Enrollment ID", "Learner ID", "Course ID"], tablefmt="grid")
        
        return users_table, courses_table, enrollments_table
