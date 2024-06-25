# -*- coding: utf-8 -*-
"""
Created on Mon Jun 24 22:12:02 2024

@author: Jason Crook MySoftDev LLC.

"""

import sqlite3

class DBHelper:
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

    def add_course(self, course_id, title):
        with self.conn:
            self.conn.execute('''
                INSERT INTO courses (course_id, title)
                VALUES (?, ?)
            ''', (course_id, title))

    def enroll_learner(self, enrollment_id, learner_id, course_id):
        with self.conn:
            self.conn.execute('''
                INSERT INTO enrollments (enrollment_id, learner_id, course_id)
                VALUES (?, ?, ?)
            ''', (enrollment_id, learner_id, course_id))

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
