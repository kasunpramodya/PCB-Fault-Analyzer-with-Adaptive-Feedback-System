# import dxf2svg
import os


# if os.path.exists(file):
#     os.remove(file)
# dxf2svg(file, "test.svg")

from dxf2svg.pycore import save_svg_from_dxf, extract_all
dxffilepath="test 3-B_Cu.dxf"
# from dxf2svg import dxf2svg
save_svg_from_dxf(dxffilepath, svgfilepath=None, frame_name=None, size=300)
# extract_all(dxffilepath, size=300)