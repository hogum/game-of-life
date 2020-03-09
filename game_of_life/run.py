"""
    Starter file
"""
from game import Runner


def run():
    """
        Starts the game
    """
    # Runner.run(n_evolutions=4, pause=0.3)
    c = Runner()
    c.init_pattern('glider')


if __name__ == '__main__':
    run()
