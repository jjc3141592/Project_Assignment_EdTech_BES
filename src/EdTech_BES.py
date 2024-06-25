'''
Course End Project: EdTech Backend System
By: Jason Crook MySoftDev LLC.
This file: Incorporates classes to support backend system
'''

class User:
    def __init__(self, user_id, email, password):
        self.user_id = user_id
        self.email = email
        self.password = password
        
    def update_email(self, new_email):
        self.email = new_email
        
    def update_password(self, new_password):
        self.password = new_password
        
    def validate_credentials(self, email, password):
        return self.email == email and self.password == password
    
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

class Instructor(User):
    def __init__(self, user_id, email, password):
        super().__init__(user_id, email, password)
        self.courses_taught = []

    def add_course(self, course):
        if course not in self.courses_taught:
            self.courses_taught.append(course)

    def remove_course(self, course):
        if course in self.courses_taught:
            self.courses_taught.remove(course)

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

class Enrollment:
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
