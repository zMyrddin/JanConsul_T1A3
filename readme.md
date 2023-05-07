# Jan Consul - T1A3

### Presentation link
https://youtu.be/7bYDt67od8E


### R3 - External resources used
2 external resources that I've used is my brother who is a vet as well at the field and ChatGPT for some information. (datetime function and weekly tally function)

### R4 Provide a linik to your source control repository
https://github.com/zMyrddin/JanConsul_T1A3

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
![Trello board screenshot](./docs/Trello%20Screenshots/Screenshot.PNG)

Here's the outline of the implementation plan:

    Task management
        Create Task class
        Implement adding tasks
        Implement displaying tasks
        Implement marking tasks as done
        Test task management feature
![Task Management](./docs/Trello%20Screenshots/Task%20Management%20screenshot.PNG)


    Daily scores
        Implement calculating daily score
        Implement displaying daily score
        Test daily scores feature
![Daily Scores](./docs/Trello%20Screenshots/Daily%20Scores.PNG)

    Weekly scores
        Implement calculating weekly scores
        Implement displaying weekly scores
        Test weekly scores feature
![Weekly Scores](./docs/Trello%20Screenshots/Weekly%20scores.PNG)

    File Handling
        Implement CSV file handling for tasks
        Implement CSV file handling for daily scores
        Test data across app runs
![File Handling](./docs/Trello%20Screenshots/file%20handling.PNG)

    REPL structure and user interface
        Design and implement the main loop
        Implement user input processing
        Test overall user experience
![Structure](./docs/Trello%20Screenshots/Structure%20screenshot.PNG)


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


### R15 - Testing

Test 1: Testing the 'add task' feature

What is being tested: The ability of the user to add a task with a point value to the daily tracker

Test case 1:

    Input: Add task 'Do pushups' with 5 points
    Expected result: Task 'Do pushups' with 5 points is added to the daily tracker

Test case 2:

    Input: Add task 'Feed the dog' with 3 points
    Expected result: Task 'Feed the dog' with 3 points is added to the daily tracker

Test 2: Testing the 'save day' feature

What is being tested: The ability of the user to save the daily tasks and display their daily score

Test case 1:

    Input: Mark all added tasks as done and save the day
    Expected result: The application displays the user's daily score out of the total possible points for the day

Test case 2:

    Input: Mark some tasks as done and leave some tasks incomplete, then save the day
    Expected result: The application displays the user's daily score out of the total possible points for the day, taking into account the incomplete tasks


