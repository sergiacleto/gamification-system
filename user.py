class User:
    def __init__(self, name):
        self.name = name
        self.points = 0
        self.badges = []

    def add_points(self, points):
        self.points += points

    def add_badge(self, badge):
        self.badges.append(badge)

    def __str__(self):
        return f"User: {self.name}, Points: {self.points}, Badges: {', '.join(self.badges)}"
