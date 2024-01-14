# WWE Supercard Codebreaker Solver

This is a simple script that will help players of WWE Supercard play the Codebreaker game mode. This game mode is a simple game of Mastermind, where the player has to guess a 4-digit code of 4 arrows. The player has 4 guesses to get the code right, with the game only telling the player how many arrows are in the correct position, and how many arrows are the correct arrow but in the wrong position.
The script is based on Donald Knuth's 5-guess algorithm, which is a simple algorithm that will always solve the game in 5 guesses or less in the following steps:
1. Create a set of all possible codes (4 arrows, 4 positions, so 256 possible codes)
2. Start with UP UP DOWN DOWN
3. Receive the number of arrows in the correct position, and the number of arrows that are the correct arrow but in the wrong position
4. Remove all codes from the set that do not match the user's feedback
5. Repeat steps 2-4 until there is only one code left in the set or the user inputs 4 correct arrows in the correct positions


## Setup

```sh
$ pip install itertools
```

```sh
$ pip install colorama
```

You might want to use pyinstaller to create an executable file for the script.

```sh
$ pip install pyinstaller
```

```sh
$ pyinstaller --noconfirm --clean --onefile --console --icon=icon.ico codebreaker.py
```

The executable file will be located in the dist folder.


## Running

```sh
$ python codebreaker.py
```

Or run the executable file located in the dist folder (if you used pyinstaller).

## Screenshots

![Screenshot 1](https://i.imgur.com/okRQwad.png)