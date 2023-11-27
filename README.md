# Task-app

This is a simple To-Do web application built using Flask and SQLAlchemy, allowing users to create, mark as done, and delete tasks.

![To do!](/assets/todolist.PNG "Reference")

## Setup

** Install Dependencies**

   Ensure you have Python installed. Then, install Flask and SQLAlchemy using pip:

   `pip install Flask SQLAlchemy`

** Run the Application**

Execute the following command in your terminal:

   `python app.py`

   This will start the Flask development server.
## Code Structure

>app.py

The main Flask application file containing routes for:

- **/**: Renders the home page displaying all tasks.
- **/create-task**: Creates a new task.
- **/done/id**: Marks a task as done.
- **/delete/id**: Deletes a task.

>'Task' Model

Defines the Task model using SQLAlchemy with attributes:

- **id**: Primary key for tasks.
- **content**: Description of the task.
- **done**: Indicates whether the task is completed.
## Notes

The app uses SQLite as its database **(tasks.sqlite).**
