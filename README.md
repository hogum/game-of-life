## game-of-life
[![Build Status](https://travis-ci.org/hogum/game-of-life.svg?branch=master)](https://travis-ci.org/hogum/game-of-life)
[![Coverage Status](https://coveralls.io/repos/github/hogum/game-of-life/badge.svg?branch=master)](https://coveralls.io/github/hogum/game-of-life?branch=master)

[Game of life](https://en.wikipedia.org/wiki/Conway%27s_Game_of_Life) implementation in the python standard library and numpy

#### Setup
##### 1. Install the Package
- Clone
```
git clone https://github.com/hogum/game-of-life && cd game_of_life
```

- Start the Game
```
python3 run
```

-------------------------

Optionally, install the package locally
- Install
```
python3 setup.py install
```
Ensure to have the `config.json` in the root of the repository
and a data folder holdind the game patterns in the format: `game_of_life/.data/pattern_files`. If missing, they will be downloaded.
###### ~~2. Install using pip~~


~~pip install game-of-life-MUGOH==0.0.11~~


#### Testing
Run
```
pytest
```

### Playing the Game
```
example

from game_of_life import play

if __name__ == '__main__':
    play()
```
