# CM1101 Group Project
***

# Odyssey of the Forgotten

## Description
Stranded on a mysterious island with no recollection of your past, you must navigate the treacherous terrain, explore ancient ruins, and solve various puzzles and riddles to piece together a functional plane and make your daring escape.

## Roadmap
**Version 1.0 (Current version)**

*Feature list:*
```
1. Randomly Generated Ruins: 
   Each playthrough offers a unique experience as the island's ancient ruins shift and change, presenting new challenges and mysteries to solve with every playthrough!

2. A variety of Puzzles and Riddles: 
   Investigate the mysterious markings found deep within the ruins and uncover the hidden messages that were intended to be hidden away for eternity.
   
   Base Puzzles:
   -    Sudoku
   -    Chess
   -    Connect the wire

5. Exploration: 
   Scour the island's lush, uncharted wilderness for resources, tools, and hidden artifacts, using them to construct vital components for your plane.

6. Choices and Consequences - Multiple Endings:
   Your decisions influence the outcome of your adventure. Will you take the risk and delve into uncharted territory for a great reward at the end, or will you play it safe and quietly leave the island, leaving no trace of your exploits?
```

**Version 1.1 (Future patch)**

*Features still work in progress*
```
1. Leaderboards: 
   Store your scores and compete against your previous playthroughs to give your final endings some more meaning
   
2. Titles: 
   Collect various titles based on your achievements and exploits within the ruins!

5. More rooms:
   As time goes on, you find out that the ruins were even more vast than you imagined, brimming with experiences never seen before; perhaps there is more to the ruins than one might have initially thought

6. Choices and Consequences:
   Your decisions influence the outcome of your adventure. Will you take the risk and delve into uncharted territory for a great reward at the end, or will you play it safe and quietly leave the island, leaving no trace of your exploits?

7. A race against time:
   The more you begin to understand of the ruins, the more you realise how precarious your situation is... You find that your time is quickly running out, lest you get consumed by the ruins and the mysteries that surround it... Will you find all the parts and make it out in time?
   
8. Bug-fixes
```

## Installation
```
Requires python3
```

## Project dictionary
**Group Project Ideas folder** - 
```
The folder stores all the relevant information about our project's ideas in the form of txt files
```

**NOTE** -
This is not to be confused with the .idea folder which is entirely useless and non-functional - it exists as a byproduct of using a jetbrains IDE

**The most relevant txt files to go through currently are**
```
"background story", "Puzzle-ideas", "story_idea" and "Story-idea-2+Lore" as these contain the current info about what the story potentially is about
```

**Note that the current story is not completely decided and the final parts will need to be voted upon**

**game.py** -
```
The main game program that runs all the various modules necessary for running the game
```

**normalise_function.py** -
```
The main program used to help filter and normalise words, using a whitelist of words
```

**map.py** -
```
The map generation algorithm used to generate a random map
```

**player.py** -
```
Contains class definitions for the player as well as the relevant methods
```

**room_dicts.py** - 
```
Contains initial information for all the starting rooms dictionaries as well as an array that contains all these dictionaries to be processed in other programs
```

**rooms.py** - 
```
Contains class definitions for all room types as well as relevant getters, setters and methods
```

**To do list** - 
```
Editable file for all remaining tasks left to do that are currently not complete
```

**room_initialisation.py** - 
```
Responsible for creating all the room objects using dictionaries and initialising all the necessary arrays required for map generation
```

**items.py** -
```
Contains class definitions for all the items as well as relevant methods
```

**item_dicts.py** -
```
Contains all the initial information for all the items as well as an array that stores all these items to reference in other programs
```

**puzzle_data.py**
```
Program used to store all relevant information for the sudoku puzzles
```

**chess_boards.py**
```
Program used to store all relevant information for the chess puzzles
```

**puzzle_pip.py**
```
Program used to store and process all relevant information about the connect the wire puzzle
```

**More information about each file is given within the documentation in each file**

## Bugs to be fixed
```
For answer_check() within the Chess class:
Regex will need to be updated to account for potential inputs such as qe8x3 sending an "incorrect answer" flag rather than a "incorrect format" flag

for puzzle_pip.py:
May need to rework the swap and open logic to account for incidents where you may reopen a spot that was already opened and swapped, resulting in the slot to return to its original state instead
```

## Project status
Ongoing

## Add your files
Relevant commands for adding files to git:
```
cd existing_repo
git remote add origin https://git.cardiff.ac.uk/c23033307/cm1101-group-project.git
git branch -M main
git push -uf origin main
```
