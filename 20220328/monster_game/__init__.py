"""It's a file that contains all game entities."""


class Monster:
    """Class that stores monster's entity and all it's data."""

    def __init__(self, name, hp, x, y):
        """Fill all monster fields with data."""
        self.name = name
        self.hp = int(hp)
        self.x = int(x)
        self.y = int(y)


class Player:
    """Class that stores player's entity and it's stats."""

    def __init__(self):
        """Init method to set players postition at the start of the game."""
        self.x = 0
        self.y = 0
