# EdTech_BES
 Course Project: EdTech Backend System
 By: Jason Crook
 For: Purdue Post Graduate Degree in Data Science
 Course: PGP DS - Programming Refresher
 
# SL Tech Backend System

This project is a backend system for SL Tech's learner interface, including user, course, and enrollment management. It features a simple GUI built with `tkinter` and formatted outputs using `tabulate`.

## Requirements

- Python 3.x
- `tk`
- `tabulate`
- `sphinx` (for documentation)

## Setup

1. Clone the repository.
2. Install the required packages: See requirements above
3. If needed set path to "src" folder so the IDE you are using will look to the correct folder for the source files
4. Uncomment the line of code in 4a) in the gui.py file on line 77 to populate the database with sample data 
    4a)# backend = populate_data(backend)  # Populate with test data
    4b)After initial run you will need to comment out this line of code otherwise you will get a "UNIQUE" database error
5. Run the file gui.py to run the application.
