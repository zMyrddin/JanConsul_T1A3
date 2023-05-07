import csv
import datetime

class Task:
    def __init__(self, name, points):
        self.name = name
        self.points = points
        self.done = False

    def mark_done(self):
        self.done = True

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
            print("No scores available yet.")
        else:
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
            print(f"No '{filename}' file found. A new file will be created when the day is saved.")

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
            print(f"No '{filename}' file found. A new file will be created when tasks are added.")

    def save_tasks_to_csv(self, filename):
        with open(filename, 'w', newline='') as csvfile:
            writer = csv.writer(csvfile)
            for task in self.tasks:
                writer.writerow([datetime.date.today(), task.name, task.points, task.done])

    def display_tasks(self):
        if not self.tasks:
            print("There are no tasks yet!")
        else:
            for index, task in enumerate(self.tasks):
                status = "Done" if task.done else "Not done"
                print(f"{index + 1}. {task.name} ({task.points} points) - {status}")

    def display_weekly_scores(self):
        today = datetime.date.today()
        start_of_week = today - datetime.timedelta(days=today.weekday() % 7)

        weekly_scores = [score for score in self.daily_scores if start_of_week <= score[0] < start_of_week + datetime.timedelta(days=7)]

        for date, earned_points, total_points in weekly_scores:
            print(f"{date}: {earned_points}/{total_points}")

tracker = DailyTracker()
tracker.load_scores_from_csv('daily_scores.csv')
tracker.load_tasks_from_csv('tasks.csv')

