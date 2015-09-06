Daedalus, the great inventor, is also terribly jealous. I don't know what you
did to make him angry, but here you are: trapped in his labyrinth.

The labyrinth has twenty rooms; each room might exist in space, or time, or 
moods, or depends on the pitch of the voice or the faith of the navigator. Or
some combination thereof.

Good luck, my friend. I hope you find what you seek.

# Gameplay

For the sake of clarity, let's call each "level" (in the usual game sense) a
"room".

A room has at least two dimensions, which you can navigate with the arrow keys.
Rooms may have up to ten dimensions. If you find the right objects, you can move
through additional dimensions: stairs will let you move up/down a floor; 
calendars forward and backward through days, for example.

Sometimes it is possible to shift how you navigate dimensions; in situations
like this, the maze shifts perpendicular to itself (calendars become stairs,
stairs doors, and the walls divide up from down instead of forward from back).

All rooms are square (or cubic, or hypercubic, etc.).

Escape the labyrinth, if you can.

## In other words

Every maze is an n-dimensional square/cube of size x. Arrow keys move you
through x/y dimensions, stairs through z, and other items are markers for the
higher dimensions.

The "perspective shift" option rotates the entire maze perpendicularly: eg., the
y/z dimensions become the ones displayed on screen as the walls to move around,
and the higher dimensions (along with x) are controlled by items.

If you prefer a numeric display of this information, rather than the metaphor-
based coordinate system, you can set that in the game options.

## Other game modes

The main "campaign" mode uses twenty pre-generated rooms. You can, however, play
in randomly generated rooms of arbitrary size and number of dimensions.

All mazes are generated with a random version of Krushal's algorithm, which
means that they are always completable.

# Installation

To download the source, build the binary, and run it, do:
```
git clone git@github.com/chicken-mover/minotaur
cd minotaur
pip install -r requirements.txt
python build.py
./minotaur
```

Or you can download pre-compiled, universal executables from 
http://chicken-mover.com/downloads/.

# License

This code is (c) 2015 Michael Schuller and Chicken Mover. The source is provided
so that users can build local versions of the code, or modify it for their own
personal use. You are not authorized to redistribute this code, any art assets,
or any executable files built from this code, without express permission the #
author(s), on a person-by-person and purpose-by-purpose basis.

If you want to get that permission, email me at: michael@chicken-mover.com.
