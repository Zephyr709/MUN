# COMP 2002
# Oct 2023

import matplotlib.pyplot as plt
from pathlib import Path
import csv

def map_render(vertexes, lines, pos_x=1500, pos_y=-3000, radius=250, highlighted=[]):
    """
    Draws the map given by the set of vertexes and line segments.

    Vertexes is assumed to be a list of (x, y) tuples.

    Lines is assumed to be a list of vertex tuples. That is, each line is
    specified by the pair of vertexes, with the position of each vertex stored
    in the vertex list.

    A circle with some radius can be drawn around a point given by pos_x and pos_y.

    Vertexes can be highlighted by passing in a list of (x, y) tuple positions to
    the argument highlighted (this should be the output of your find_neaby_vertexes).

    Returns a Matplotlib figure object and also saves it to level.pdf.
    """
    fig, ax = plt.subplots(figsize=(15, 15))

    for line in lines:
        x0, y0 = vertexes[line[0]]
        x1, y1 = vertexes[line[1]]
        ax.plot([x0, x1], [y0, y1], color='black')

        if vertexes[line[0]] in highlighted or vertexes[line[1]] in highlighted:
            x0, y0 = vertexes[line[0]]
            x1, y1 = vertexes[line[1]]
            ax.plot([x0, x1], [y0, y1], color='red', linewidth=2)

    ax.scatter(pos_x, pos_y, marker='*', s=500, color='#880000')
    circle = plt.Circle((pos_x, pos_y), radius, fill=False, linewidth=3, linestyle='--', color='#880000')
    ax.add_patch(circle)
    # sns.despine(ax=ax, left=True, bottom=True)

    for spine in ['right', 'top', 'left', 'bottom']:
        ax.spines[spine].set_visible(False)

    ax.set_xlim((-1000, 4000))
    ax.set_ylim((-6000, -1000))

    ax.set_xticks([])
    ax.set_yticks([])

    fig.tight_layout()
    fig.savefig('level.pdf')

    return fig


def read_map_data(vertex_csv = Path("C:/Users/jager/OneDrive/Documents/GitHub/MUN/comp-2002/Assignment-3/vertexes.csv"), lines_csv = Path("C:/Users/jager/OneDrive/Documents/GitHub/MUN/comp-2002/Assignment-3/lines.csv")):
    """
    Reads the vertex and line data from csv files.

    Returns a list of (x, y) tuples representing the vertexes, and a list
    of (vertex, vertex) tuples representing line segments connecting two
    vertexes.
    """
    vertexes = []
    lines = []

    with open(vertex_csv) as csvfile:
        vertexes_reader = csv.reader(csvfile)
        for row in vertexes_reader:
            vertexes.append((int(row[0]), int(row[1])))

    with open(lines_csv) as csvfile:
        lines_reader = csv.reader(csvfile)
        for row in lines_reader:
            lines.append((int(row[0]), int(row[1])))

    return (vertexes, lines)

if __name__ == '__main__':
    (vertexes, lines) = read_map_data()
    fig = map_render(vertexes,lines)