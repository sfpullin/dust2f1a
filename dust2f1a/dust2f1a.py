import pyvista as pv
import os

def convert(input, output_dir):
    
    if output_dir == None:
        output_dir = "./"

    reader = pv.get_reader(input)

    mesh = reader.read()

    quad = mesh.extract_cells_by_type(9)
    tri = mesh.extract_cells_by_type(5)

    merged = quad.merge(tri)

    merged.save(output_dir + input)

