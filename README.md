# Classmate Finder

## Overview

The Classmate Finder is a Python program designed to help students at Sunway University find classmates who are in the same class across multiple courses. This program is tailored specifically for Sunway University's eLearn platform and requires manual input of student names from the platform.

## Features

- **Class Support**: The program supports up to 6 classes.
- **User-Friendly Input**: Prompts the user to input class names and student lists.
- **Comparison**: Finds common students across the specified classes.

## Requirements

- Python 3.x
- Manual input of student names from Sunway University's eLearn platform.


## How It Works

1. **Access e-Learn:** Log in to your Sunway University e-Learn account.
2. **Navigate to Groups:** Go to the 'Groups' section of your classes.
3. **Select CGPA:** Click on the CGPA option to view the list of students.
4. **Copy Data:** Select all the names of the students from the CGPA list and copy them.
5. **Prepare Data:** Paste the copied names as a single line of text into the command line.

## Running the Script

1. **Prepare Your Data**:
   - Go to the **Groups** section in eLearn and select all the names of students in each class.
   - Copy the names and paste them into the command line when prompted by the program.

2. **Execute the Script:**

    ```bash
    python classmate_finder.py
    ```

3. **Input Data:** When prompted, paste the copied student names into the command line as a single line.

4. **Results:** The script will process the input and output the names of students who are enrolled in the same classes as you.


