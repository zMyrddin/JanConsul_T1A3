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