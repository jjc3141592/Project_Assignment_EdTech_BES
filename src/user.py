# -*- coding: utf-8 -*-
"""
Created on Mon Jun 24 20:42:18 2024

@author: Jason Crook MySoftDev LLC.

"""
class User:
    """
    
    Builds the user class upon which of the user types are based.
    
    Implements 3 methods: update_email, update_password and
    validate_credentials
    
    """
    
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
