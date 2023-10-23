# CM1101 Group Project

## Add your files
Relevant commands for adding files to git:
```
cd existing_repo
git remote add origin https://git.cardiff.ac.uk/c23033307/cm1101-group-project.git
git branch -M main
git push -uf origin main
```

***

# Project Details:

## Name
Undecided - Will need to vote on this later

## Description
This game is a text based adventure game focused on roguelite puzzle game mechanics.

**This description will be left incomplete until the final story is fully decided upon**

## Testing info
**REQUIRES FIXES**
```
Tests for game.py - Breaks upon invalid/unexpected inputs, however works as intended as long as expected inputs are entered
```

## Installation
```
Requires python3
```

## To-do list
```
This is a to do list for the project, please add your name like this:(Leo) at the end of the name of the task if you are taking on the task. Please delete the take from this file once you have completed it. Please add any more tasks that need to be completed if you think of any.
 To edit this to-do list, refer to the actual txt file in the dev-branch repository

------------------------------------------------------------------------------------------------------------------------------------
-Normalise function:
This is a function that takes the players input and removes spaces, punctuation, changes to lower class, splits the sentence into a list of words and uses a whitelist (list of words we need to keep like "go","take","north" ect) to remove unnecessary words.
This can be created in the main.py file or create a new .py file like in task 6 (gameparser.py)
------------------------------------------------------------------------------------------------------------------------------------
-Item class:
create a new .py file that holds a class which can be used to create items, this will have values like "id", "from_room" or anything else you can think of
------------------------------------------------------------------------------------------------------------------------------------
-Room initialization:
A way to take rooms from their information stored in dictionaries and creates room objects in the rooms.py file, then create a list of all the rooms that can be passed to the map class to create the map
------------------------------------------------------------------------------------------------------------------------------------
-Create room dictionaries:
This will likely be something lots of people work on, it will be inputting the information of the room (name, puzzle or riddle ect) within dictionaries that can be passed to the room initialization
------------------------------------------------------------------------------------------------------------------------------------
-Build a story:
Build a story from the ideas already stated (ask people if you have missed some of the ideas stated in the groupchat) this will include creating strings that will be printed for the player eg "Welcome to the game", "you enter a *room* there is .... inside", things like that
------------------------------------------------------------------------------------------------------------------------------------
-Create a scoring system:
The game will need a scoring system that gets larger the more puzzles you solve, and is printed to the player when completed, maybe in future add a leaderboard too that stores the top scores of the game
------------------------------------------------------------------------------------------------------------------------------------
```

## Roadmap
**Highest priority tasks-**
```
1. Get the game and map running properly without bugs or hardcoded information within the same location as the main code - including elegant error handling
2. Add relevant room details for all rooms
3. Adding optional features from the story idea files if time is available
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

**Game demo folder** -
```
This folder contains all of Linli's programs for her current ideas - refer to "story_idea" and "Story-idea-2+Lore" to see potential use cases for these files


game.py within Game demo folder - Linli's main game program using her map generation algorithm which generates a completely random map - starting room is **random**
```

**game.py** -
```
Leo's main game program using his map generation algorithm - refer to "Leo's idea" and "Story-idea-2+Lore" to see potential use cases for this file
```

**gameparser.py** -
```
The main program used to help filter and normalise words, similar to Exercise 4+6's parser; **subject to change** as we might potentially change how the program filters words
```

**map.py** -
```
Leo's map generation algorithm used to generate a random map - starting room is **constant**
```

**player.py** -
```
Contains class definitions for the player
```

**room_dicts.py** - 
```
Contains initial information for the starting room dictionary
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
Supposed to be the program responsible for creating all the room objects using dictionaries and initialising all the necessary arrays required for map generation
```
**room_initialisation.py may be deprecated later if the file is not used**

**More information about each file is given within the documentation in each file**

## Authors and acknowledgment
Show your appreciation to those who have contributed to the project.

## Project status
Ongoing
