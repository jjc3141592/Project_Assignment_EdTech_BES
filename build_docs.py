# -*- coding: utf-8 -*-
"""
Created on Tue Jun 25 13:56:55 2024

@author: Jason Crook MySoftDev LLC.

"""
import os
import subprocess
from tabulate import tabulate

def build_html_docs():
    """
    Builds the HTML documentation using Sphinx and prints messages to the console.
    """
    # Get the absolute path to the project root
    project_root = os.path.abspath(os.path.dirname(__file__))

    # Construct the path to the docs directory
    docs_path = os.path.join(project_root, 'docs')

    # Change to the docs directory
    os.chdir(docs_path)

    # Run the Sphinx build command
    process = subprocess.Popen(['sphinx-build', '-b', 'html', '.', '_build/html'],
                               stdout=subprocess.PIPE,
                               stderr=subprocess.PIPE,
                               text=True)
    
    # Collect output and error messages
    output_lines = []
    error_lines = []

    for line in process.stdout:
        output_lines.append(line.strip())

    for line in process.stderr:
        error_lines.append(line.strip())

    # Wait for the process to complete and get the return code
    process.wait()

    # Format and print output messages using tabulate
    if output_lines:
        output_table = tabulate([[line] for line in output_lines], headers=["Output"], tablefmt="grid")
        print(output_table)

    # Format and print error messages using tabulate
    if error_lines:
        error_table = tabulate([[line] for line in error_lines], headers=["Error"], tablefmt="grid")
        print(error_table)

    if process.returncode == 0:
        print("HTML documentation built successfully.")
    else:
        print("Error in building HTML documentation.")

if __name__ == "__main__":
    build_html_docs()
