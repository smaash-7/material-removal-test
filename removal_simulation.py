from __future__ import absolute_import, division, print_function
from turtle import color
import pymesh
import meshcat.geometry as g
import time
import meshcat
import trimesh


box_trim = trimesh.creation.box(extents=[10,10,4])
tool = trimesh.creation.cylinder(radius= 1, height=5)

box_mesh = pymesh.form_mesh(box_trim.vertices,box_trim.faces)
tool_mesh = pymesh.form_mesh(tool.vertices,tool.faces)


vis = meshcat.Visualizer().open()

box = meshcat.geometry.TriangularMeshGeometry(box_mesh.vertices, box_mesh.faces)

vis.set_object(box, g.MeshLambertMaterial(color=0x9933ff,reflectivity=0.2, wireframe=True) )




time.sleep(1)

for i in range(0,45):
  tool_mesh =  pymesh.form_mesh(tool_mesh.vertices + [[0.1, 0, 0]], tool_mesh.faces)
  box_mesh = pymesh.boolean(box_mesh, tool_mesh, operation="difference",engine="cgal")
  box = meshcat.geometry.TriangularMeshGeometry(box_mesh.vertices, box_mesh.faces)
  #time.sleep(0.1)

  vis.delete()
  vis.set_object(box, g.MeshLambertMaterial(color=0x9933ff,reflectivity=0))
  

tool_mesh =  pymesh.form_mesh(tool_mesh.vertices + [[0, 0, 1]], tool_mesh.faces)

for i in range(0,20):
  tool_mesh =  pymesh.form_mesh(tool_mesh.vertices + [[0, 0.1, 0]], tool_mesh.faces)
  box_mesh = pymesh.boolean(box_mesh, tool_mesh, operation="difference",engine="cgal")
  
  box = meshcat.geometry.TriangularMeshGeometry(box_mesh.vertices, box_mesh.faces)
  
  #time.sleep(0.1)

  vis.delete()
  vis.set_object(box, g.MeshLambertMaterial(color=0x9933ff,reflectivity=0))
  
 



vis.wait()


