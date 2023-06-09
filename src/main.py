from task import Task
import csv
import datetime


class DailyTracker:
    def __init__(self):
        self.tasks = []
        self.daily_scores = []

    def add_task(self, name, points):
        task = Task(name, points)
        self.tasks.append(task)

    def mark_task_done(self, task_index):
        self.tasks[task_index].mark_done()

    def save_day(self):
        total_points = sum([task.points for task in self.tasks])
        earned_points = sum([task.points for task in self.tasks if task.done])

        self.daily_scores.append((datetime.date.today(), earned_points, total_points))
        self.save_tasks_to_csv('tasks.csv')
        self.save_scores_to_csv('daily_scores.csv')

    def display_scores(self):
        if not self.daily_scores:
            print("No scores available yet. Please create a task and save it.")
        else:
            print("Here is today's score: ")
            date, earned_points, total_points = self.daily_scores[-1]
            print(f"{date}: {earned_points}/{total_points}")


    def load_scores_from_csv(self, filename):
        try:
            with open(filename, 'r') as csvfile:
                reader = csv.reader(csvfile)
                for row in reader:
                    date = datetime.datetime.strptime(row[0], "%Y-%m-%d").date()
                    earned_points = int(row[1])
                    total_points = int(row[2])
                    self.daily_scores.append((date, earned_points, total_points))
        except FileNotFoundError:
            print("It seems this is the first time you have used me! Once you finish adding a few tasks and choose save, a simple log of past activities will be accessible by me to keep track of your progress!")

    def save_scores_to_csv(self, filename):
        with open(filename, 'w', newline='') as csvfile:
            writer = csv.writer(csvfile)
            for date, earned_points, total_points in self.daily_scores:
                writer.writerow([date, earned_points, total_points])

    def load_tasks_from_csv(self, filename):
        try:
            with open(filename, 'r') as csvfile:
                reader = csv.reader(csvfile)
                for row in reader:
                    date = datetime.datetime.strptime(row[0], "%Y-%m-%d").date()
                    if date == datetime.datetime.now().date():
                        name = row[1]
                        points = int(row[2])
                        done = row[3] == 'True'
                        task = Task(name, points)
                        task.done = done
                        self.tasks.append(task)
        except FileNotFoundError:
            pass

    def save_tasks_to_csv(self, filename):
        with open(filename, 'w', newline='') as csvfile:
            writer = csv.writer(csvfile)
            for task in self.tasks:
                writer.writerow([datetime.date.today(), task.name, task.points, task.done])

    def display_tasks(self):
        if not self.tasks:
            print("There are no tasks yet!")
        else:
            print("Here are your tasks for the day: ")
            for index, task in enumerate(self.tasks):
                status = "Done" if task.done else "Not done"
                print(f"{index + 1}. {task.name} ({task.points} points) - {status}")

    def display_weekly_scores(self):
        print("Here are your scores for the week!")        
        today = datetime.date.today()
        start_of_week = today - datetime.timedelta(days=today.weekday() % 7)

        weekly_scores = [score for score in self.daily_scores if start_of_week <= score[0] < start_of_week + datetime.timedelta(days=7)]

        seen_dates = set()
        weekly_scores_filtered = []
        for score in reversed(weekly_scores):
            if score[0] not in seen_dates:
                seen_dates.add(score[0])
                weekly_scores_filtered.append(score)

        for date, earned_points, total_points in reversed(weekly_scores_filtered):
            print(f"{date}: {earned_points}/{total_points}")


tracker = DailyTracker()
tracker.load_scores_from_csv('daily_scores.csv')
tracker.load_tasks_from_csv('tasks.csv')

while True:
    print("This is your personal daily tracker with points!")
    print("Choose any action from the list below:")
    print("Enter 1 to Add Tasks")
    print("Enter 2 to Mark Tasks done")
    print("Enter 3 to Save the daily tasks and update")
    print("Enter 4 to Show today's scores")
    print("Enter 5 to Show today's tasks")
    print("Enter 6 to Show weekly scores")
    print("Enter 7 to End usage of the App Tracker")                 
    action= input("What do you want to do? ")

    if action == "1":
        task_name = input("Enter task name: ")
        task_points = int(input("Enter task points: "))
        tracker.add_task(task_name, task_points)
        print("Would you like to do anything else?")        

    elif action == "2":
        tracker.display_tasks()
        task_index = int(input("Enter the task number you want to mark as done: ")) - 1
        if task_index < len(tracker.tasks):
            tracker.mark_task_done(task_index)
        else:
            print("Invalid task number.")
            add_new = input("Do you want to add a new task to the list? (yes/no): ")
            if add_new.lower() == "yes":
                task_name = input("Enter task name: ")
                task_points = int(input("Enter task points: "))
                tracker.add_task(task_name, task_points)
                tracker.mark_task_done(task_index)
        print("Would you like to do anything else?")                

    elif action == "3":
        tracker.save_day()
        print("Would you like to do anything else?")        

    elif action == "4":
        tracker.display_scores()
        print("Would you like to do anything else?")   

    elif action == "5":
        tracker.display_tasks()
        print("Would you like to do anything else?")

    elif action == "6":
        tracker.display_weekly_scores()
        print("Would you like to do anything else?")

    elif action == "7":
        print("Thank you for using the Gamified To-do Tracker!")
        break

    else:
        print("Invalid action, please try again.")