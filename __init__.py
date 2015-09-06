"""
But of all the games, I prefer the one about 
the other Asterion. I pretend that he comes to visit me and that I show him my 
house. With great obeisance I say to him "Now we shall return to the first 
intersection" or "Now we shall come out into another courtyard" Or "I knew you 
would like the drain" or "Now you will see a pool that was filled with sand" or
"You will soon see how the cellar branches out". Sometimes I make a mistake and
the two of us laugh heartily.


FIXME:

- Show the Xn, Yn (notional X, notional Y) in each view
- And then be able to adjust the "floor", which is the value of *each other axis*.

Ie, in 2 dimensions, there are no floors
... in 3 dimensions, the floor is the value of Z
... in n dimensions, the floor is the value of (Z, An, An+1, ...)

Or put another way, in a 3d display, you display (Xn, Yn, Zn), and the next axis
An becomes the "frame".  (An+1, An+2, ...) constitute "frames" in different
"branches".

DIMENSIONS:

height
width
length
day
color
mood
name

...
"""

import pyglet
import sys

from pyglet.window import key

import krushal
import player
import dimensions

W_SIZE=200
level=2

M_SIZE=2
M_DIMS=2

CELL_SIZE = W_SIZE/M_SIZE

maze = None

class Wall(object):

    def __init__(self, x1, y1, orientation="horizontal"):

        if orientation == "horizontal":
            x2 = x1 + 2
            y2 = y1 + CELL_SIZE
        else:
            x2 = x1 + CELL_SIZE
            y2 = y1 + 2

        self.verts = pyglet.graphics.vertex_list(4, 
            ('v2f', (
                x1,
                y1,

                x2,
                y1,

                x2,
                y2,

                x1,
                y2,
            )),
        )

    def draw(self):
        self.verts.draw(pyglet.gl.GL_QUADS)

class Item(object):

    def __init__(self, x, y, text):

        x+=1
        y+=CELL_SIZE

        self.label = pyglet.text.Label(
            text,
            x=x,
            y=y,
            font_size=8,
            color=(255,0,0,255),
            anchor_x='left',
            anchor_y='top',
        )

    def draw(self):
        self.label.draw()


class MWindow(pyglet.window.Window):

    dim_names = "xyzabcdefghijklmnopqrstuvwXYZABCDEFGHIJKLMNOPQRSTUVW"

    keys = {
        key.V: "view_switch",
        key._1: "floor_switch",
        key._2: "floor_switch",
        key._3: "floor_switch",
        key._4: "floor_switch",
        key._5: "floor_switch",
        key._6: "floor_switch",
        key._7: "floor_switch",
        key._8: "floor_switch",
        key._9: "floor_switch",
        key.Q: "quit",
        key.UP: "move",
        key.DOWN: "move",
        key.LEFT: "move",
        key.RIGHT: "move",
    }


    def _maze(self):
        global maze
        global level

        global M_SIZE
        global M_DIMS
        global CELL_SIZE

        level += 1

        M_SIZE = level
        M_DIMS = level
        CELL_SIZE = W_SIZE/M_SIZE

        maze = krushal.Maze(M_SIZE, M_DIMS)
        maze.generate()

        self.player = player.Player(maze.start, CELL_SIZE)
        self.dim_offs = 0


    def __init__(self):
        super(MWindow, self).__init__(
            W_SIZE,
            W_SIZE, 
            resizable=False, 
            caption="above, the intricate sun; below Asterion"
        )
        self._maze()


    def on_draw(self):
        self.clear()
        self.player.draw(*self.getxyo())
        self.draw_walls()
        self.show_label()
        self.draw_items()


    def on_key_press(self, symbol, modifiers):
        fname = self.keys.get(symbol)
        if fname:
            getattr(self, fname)(symbol, modifiers)

        # FIXME: shouldn't be here
        if self.player.position == maze.end:
            self._maze()


    def move(self, symbol, modifiers):
        x = y = 0
        if symbol == key.UP:
            y = 1
        elif symbol == key.RIGHT:
            x = 1
        elif symbol == key.DOWN:
            y = -1
        else:
            x = -1
        ix, iy = self.getxyo()
        new_pos = list(self.player.position)
        new_pos[ix] += x
        new_pos[iy] += y
        return self.player.move(new_pos, maze)


    def view_switch(self, symbol, modifiers):
        self.dim_offs += 1
        if self.dim_offs > maze.dimensions - 1:
            self.dim_offs = 0


    def floor_switch(self, symbol, modifiers):
        if modifiers & key.MOD_CTRL:
            n = -1
        else:
            n = 1
        
        numkeys = [getattr(key, "_%s" % i) for i in xrange(1, 10)]
        idx = numkeys.index(symbol)

        end = list(self.player.position)
        try:
            end[idx] += n
        except IndexError:
            return False

        result = self.player.move(end, maze)
        if result:
            self.speak(dimensions.get_msg(idx, n))


    def speak(self, text):
        print text


    def show_label(self):
        s, e = self.getxyo()
        l1, l2 = self.dim_names[s], self.dim_names[e]
        label = "%s/%s  f: %s" % (l1, l2, repr(self.player.position))
        label = pyglet.text.Label(
            label,
            x=10,
            y=190,
            font_size=12,
            color=(255,255,255,255),
            anchor_x='left',
            anchor_y='top',
        )
        label.draw()

    def draw_labels(self):
        for cell in self.cells_on_this_floor():
            for wall in filter(lambda w: not self.on_this_floor(w), cell.get_walls()):
                self.mark_wall(wall)
    

    def draw_items(self):
        xidx, yidx = self.getxyo()
        for cell in maze.cells.keys():

            if not self.on_this_floor((cell, cell)):
                continue

            x, y = map(lambda i: i*CELL_SIZE, (cell[xidx], cell[yidx]))
            c = d = 0
            for passage in maze.get_passages(cell):
                if self.on_this_floor(passage):
                    pass
                else:
                    # get the coord that isn't this cell 
                    # FIXME: Can this just always use passage[1] ?
                    other = filter(lambda x: x != cell, passage)[0]
                    # get the dimensional index that differs
                    for idx, v in enumerate(other):
                        if v != cell[idx]:
                            # draw the item
                            sign = "+" if v > cell[idx] else "-"
                            item = "%s%s " % (sign, self.dim_names[idx])
                            Item(x + (c * 20), y - (d * 20), item).draw()
                            c += 14
                            if c > 2:
                                d += 1
                                c = 0
                            break


    def quit(self, *args):
        sys.exit(0)


    def getxyo(self):
        yield self.dim_offs
        if self.dim_offs >= maze.dimensions - 1:
            yield 0
        else:
            yield self.dim_offs+1


    def on_this_floor(self, wall):
        pt1, pt2 = map(list, wall)
        # copy the list
        offst = list(self.player.position)
        x, y = self.getxyo()
        offst[x] = offst[y] = pt1[x] = pt1[y] = pt2[x] = pt2[y] = -1
        return pt1 == pt2 == offst


    def draw_walls(self):
        for wall in filter(self.on_this_floor, maze.walls):
            pt1, pt2 = wall
            pt1 = map(lambda x: x*CELL_SIZE, pt1)
            pt2 = map(lambda x: x*CELL_SIZE, pt2)
            x, y = self.getxyo()
            if pt1[y] == pt2[y]:
                q = Wall(
                    pt1[x] + CELL_SIZE,
                    pt1[y],
                    "horizontal"
                )
            else:
                q = Wall(
                    pt1[x],
                    pt1[y] + CELL_SIZE,
                    "vertical"
                )
            q.draw()


w = MWindow()
pyglet.app.run()
