"""
    Game Environment and Transition control
"""

from dataclasses import dataclass, field

import numpy as np


@dataclass
class Universe:
    """
        This is a representation of the world in which
        evolutions and rule transitions occur

    Parameters
    ---------------

    size: tuple
        Size of the world grid
    random: bool
        Whether to initialize the world population randomly
    """
    size: tuple = (10, 10)
    random: bool = False
    world: None = field(init=False)

    def evolve(self, world):
        """
            Completes a generation by applying the game rules
            to the existing world  population.
                - Live cell with two or three neighbors survives.
                - Dead cell with three live neighbors becomes a live cell.
        """
        self.world = world
        self._retrieve_neighbours()

        survivals = ((self.neighbours == 2) | (self.neighbours == 3)) & (
            world[1: -1, 1: -1] == 1)
        new_lives = (self.neighbours == 3) & (world[1: -1, 1: -1] == 0)

        world[:, :] = 0
        world[1: -1, 1: -1][survivals | new_lives] = 1

    def _retrieve_neighbours(self):
        """
            Retrieves cells that represent the neighbours
            of each world cell.
            Each index represents a neighbour in one of the
            possible directions from the cell.
             - ie N, S, E, W, NE, NW, SE, SW
            (8 directions in total)
        """
        world = self.world
        # Top rows
        # Bottom rows
        self.neighbours = world[0:-2, 0:-2] + world[0:-2, 1:-1] \
            + world[0:-2, 2:] +  \
            world[2:, 0:-2] + world[2:, 1:-1] + world[2:, 2:] +  \
            world[1:-1, 0:-2] + world[1:-1, 2:]  # Mid rows

    def __repr__(self):
        return f'{self.world}'


class Runner:
    """
        Handles loading of the game and
        interations with user
    """

    @classmethod
    def run(cls, n_evolutions=100, pause=.1):
        """
            Initializes the game

            Paramaters
            ----------
            n_evolutions: int
                - Number of generations to evolve
            pause: float | (default = .1)
                - Duration in seconds to pause while printing
                  each generation
        """
        from time import sleep

        world = Universe(random=False)
        ss = np.array([[0, 0, 0, 0, 0, 0],
                       [0, 0, 1, 1, 0, 0],
                       [0, 1, 0, 1, 0, 0],
                       [0, 0, 1, 1, 0, 0],
                       [0, 0, 0, 0, 0, 0],
                       [0, 0, 0, 0, 0, 0]])
        for i in range(n_evolutions):
            world.evolve(ss)
            print(f'Generation: {i}')
            print(world)
            sleep(pause)

    def load_config(self):
        ...
