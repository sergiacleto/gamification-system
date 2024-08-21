class Badge:
    def __init__(self, name, description):
        self.name = name
        self.description = description

    def __str__(self):
        return f"Badge: {self.name} - {self.description}"
