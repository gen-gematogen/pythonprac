"""Implement CLI for the game."""

import shlex
import cmd
from monster_game import Monster, Player


class game(cmd.Cmd):
    """Store all data about CLI actions."""

    prompt = "> "
    monsters = []
    player = Player()
    cnt = 0

    def do_add(self, arg):
        """Insert new monster on the field."""
        args = shlex.split(arg)
        name = args[2]
        hp = args[4]
        x = args[6]
        y = args[7]
        for monster in self.monsters:
            if monster.x == x and monster.y == y and monster.name == name:
                monster.hp = hp
                return
        self.monsters.append(Monster(name, hp, x, y))

    def do_show(self, arg):
        """Print for user data about monsters."""
        for monster in self.monsters:
            print(f"{monster.name} at ({monster.x} {monster.y}) hp {monster.hp}")

    def do_move(self, arg):
        """Try moving player on the filed and if possible do it."""
        args = shlex.split(arg)
        phrase = "cannot move"
        if args[0] == "up":
            if self.player.y < 9:
                self.player.y += 1
                phrase = ""
        elif args[0] == "down":
            if self.player.y > 0:
                self.player.y -= 1
                phrase = ""
        elif args[0] == "right":
            if self.player.x < 9:
                self.player.x += 1
                phrase = ""
        elif args[0] == "left":
            if self.player.x > 0:
                self.player.x -= 1
                phrase = ""

        if phrase:
            print(phrase)
        else:
            print(f"player at {self.player.x} {self.player.y}")
            monsters_in_field = []
            for monster in self.monsters:
                if monster.x == self.player.x and monster.y == self.player.y:
                    monsters_in_field.append(f"{monster.name} {monster.hp} hp")
