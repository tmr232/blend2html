"""HTML Creator

Creates HTML files
"""

def create_face_div(svg_file_path, transform):
    return """<div style=\"-webkit-mask: url({0}) no-repeat;-webkit-transform:matrix3d({1});\"></div>""".format(