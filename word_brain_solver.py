"""
word_brain_solver.py is a simply utility script that can be used to solve Word Brain/Word Up/any Boogle-type derivative.

It works by loading a word dictionary (12Dicts: http://wordlist.aspell.net/12dicts/) into a hashmap. Then it uses a recursive
strategy to iterate over every possible combination of letters present in the puzzle.

This is not the most optimized approach, it solves 6x6 puzzles in ~2 seconds.
"""

import mmap
from collections import defaultdict

def is_new_valid_word(word):
    return word not in found_words[len(word)] and word in word_dict[word[0]]

def recursive_search(x, y, cur_word):
    visited[x][y] = True
    cur_word += letters[x][y]

    if is_new_valid_word(cur_word):
        found_words[len(cur_word)].append(cur_word)

    row = x-1
    while row <= x+1 and row < matrix_size:
        col = y - 1
        while col <= y+1 and col < matrix_size:
            if row >= 0 and col >= 0 and not visited[row][col] and len(cur_word) < max_word_length:
                recursive_search(row, col, cur_word)

            col += 1
        row += 1

    cur_word = cur_word[:-1]
    visited[x][y] = False

if __name__ == "__main__":
    word_dict = defaultdict(list)
    with open('word_list.txt') as word_list_file:
        for word in word_list_file.readlines():
            word_dict[word[0]].append(word.strip())

    letters = [ ]

    print "Type letters. Hit Enter for next line. (Enter a blank line when done):"

    line = 0
    while True:
        temp_line = raw_input("Line " + str(line+1) + ": ")
        if len(temp_line) is 0:
            break

        letters.append(list(temp_line))
        line += 1

    matrix_size = len(letters[0])

    visited = [[False for x in range(matrix_size)] for y in range(matrix_size)]

    max_word_length = int(raw_input("Max word length: "))

    found_words = defaultdict(list)
    cur_word = ""
    for i in xrange(0, matrix_size):
        for j in xrange(0, matrix_size):
                    recursive_search(i, j, cur_word)

    for key, list in found_words.iteritems():
        if key is not 1 and key is not 2:
            print key, sorted(list)
            
