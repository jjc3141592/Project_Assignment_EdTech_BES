# -*- coding: utf-8 -*-
"""
Created on Mon Jun 24 21:11:17 2024

@author: jjc31

"""

import tkinter as tk
from tkinter import simpledialog
from tabulate import tabulate
from EdTech_BES import SLTechBackend
from learner import Learner
from instructor import Instructor
from course import Course
from enrollment import Enrollment
from db_helper import DBHelper

class SLTechGUI:
    def __init__(self, backend):
        self.backend = backend
        self.root = tk.Tk()
        self.root.title("SL Tech Backend System")

    def add_user(self):
        user_id = simpledialog.askstring("Input", "Enter User ID:")
        email = simpledialog.askstring("Input", "Enter Email:")
        password = simpledialog.askstring("Input", "Enter Password:")
        user_type = simpledialog.askstring("Input", "Enter User Type (Learner/Instructor):")

        if user_type.lower() == 'learner':
            user = Learner(user_id, email, password)
        elif user_type.lower() == 'instructor':
            user = Instructor(user_id, email, password)
        else:
            tk.messagebox.showerror("Error", "Invalid User Type!")
            return

        self.backend.add_user(user)
        tk.messagebox.showinfo("Success", f"User {user_id} added successfully!")

    def add_course(self):
        course_id = simpledialog.askstring("Input", "Enter Course ID:")
        title = simpledialog.askstring("Input", "Enter Course Title:")
        self.db_helper.add_course(course_id, title)
        tk.messagebox.showinfo("Success", f"Course {course_id} added successfully!")

    def enroll_learner(self):
        enrollment_id = simpledialog.askstring("Input", "Enter Enrollment ID:")
        learner_id = simpledialog.askstring("Input", "Enter Learner ID:")
        course_id = simpledialog.askstring("Input", "Enter Course ID:")

        if learner_id in self.backend.users and course_id in self.backend.courses:
            learner = self.backend.users[learner_id]
            course = self.backend.courses[course_id]
            enrollment = Enrollment(enrollment_id, learner, course)
            self.backend.enroll_learner(enrollment)
            tk.messagebox.showinfo("Success", f"Learner {learner_id} enrolled in Course {course_id}!")
        else:
            tk.messagebox.showerror("Error", "Invalid Learner ID or Course ID!")

    def run(self):
        add_user_btn = tk.Button(self.root, text="Add User", command=self.add_user)
        add_course_btn = tk.Button(self.root, text="Add Course", command=self.add_course)
        enroll_learner_btn = tk.Button(self.root, text="Enroll Learner", command=self.enroll_learner)

        add_user_btn.pack(pady=10)
        add_course_btn.pack(pady=10)
        enroll_learner_btn.pack(pady=10)

        self.root.mainloop()

# Initialize backend and GUI
if __name__ == "__main__":
    backend = SLTechBackend()
    db_helper = DBHelper()
    #backend = populate_data(backend)  # Populate with test data
    gui = SLTechGUI(backend, db_helper)
    gui.run()
