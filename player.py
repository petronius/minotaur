
import krushal

import pyglet

class Player(object):
    def __init__(self, position, cz):
        self.position = position
        self.cell_size = cz # for drawing

    def draw(self, xidx, yidx):
        pt1 = map(lambda x: x*self.cell_size+5, self.position)
        pt2 = map(lambda x: x+ self.cell_size - 10, pt1)

        x1, y1 = pt1[xidx], pt1[yidx]
        x2, y2 = pt2[xidx], pt2[yidx]

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
            ('c3B', (
                0, 0, 255,
                0, 0, 255,
                0, 0, 255,
                0, 0, 255,
            )),
        )
        self.verts.draw(pyglet.gl.GL_QUADS)

    def move(self, new_pos, maze):

        if not maze.in_bounds(new_pos):
            return False

        w = krushal.Wall.normalize(self.position, new_pos)
        if w in maze.walls:
            return False
        else:
            self.position = new_pos
            return True
