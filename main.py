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
