class Football:
    def __init__(self, helmet, uniform, cleats):

        self.helmet = helmet
        self.uniform = uniform
        self.cleats = cleats

    def home_or_away(self, gamestatus):
        print(f"This game is: {gamestatus}" )
        print("You are wearing:", self.uniform)

football = Football("Sporting Goods", "Nike", "Nike")

football.home_or_away("home") 