## game-of-life
[![Build Status](https://travis-ci.org/hogum/game-of-life.svg?branch=master)](https://travis-ci.org/hogum/game-of-life)
[![Coverage Status](https://coveralls.io/repos/github/hogum/game-of-life/badge.svg?branch=master)](https://coveralls.io/github/hogum/game-of-life?branch=master)

[Game of life](https://en.wikipedia.org/wiki/Conway%27s_Game_of_Life) implementation in the python standard library and numpy

#### Setup
##### 1. Initiliazing the Game
- Get a cloned local copy
```
    git clone https://github.com/hogum/game-of-life
```

**Switch to the working directory**

```
    cd game-of-life
```

**Starting the Game**
- You need to have `numpy` installed: `pip install -r requirements.txt` or simply `pip install numpy`
- Then simply start the game with:
```
    python3 run
```

-------------------------


#### Testing
- In the root directory, run:
```
    pytest
```
----------------------------------------------


##### Optionally, you could opt to install the package locally

**Either**
```
python3 setup.py install
```
Ensure to have the `config.json` in the root of the repository
and a data folder holdind the game patterns in the path: `game_of_life/.data/*`


**Or**

```
    pip install game-of-life-MUGOH==0.0.11
```
