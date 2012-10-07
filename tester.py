"""Tester.py
"""
import sys
sys.path.append("C:\\temp\\blendertest")
from os import path
from random import randint
import math

from blend2data import *
from svg import *

SVG_DIR = "c:\\temp"

if __name__ == "__main__":
    mesh = bpy.context.selected_objects[0].data
    svg_paths = []
    rotations = []
    sizes = []
    names = []
    translations = []
    for index, face in enumerate(mesh.polygons):
        rotation = get_rotation(face.normal)
        flat_face = flatten_face(face, mesh)
        trans = get_3d_location(flat_face)*100
        translations.append(trans)
        verts = relocate_face(flat_face)
        polygon = Polygon([vert * 100 for vert in verts])
        print(verts)
        sizes.append(polygon.get_size())
        svg = create_svg([polygon])
        name = path.join(SVG_DIR, "face_{0}.svg".format(index))
        open(name, "wb").write(svg.encode("ascii"))
        svg_paths.append(name)
        rotations.append(rotation)
        names.append("face_{0}.svg".format(index))
        
    open(path.join(SVG_DIR, "index.html"), "wb").write("""<html>
    <body>
    {0}
    </body>
    </html>
    """.format("\n".join(
        "<div style=\"background-color:{5};position:absolute;\
        -webkit-transform-origin: top left;\
        -webkit-transform-style: preserve-3d;\
        -webkit-transform: rotateZ({1:0.3f}deg) rotateX({0:0.3f}deg) translate3d({6});\
        width:{3:0.3f}px;height:{4:0.3f}px;\
        -webkit-mask:url({2}) no-repeat;\"></div>".format(
            math.degrees(r[0]),
            math.degrees(r[2]), 
            p,
            s[0], 
            s[1],
            ("#{0:02x}{1:02x}{2:02x}".format(randint(0, 256)%0xff,randint(0, 256)%0xff,randint(0, 256)%0xff)),
            "{0:0.3f}px,{1:0.3f}px,{2:0.3f}px".format(t.x,t.y,t.z)
            ) for
        r,p,s,t in zip(rotations,names, sizes,translations))).encode("ascii"))