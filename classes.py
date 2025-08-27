class Game:
    def __init__(self, title, genre, platform):
        self._title = title            
        self._genre = genre
        self._platform = platform

    def display_info(self):
        return f"Title: {self._title}, Genre: {self._genre}, Platform: {self._platform}"

    def play(self):
        return f"Playing {self._title} on {self._platform}!"

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        self._title = value

class OnlineGame(Game):
    def __init__(self, title, genre, platform, max_players):
        super().__init__(title, genre, platform)
        self.max_players = max_players

    def display_info(self):
        base_info = super().display_info()
        return f"{base_info}, Max Players: {self.max_players}"

    def play(self):
        return f"Connecting online... {self._title} supports up to {self.max_players} players!"

if __name__ == "__main__":
    g1 = Game("Chess", "Strategy", "PC")
    print(g1.display_info())
    print(g1.play())

    g2 = OnlineGame("call of duty", "Action", "PC", 100)
    print(g2.display_info())
    print(g2.play())