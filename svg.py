"""SVG Creator

This module handles the creation of SVG files for use in the presentation.
"""
from collections import namedtuple

Point = namedtuple('Point', ['x', 'y'])

def verts_to_svglist(verts):
    return " ".join("{0},{1}".format(vert.x, vert.y) for vert in verts)


class Polygon:
    def __init__(self, vertices, style=None):
        self._vertices = vertices
        self._style = style or ""
        
    def __str__(self):
        return "<polygon points=\"{0}\" style=\"{1}\"/>".format(verts_to_svglist(self._vertices), self._style)
        
def create_svg(elements):
    return """<svg xmlns="http://www.w3.org/2000/svg" version="1.1">
    {0}
    </svg>""".format("\n".join(str(element) for element in elements))
    
if __name__ == "__main__":
    p = Polygon((Point(0,0), Point(0, 100), Point(100, 100), Point(100, 0)))
    print(create_svg([p]))