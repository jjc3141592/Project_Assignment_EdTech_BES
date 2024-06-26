# -*- coding: utf-8 -*-
"""
Created on Mon Jun 24 21:13:07 2024

@author: Jason Crook MySoftDev LLC.

"""
import os
import sys
sys.path.insert(0, os.path.abspath('../src/'))
#print(f"sys.path: {sys.path}\n")


# docs/conf.py
project = 'SL Tech Backend System'
author = 'Jason Crook MySoftDev LLC'
extensions = ['sphinx.ext.autodoc', 'sphinx.ext.napoleon']
# Paths that contain custom static files (such as style sheets)
# These files are copied after the built-in static files, so a file
# named "default.css" will overwrite the built-in "default.css".
html_static_path = ['_static']
templates_path = ['_templates']
exclude_patterns = []
html_theme = 'alabaster'
html_static_path = ['_static']
add_module_names = False
master_doc = 'index'
