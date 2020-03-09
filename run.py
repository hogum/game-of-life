"""
    Starter file
"""
from game_of_life.game import Runner


def run():
    """
        Starts the game
    """
    Runner.run(n_evolutions=4, pause=0.3)


if __name__ == '__main__':
    run()
