# -*- coding: utf-8 -*-
"""
Created on Mon Jun 24 22:12:02 2024

@author: Jason Crook MySoftDev LLC.

"""

import sqlite3

class DBHelper:
    """
    A database helper class to maintain records in the database    
    
    """
    def __init__(self, db_name='sltech.db'):
        self.conn = sqlite3.connect(db_name)
        self.create_tables()

    def create_tables(self):
        with self.conn:
            self.conn.execute('''
                CREATE TABLE IF NOT EXISTS users (
                    user_id TEXT PRIMARY KEY,
                    email TEXT NOT NULL,
                    password TEXT NOT NULL,
                    user_type TEXT NOT NULL
                )
            ''')
            self.conn.execute('''
                CREATE TABLE IF NOT EXISTS courses (
                    course_id TEXT PRIMARY KEY,
                    title TEXT NOT NULL
                )
            ''')
            self.conn.execute('''
                CREATE TABLE IF NOT EXISTS enrollments (
                    enrollment_id TEXT PRIMARY KEY,
                    learner_id TEXT,
                    course_id TEXT,
                    FOREIGN KEY(learner_id) REFERENCES users(user_id),
                    FOREIGN KEY(course_id) REFERENCES courses(course_id)
                )
            ''')

    def add_user(self, user_id, email, password, user_type):
        with self.conn:
            self.conn.execute('''
                INSERT INTO users (user_id, email, password, user_type)
                VALUES (?, ?, ?, ?)
            ''', (user_id, email, password, user_type))
            self.conn.commit()

    def add_course(self, course_id, title):
        with self.conn:
            self.conn.execute('''
                INSERT INTO courses (course_id, title)
                VALUES (?, ?)
            ''', (course_id, title))
            self.conn.commit()

    def enroll_learner(self, enrollment_id, learner_id, course_id):
        with self.conn:
            self.conn.execute('''
                INSERT INTO enrollments (enrollment_id, learner_id, course_id)
                VALUES (?, ?, ?)
            ''', (enrollment_id, learner_id, course_id))
            self.conn.commit()

    def get_users(self):
        cursor = self.conn.cursor()
        cursor.execute('SELECT * FROM users')
        return cursor.fetchall()

    def get_courses(self):
        cursor = self.conn.cursor()
        cursor.execute('SELECT * FROM courses')
        return cursor.fetchall()

    def get_enrollments(self):
        cursor = self.conn.cursor()
        cursor.execute('SELECT * FROM enrollments')
        return cursor.fetchall()
    
    def update_password(self, user_id, new_password):
        try:
            with self.conn:
                cursor = self.conn.cursor()
                cursor.execute('''
                    UPDATE users
                    SET password = ?
                    WHERE user_id = ?
                ''', (new_password, user_id))
                self.conn.commit()
                if cursor.rowcount == 0:
                    print(f"No user found with user_id: {user_id}")
                else:
                    print(f"Password updated for user_id: {user_id}")
        except sqlite3.Error as e:
            print(f"An error occurred: {e}")
                
    def update_email(self, user_id, new_email):
        try:
            with self.conn:
                cursor = self.conn.cursor()
                cursor.execute('''
                    UPDATE users
                    SET email = ?
                    WHERE user_id = ?
                ''', (new_email, user_id))
                self.conn.commit()
                if cursor.rowcount == 0:
                    print(f"No user found with user_id: {user_id}")
                else:
                    print(f"Email updated for user_id: {user_id}")
        except sqlite3.Error as e:
            print(f"An error occurred: {e}")


    def drop_course(self, learner_id, course_id):
        with self.conn:
            self.conn.execute('''
                DELETE FROM enrollments
                WHERE learner_id = ? AND course_id = ?
            ''', (learner_id, course_id))
            self.conn.commit()

    def validate_credentials(self, email, password):
        cursor = self.conn.cursor()
        cursor.execute('''
            SELECT user_id, user_type FROM users
            WHERE email = ? AND password = ?
        ''', (email, password))
        return cursor.fetchone()
