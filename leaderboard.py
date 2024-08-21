class Leaderboard:
    def __init__(self):
        self.users = []

    def add_user(self, user):
        self.users.append(user)

    def get_top_users(self, top_n=3):
        sorted_users = sorted(self.users, key=lambda x: x.points, reverse=True)
        return sorted_users[:top_n]

    def __str__(self):
        leaderboard_str = "Leaderboard:\n"
        for user in self.get_top_users():
            leaderboard_str += str(user) + "\n"
        return leaderboard_str
