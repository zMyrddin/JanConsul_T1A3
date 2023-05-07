class Task:
    def __init__(self, name, points):
        self.name = name
        self.points = points
        self.done = False
        
    def mark_done(self):
        self.done = True
