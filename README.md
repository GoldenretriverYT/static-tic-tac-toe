# Static Tic-Tac-Toe

## What is this?

TicTacToe is a solved game, meaning all possible states are calculated. This gave me the idea to make a generator, that generates all needed states of the TicTacToe board as static HTML files.  
No JavaScript is required, just plain HTML. Each click on a tile is a link (<a>-Tag) to the corresponding state.


## Demo

Try it out at [tictactoe.programar.io](https://tictactoe.programar.io).


## Build it yourself

1. Clone the repo
2. Run the `generator.py` file with python
3. Copy the `output` folder to you server

> The starting URL is `/x-_________.html`


## Combinations

The `gen_patterns.py` script generates all needed combinations for player x and o. It gets saved to `combinations.txt` where each line is one board state. This file is used by the `generator.py` script.

## State format

Prefix: `x-`/`o-` -> Player that placed the current move, meaning the next click will place the opposite
The rest of the 9 characters correspond to the tiles of the board. Starting top-left going down then right.
Lowercase `x` means player x
Lowercase `o` means player o
Underscore `_` or any other character means empty

> 1 4 7
> 2 5 8
> 3 6 9

## Deployment script

```sh

```
