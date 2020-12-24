# word_brain_solver
A utility script to solve Word Brain/Word Up/any Boogle-type derivative.

[![asciicast](https://asciinema.org/a/381014.svg)](https://asciinema.org/a/381014)

## Usage
1. Run `$ python word_brain_solver.py`
2. Enter in the letters on each line in one string without spaces.
3. Enter a blank line when you are finished with all the lines.
4. Enter the max word length expected by the puzzle.

Requires Python 2.7.x.

## Background
This works by loading a word dictionary (12Dicts: http://wordlist.aspell.net/12dicts/) into a hashmap. Then it uses a recursive strategy to iterate over every possible combination of letters present in the puzzle.

This is not the most optimized approach, but it solves 6x6 puzzles in ~2 seconds.

## Development
This does not use any extra libraries.
