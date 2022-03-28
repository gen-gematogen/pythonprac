"""Start the game when run as package."""

from monster_game.cmd_init import game

if __name__ == '__main__':
    game().cmdloop()
