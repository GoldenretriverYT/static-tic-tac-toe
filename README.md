# Static Tic-Tac-Toe

> One wouldn't just, you know, make a Game, in like, ONLY HTML, no programming language at all - just plain HyperText Markup Languange - or would they?  
> Who needs JavaScript anyways, am I right? Right?  
> ...

## What is this?

TicTacToe is a solved game, meaning all possible states are calculated. This gave me the idea to make a generator, that generates all needed states of the TicTacToe board as static HTML files.  
No JavaScript is required, just plain HTML. Each click on a tile is a link (<a>-Tag) to the corresponding state.

> Disclaimer:  
> Python is only required once for generating all the HTML files, your server won't need python or anything other than the ability to server HTML files.  
> You can just copy all the html files and upload them to your Webhost


## Demo

Try it out at [tictactoe.programar.io](https://tictactoe.programar.io).


## Build it yourself

1. Clone the repo
2. Run the `generator.py` file with python
3. Copy the `output` folder to you server

> The starting URL is `/x-_________.html`


## Customize

Customize the `template.html` and the `template.css` to your liking. Make sure to have `<a id="00">` - `<a id="22">` elements, since here the player pieces and the link will be inserted.  
After customizing, don't forget to run the `generator.py` script.


## Combinations

The `gen_patterns.py` script generates all needed combinations for player x and o. It gets saved to `combinations.txt` where each line is one board state. This file is used by the `generator.py` script.

## State format

Prefix: `x-`/`o-` -> Player that placed the current move, meaning the next click will place the opposite
The rest of the 9 characters correspond to the tiles of the board. Starting top-left going down then right.
Lowercase `x` means player x
Lowercase `o` means player o
Underscore `_` or any other character means empty


> |Nr|0x|1x|2x|
> |-|-|-|-|
> |x0|1|4|7|
> |x1|2|5|8|
> |x2|3|6|9|

> |ID|0x|1x|2x|
> |--|--|--|--|
> |x0|00|10|20|
> |x1|01|11|21|
> |x2|02|12|22|

## Easy-Deployment script

Run this script with `sh` to automatically clone, pull and generate the HTML files. You'll only need to set your webserver's root to the `static-tic-tac-toe/output/` directory.

```sh
#!/bin/bash
git -C "static-tic-tac-toe" pull || git clone https://github.com/MarioMatschgi/static-tic-tac-toe

cd static-tic-tac-toe

python3 generator.py
ln -s x-_________.html ./output/index.html
```
