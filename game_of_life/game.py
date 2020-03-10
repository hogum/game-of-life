"""
    Game Environment and Transition control
"""

import os
import json

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

        Parameters
        ----------
        data_path: str
            - absolute path to the pattern files
    """

    def __init__(self, data_path='.data/'):
        if not os.path.exists(data_path):
            raise TypeError(
                "Invalid path. Pass an existing path to the patters, cool?")
        self.data_path = data_path
        self.load_config()

    def run(self, n_evolutions=100, pause=.1):
        """
            Initializes the game.

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
        pattern_name = self._prompt_user()
        pattern = self.init_pattern(pattern_name)
        n_evolutions, pause = self.cfg.get(
            'evolutions'), self.cfg.get('delay_interval')

        for i in range(n_evolutions):
            world.evolve(pattern)
            print(f'\nGeneration: {i}')
            with np.printoptions(threshold=np.inf, linewidth=np.inf):
                print(world)
            sleep(pause)

    def _prompt_user(self):
        """
            Handles the user interface.
            Requests the user for the pattern to be used
            in initializing the game.
        """
        import platform
        import subprocess

        choices = []

        if platform.system().lower().startswith('win'):
            clear_scr = 'clr'
        else:
            clear_scr = 'clear'
        try:
            subprocess.run(clear_scr, check=True)
        except subprocess.CalledProcessError:
            ...
        print('\n\t\t\t-------------------------------------------')
        print('\n\t\t\t\t\tGAME of LIFE')
        print('\n\t\t---------------------------------' +
              '---------------------------')
        print('\tThe Game of Life is best played while sipping' +
              ' coffee amid soothing sounds of a Spanish lullaby', '\n')
        print('Ready to rock:)?', ' [y/n]', end=' ')
        ans = input()

        while not ans or ans not in ('y', 'n'):
            ans = input()

        print('\nAlright!!', 'Select a pattern from one of these below\n')

        available_patterns = self.cfg.get('patterns')

        for i, ptn in enumerate(available_patterns):
            print(f'{i + 1}.  {ptn}')
            choices += [str(i + 1)]

        print('\nDo I envy the fun you are about to have? Answer? Yes!')
        print(' **[Remember to maximize terminal window for infinite fun]**')
        print('Your choice (e.g 1) ->', end=' ')
        choice = input()

        while not choice or choice not in choices:
            print(
                f'\nOopsy, {choice} not in the choices.' +
                ' Just smile and try again')
            choice = input('Your choice -> ')
        print('Starting...')

        return available_patterns[int(choice) - 1]

    def load_config(self):
        """
            Loads the JSON game config data
        """
        cfg_path = '../config.json'

        with open(cfg_path, 'r') as cfg:
            cfg_data = json.load(cfg)
        self.cfg = cfg_data

    def init_pattern(self, pattern_name):
        """
            Converts a given GOL pattern in text format
            to an array
        """
        short_blocks = ['beacon', 'glider', 'bee_hive',
                        'blinker', 'block', 'toad', 'tub']
        trim_size = self.cfg.get('trim_size')

        path = os.path.join(self.data_path, pattern_name)
        pattern = []
        with open(path) as f:
            line = f.readline()
            while line:
                ln = list(line)[:-1]
                length = len(ln)

                #  Shorten size for short blocks
                if trim_size and(length > trim_size and
                                 pattern_name in short_blocks):
                    idx = (length - trim_size / 2) // 2
                    ln = ln[idx:-idx - 1].copy()

                pattern.append(list(ln)[:-1])
                line = f.readline()
        pattern = np.asanyarray(pattern)

        pattern[pattern == '.'] = 0
        pattern[pattern == 'X'] = 1

        pattern = pattern.astype(np.int64, copy=False)
        check = pattern[(pattern != 1) & (pattern != 0)]
        if check:
            raise ValueError(
                'Found invalid characters in pattern.Use `.` and `X`')
        return pattern
