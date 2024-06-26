# -*- coding: utf-8 -*-
"""
Created on Tue Jun 25 13:16:39 2024

@author: Jason Crook MySoftDev lLC.

"""
import tkinter as tk
from tkinter import simpledialog, messagebox

class CustomDialogs:
    """
    A class containing static methods to create custom dialog boxes for the application.
    """
    
    @staticmethod
    def add_user_dialog(parent):
        """
        Create a custom dialog for adding a user.

        Parameters:
        parent (tk.Tk): The parent window.

        Returns:
        dict: A dictionary containing user_id, email, password, and user_type.
        """        
        dialog = tk.Toplevel(parent)
        dialog.title("Add User")
        dialog.resizable(True, True)

        instruction_label = tk.Label(dialog, text="Please fill out the form to add a new user.", wraplength=380)
        instruction_label.pack(padx=10, pady=10)

        user_id_label = tk.Label(dialog, text="User ID:")
        user_id_label.pack(padx=5, pady=5)
        user_id_entry = tk.Entry(dialog)
        user_id_entry.pack(padx=5, pady=5)

        email_label = tk.Label(dialog, text="Email:")
        email_label.pack(padx=5, pady=5)
        email_entry = tk.Entry(dialog)
        email_entry.pack(padx=5, pady=5)

        password_label = tk.Label(dialog, text="Password:")
        password_label.pack(padx=5, pady=5)
        password_entry = tk.Entry(dialog, show="*")
        password_entry.pack(padx=5, pady=5)

        user_type_label = tk.Label(dialog, text="User Type (Learner/Instructor):")
        user_type_label.pack(padx=5, pady=5)
        user_type_entry = tk.Entry(dialog)
        user_type_entry.pack(padx=5, pady=5)

        def on_ok():
            dialog.result = {
                "user_id": user_id_entry.get(),
                "email": email_entry.get(),
                "password": password_entry.get(),
                "user_type": user_type_entry.get()
            }
            dialog.destroy()

        def on_cancel():
            dialog.result = None
            dialog.destroy()

        button_frame = tk.Frame(dialog)
        button_frame.pack(padx=5, pady=5)

        ok_button = tk.Button(button_frame, text="OK", command=on_ok)
        ok_button.pack(side=tk.LEFT, padx=10, pady=10)
        cancel_button = tk.Button(button_frame, text="Cancel", command=on_cancel)
        cancel_button.pack(side=tk.RIGHT, padx=10, pady=10)

        dialog.update_idletasks()  # Update window size based on content
        parent.wait_window(dialog)
        return dialog.result

    @staticmethod
    def add_course_dialog(parent):
        dialog = tk.Toplevel(parent)
        dialog.title("Add Course")
        dialog.resizable(True, True)

        instruction_label = tk.Label(dialog, text="Please fill out the form to add a new course.", wraplength=380)
        instruction_label.pack(padx=10, pady=10)

        course_id_label = tk.Label(dialog, text="Course ID:")
        course_id_label.pack(padx=5, pady=5)
        course_id_entry = tk.Entry(dialog)
        course_id_entry.pack(padx=5, pady=5)

        title_label = tk.Label(dialog, text="Title:")
        title_label.pack(padx=5, pady=5)
        title_entry = tk.Entry(dialog)
        title_entry.pack(padx=5, pady=5)

        def on_ok():
            dialog.result = {
                "course_id": course_id_entry.get(),
                "title": title_entry.get()
            }
            dialog.destroy()

        def on_cancel():
            dialog.result = None
            dialog.destroy()

        button_frame = tk.Frame(dialog)
        button_frame.pack(padx=5, pady=5)

        ok_button = tk.Button(button_frame, text="OK", command=on_ok)
        ok_button.pack(side=tk.LEFT, padx=10, pady=10)
        cancel_button = tk.Button(button_frame, text="Cancel", command=on_cancel)
        cancel_button.pack(side=tk.RIGHT, padx=10, pady=10)

        dialog.update_idletasks()  # Update window size based on content
        parent.wait_window(dialog)
        return dialog.result

    @staticmethod
    def enroll_learner_dialog(parent):
        dialog = tk.Toplevel(parent)
        dialog.title("Enroll Learner")
        dialog.resizable(True, True)

        instruction_label = tk.Label(dialog, text="Please fill out the form to enroll a learner in a course.", wraplength=380)
        instruction_label.pack(padx=10, pady=10)

        enrollment_id_label = tk.Label(dialog, text="Enrollment ID:")
        enrollment_id_label.pack(padx=5, pady=5)
        enrollment_id_entry = tk.Entry(dialog)
        enrollment_id_entry.pack(padx=5, pady=5)

        learner_id_label = tk.Label(dialog, text="Learner ID:")
        learner_id_label.pack(padx=5, pady=5)
        learner_id_entry = tk.Entry(dialog)
        learner_id_entry.pack(padx=5, pady=5)

        course_id_label = tk.Label(dialog, text="Course ID:")
        course_id_label.pack(padx=5, pady=5)
        course_id_entry = tk.Entry(dialog)
        course_id_entry.pack(padx=5, pady=5)

        def on_ok():
            dialog.result = {
                "enrollment_id": enrollment_id_entry.get(),
                "learner_id": learner_id_entry.get(),
                "course_id": course_id_entry.get()
            }
            dialog.destroy()

        def on_cancel():
            dialog.result = None
            dialog.destroy()

        button_frame = tk.Frame(dialog)
        button_frame.pack(padx=5, pady=5)

        ok_button = tk.Button(button_frame, text="OK", command=on_ok)
        ok_button.pack(side=tk.LEFT, padx=10, pady=10)
        cancel_button = tk.Button(button_frame, text="Cancel", command=on_cancel)
        cancel_button.pack(side=tk.RIGHT, padx=10, pady=10)

        dialog.update_idletasks()  # Update window size based on content
        parent.wait_window(dialog)
        return dialog.result

    @staticmethod
    def update_password_dialog(parent):
        dialog = tk.Toplevel(parent)
        dialog.title("Update Password")
        dialog.resizable(True, True)

        instruction_label = tk.Label(dialog, text="Please fill out the form to update the password.", wraplength=380)
        instruction_label.pack(padx=10, pady=10)

        user_id_label = tk.Label(dialog, text="User ID:")
        user_id_label.pack(padx=5, pady=5)
        user_id_entry = tk.Entry(dialog)
        user_id_entry.pack(padx=5, pady=5)

        new_password_label = tk.Label(dialog, text="New Password:")
        new_password_label.pack(padx=5, pady=5)
        new_password_entry = tk.Entry(dialog, show="*")
        new_password_entry.pack(padx=5, pady=5)

        def on_ok():
            dialog.result = {
                "user_id": user_id_entry.get(),
                "new_password": new_password_entry.get()
            }
            dialog.destroy()

        def on_cancel():
            dialog.result = None
            dialog.destroy()

        button_frame = tk.Frame(dialog)
        button_frame.pack(padx=5, pady=5)

        ok_button = tk.Button(button_frame, text="OK", command=on_ok)
        ok_button.pack(side=tk.LEFT, padx=10, pady=10)
        cancel_button = tk.Button(button_frame, text="Cancel", command=on_cancel)
        cancel_button.pack(side=tk.RIGHT, padx=10, pady=10)

        dialog.update_idletasks()  # Update window size based on content
        parent.wait_window(dialog)
        return dialog.result

    @staticmethod
    def validate_credentials_dialog(parent):
        dialog = tk.Toplevel(parent)
        dialog.title("Validate Credentials")
        dialog.resizable(True, True)

        instruction_label = tk.Label(dialog, text="Please fill out the form to validate credentials.", wraplength=380)
        instruction_label.pack(padx=10, pady=10)

        email_label = tk.Label(dialog, text="Email:")
        email_label.pack(padx=5, pady=5)
        email_entry = tk.Entry(dialog)
        email_entry.pack(padx=5, pady=5)

        password_label = tk.Label(dialog, text="Password:")
        password_label.pack(padx=5, pady=5)
        password_entry = tk.Entry(dialog, show="*")
        password_entry.pack(padx=5, pady=5)

        def on_ok():
            dialog.result = {
                "email": email_entry.get(),
                "password": password_entry.get()
            }
            dialog.destroy()

        def on_cancel():
            dialog.result = None
            dialog.destroy()

        button_frame = tk.Frame(dialog)
        button_frame.pack(padx=5, pady=5)

        ok_button = tk.Button(button_frame, text="OK", command=on_ok)
        ok_button.pack(side=tk.LEFT, padx=10, pady=10)
        cancel_button = tk.Button(button_frame, text="Cancel", command=on_cancel)
        cancel_button.pack(side=tk.RIGHT, padx=10, pady=10)

        dialog.update_idletasks()  # Update window size based on content
        parent.wait_window(dialog)
        return dialog.result
    
    @staticmethod
    def drop_course_dialog(parent):
        dialog = tk.Toplevel(parent)
        dialog.title("Drop Course")
        dialog.resizable(True, True)

        instruction_label = tk.Label(dialog, text="Please fill out the form to drop a course.", wraplength=380)
        instruction_label.pack(padx=10, pady=10)

        learner_id_label = tk.Label(dialog, text="Learner ID:")
        learner_id_label.pack(padx=5, pady=5)
        learner_id_entry = tk.Entry(dialog)
        learner_id_entry.pack(padx=5, pady=5)

        course_id_label = tk.Label(dialog, text="Course ID:")
        course_id_label.pack(padx=5, pady=5)
        course_id_entry = tk.Entry(dialog)
        course_id_entry.pack(padx=5, pady=5)

        def on_ok():
            dialog.result = {
                "learner_id": learner_id_entry.get(),
                "course_id": course_id_entry.get()
            }
            dialog.destroy()

        def on_cancel():
            dialog.result = None
            dialog.destroy()

        button_frame = tk.Frame(dialog)
        button_frame.pack(padx=5, pady=5)

        ok_button = tk.Button(button_frame, text="OK", command=on_ok)
        ok_button.pack(side=tk.LEFT, padx=10, pady=10)
        cancel_button = tk.Button(button_frame, text="Cancel", command=on_cancel)
        cancel_button.pack(side=tk.RIGHT, padx=10, pady=10)

        dialog.update_idletasks()  # Update window size based on content
        parent.wait_window(dialog)
        return dialog.result
    
    @staticmethod
    def update_email_dialog(parent):
        dialog = tk.Toplevel(parent)
        dialog.title("Update Email")
        dialog.resizable(True, True)
    
        instruction_label = tk.Label(dialog, text="Please fill out the form to update the email.", wraplength=380)
        instruction_label.pack(padx=10, pady=10)
    
        user_id_label = tk.Label(dialog, text="User ID:")
        user_id_label.pack(padx=5, pady=5)
        user_id_entry = tk.Entry(dialog)
        user_id_entry.pack(padx=5, pady=5)
    
        new_email_label = tk.Label(dialog, text="New Email:")
        new_email_label.pack(padx=5, pady=5)
        new_email_entry = tk.Entry(dialog)
        new_email_entry.pack(padx=5, pady=5)
    
        def on_ok():
            dialog.result = {
                "user_id": user_id_entry.get(),
                "new_email": new_email_entry.get()
            }
            dialog.destroy()
    
        def on_cancel():
            dialog.result = None
            dialog.destroy()
    
        button_frame = tk.Frame(dialog)
        button_frame.pack(padx=5, pady=5)
    
        ok_button = tk.Button(button_frame, text="OK", command=on_ok)
        ok_button.pack(side=tk.LEFT, padx=10, pady=10)
        cancel_button = tk.Button(button_frame, text="Cancel", command=on_cancel)
        cancel_button.pack(side=tk.RIGHT, padx=10, pady=10)
    
        dialog.update_idletasks()  # Update window size based on content
        parent.wait_window(dialog)
        return dialog.result
