# -*- coding: utf-8 -*-
"""
Created on Mon Jun 24 21:11:17 2024

@author: Jason Crook MySoftDev LLC.

"""
import tkinter as tk
from tkinter import messagebox, scrolledtext
from backend import SLTechBackend
from populate_data import populate_data
from custom_dialog import CustomDialogs

class SLTechGUI:
    def __init__(self, backend):
        self.backend = backend
        self.root = tk.Tk()
        self.root.title("SL Tech Backend System")
        self.root.geometry("800x600")
        self.create_widgets()

    def create_widgets(self):
        add_user_btn = tk.Button(self.root, text="Add User", command=self.add_user)
        add_course_btn = tk.Button(self.root, text="Add Course", command=self.add_course)
        enroll_learner_btn = tk.Button(self.root, text="Enroll Learner", command=self.enroll_learner)
        update_password_btn = tk.Button(self.root, text="Update Password", command=self.update_password)
        validate_credentials_btn = tk.Button(self.root, text="Validate Credentials", command=self.validate_credentials)
        generate_report_btn = tk.Button(self.root, text="Generate Report", command=self.generate_report)
        drop_course_btn = tk.Button(self.root, text="Drop Course", command=self.drop_course)
        update_email_btn = tk.Button(self.root, text="Update Email", command=self.update_email)
        
        add_user_btn.pack(pady=10)
        add_course_btn.pack(pady=10)
        drop_course_btn.pack(pady=10)        
        enroll_learner_btn.pack(pady=10)
        update_password_btn.pack(pady=10)
        validate_credentials_btn.pack(pady=10)
        generate_report_btn.pack(pady=10)
        update_email_btn.pack(pady=10)

    def add_user(self):
        result = CustomDialogs.add_user_dialog(self.root)
        if result:
            self.backend.db_helper.add_user(result['user_id'], result['email'], result['password'], result['user_type'])
            messagebox.showinfo("Success", f"User {result['user_id']} added successfully!")
        else:
            messagebox.showerror("Error", "User addition cancelled!")

    def add_course(self):
        result = CustomDialogs.add_course_dialog(self.root)
        if result:
            self.backend.db_helper.add_course(result['course_id'], result['title'])
            messagebox.showinfo("Success", f"Course {result['course_id']} added successfully!")
        else:
            messagebox.showerror("Error", "Course addition cancelled!")
    def drop_course(self):
        result = CustomDialogs.drop_course_dialog(self.root)
        if result:
            self.backend.db_helper.drop_course(result['learner_id'], result['course_id'])
            messagebox.showinfo("Success", f"Course {result['course_id']} dropped successfully!")
        else:
            messagebox.showerror("Error", "Course drop cancelled!")

    def enroll_learner(self):
        result = CustomDialogs.enroll_learner_dialog(self.root)
        if result:
            self.backend.db_helper.enroll_learner(result['enrollment_id'], result['learner_id'], result['course_id'])
            messagebox.showinfo("Success", f"Learner {result['learner_id']} enrolled in Course {result['course_id']} successfully!")
        else:
            messagebox.showerror("Error", "Enrollment cancelled!")

    def update_password(self):
        result = CustomDialogs.update_password_dialog(self.root)
        if result:
            self.backend.update_password(result['user_id'], result['new_password'])
            messagebox.showinfo("Success", f"Password for user {result['user_id']} updated successfully!")
        else:
            messagebox.showerror("Error", "Password update cancelled!")

    def validate_credentials(self):
        result = CustomDialogs.validate_credentials_dialog(self.root)
        if result:
            valid = self.backend.validate_credentials(result['email'], result['password'])
            if valid:
                messagebox.showinfo("Success", "Credentials are valid!")
            else:
                messagebox.showerror("Error", "Invalid credentials!")
                
    def update_email(self):  # New method for updating email
        result = CustomDialogs.update_email_dialog(self.root)
        if result:
            self.backend.update_email(result['user_id'], result['new_email'])
            messagebox.showinfo("Success", f"Email for user {result['user_id']} updated successfully!")
        else:
            messagebox.showerror("Error", "Email update cancelled!")                

    def generate_report(self):
        users_table, courses_table, enrollments_table = self.backend.generate_report()
        report_window = tk.Toplevel(self.root)
        report_window.title("Report")
        text_area = scrolledtext.ScrolledText(report_window, wrap=tk.WORD)
        text_area.pack(expand=True, fill=tk.BOTH)
        text_area.insert(tk.END, "Users:\n" + users_table + "\n\n")
        text_area.insert(tk.END, "Courses:\n" + courses_table + "\n\n")
        text_area.insert(tk.END, "Enrollments:\n" + enrollments_table + "\n")

    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    backend = SLTechBackend()
    #backend = populate_data(backend)
    gui = SLTechGUI(backend)
    gui.run()
