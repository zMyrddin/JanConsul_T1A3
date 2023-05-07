# Jan Consul - T1A3

### Presentation link
placeholder

### R4 Provide a linik to your source control repository
To be added here

### R5 Code Style Guide / Styling Conventions used
1. Indentation - The terminal app follows the standard indentation
2. Naming conventions - there is a mix of PascalCase and snake_case used in the terminal app.
3. Imports - The imports are placed at the top of the file

### R6 - App Features
1. Asks user what to do
2. User can add tasks
3. User adds points to tasks
4. User can show scores for the day and for the week
5. User can mark stuff done
6. App creates csv that stores information regarding points and tasks. It creates csv when there is none yet found.

### R7 - Implementation Plan

I've used trello to manage the project. 
![Trello board screenshot](./Images/Trello%20Screenshots/Screenshot.PNG)

Here's the outline of the implementation plan:

    Task management
        Create Task class
        Implement adding tasks
        Implement displaying tasks
        Implement marking tasks as done
        Test task management feature
![Task Management](./Images/Trello%20Screenshots/Task%20Management%20screenshot.PNG)


    Daily scores
        Implement calculating daily score
        Implement displaying daily score
        Test daily scores feature
![Daily Scores](./Images/Trello%20Screenshots/Daily%20Scores.PNG)

    Weekly scores
        Implement calculating weekly scores
        Implement displaying weekly scores
        Test weekly scores feature
![Weekly Scores](./Images/Trello%20Screenshots/Weekly%20scores.PNG)

    File Handling
        Implement CSV file handling for tasks
        Implement CSV file handling for daily scores
        Test data across app runs
![File Handling](./Images/Trello%20Screenshots/file%20handling.PNG)

    REPL structure and user interface
        Design and implement the main loop
        Implement user input processing
        Test overall user experience
![Structure](./Images/Trello%20Screenshots/Structure%20screenshot.PNG)


### R8 - Help Documentation
Gamified Daily Tracker Help Documentation

This help documentation provides instructions on how to install and use the Gamified Daily Tracker application.

Installation Steps:

    - Ensure you have Python 3.6 or later installed on your system. You can download the latest version of Python from the official website: https://www.python.org/downloads/

    - Download the folder containing main.py file and save it to a folder on your local machine.

    - Open a terminal (or Command Prompt on Windows) and navigate to the folder containing the main.py file.

Dependencies:

The Gamified Daily Tracker does not require any external libraries or dependencies. 

System/Hardware Requirements:

    1. Python 3.6 or later installed on your system
    2. A computer with a command-line interface (Terminal on macOS/Linux, Command Prompt on Windows)

Using the Gamified Daily Tracker:

    Open a terminal (or Command Prompt on Windows) and navigate to the folder containing the main.py file.

    Run the application by typing the following command and pressing Enter: "python main.py"

    The application will prompt you with the following message: "What would you like to do?". You can enter any of the following commands:
        add task: Add a new task by providing a name and assigning points to it.
        show tasks: Display the list of tasks with their current status (Done/Not done).
        mark done [task_number]: Mark a task as done by providing its number from the task list.
        show score: Display the current day's score based on the completed tasks.
        show weekly scores: Display the total scores for the week.
        quit: Save the tasks and scores, then exit the application.

For example, to add a task, type add task, and the application will ask you to enter the task name and points. After entering the information, the task will be added to your list.
