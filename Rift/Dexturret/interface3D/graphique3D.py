from direct.showbase.ShowBase import ShowBase
from direct.task import Task
from direct.actor.Actor import Actor
from direct.interval.IntervalGlobal import Sequence
from panda3d.core import Geom,GeomTriangles,GeomVertexWriter,GeomVertexFormat,GeomVertexData,TransparencyAttrib,Point3,Vec4

from panda3d.core import Geom, GeomTriangles, GeomVertexWriter, GeomVertexFormat, GeomVertexData, NodePath, GeomNode, GeomVertexReader

class VueRobot(ShowBase):
    def __init__(self):
        super().__init__()

        # Coordonnées des sommets du rectangle 3D
        vertices = [
            (-1, -1, -1),  # sommet 0
            (1, -1, -1),   # sommet 1
            (1, 1, -1),    # sommet 2
            (-1, 1, -1),   # sommet 3
            (-1, -1, 1),   # sommet 4
            (1, -1, 1),    # sommet 5
            (1, 1, 1),     # sommet 6
            (-1, 1, 1),    # sommet 7
        ]

        # Normales des sommets du rectangle 3D
        normals = [
            (-1, -1, -1),  # normal du sommet 0
            (1, -1, -1),   # normal du sommet 1
            (1, 1, -1),    # normal du sommet 2
            (-1, 1, -1),   # normal du sommet 3
            (-1, -1, 1),   # normal du sommet 4
            (1, -1, 1),    # normal du sommet 5
            (1, 1, 1),     # normal du sommet 6
            (-1, 1, 1),    # normal du sommet 7
        ]

        # Couleurs des sommets du rectangle 3D
        colors = [
            (1, 0, 0, 1),  # couleur du sommet 0 (rouge)
            (0, 1, 0, 1),  # couleur du sommet 1 (vert)
            (0, 0, 1, 1),  # couleur du sommet 2 (bleu)
            (1, 1, 0, 1),  # couleur du sommet 3 (jaune)
            (1, 0, 1, 1),  # couleur du sommet 4 (magenta)
            (0, 1, 1, 1),  # couleur du sommet 5 (cyan)
            (1, 1, 1, 1),  # couleur du sommet 6 (blanc)
            (0, 0, 0, 1),  # couleur du sommet 7 (noir)
        ]

        # Indices des triangles du rectangle 3D
        indices = [
            (0, 1, 2), (0, 2, 3),  # face avant
            (4, 5, 6), (4, 6, 7),  # face arrière
            (0, 1, 5), (0, 5, 4),  # face bas
            (2, 3, 7), (2, 7, 6),  # face haut
            (0, 3, 7), (0, 7, 4),  # face gauche
            (1, 2, 6), (1, 6, 5),  # face droite
        ]

        # Créer le format des vertices
        format = GeomVertexFormat.getV3n3c4()  # 3D vertices, normals, and colors
        vdata = GeomVertexData('vertices', format, Geom.UHStatic)

        # Créer les vertices
        vertex = GeomVertexWriter(vdata, 'vertex')
        normal = GeomVertexWriter(vdata, 'normal')
        color = GeomVertexWriter(vdata, 'color')

        # Ajouter les vertices du rectangle 3D
        for i in range(8):
            vertex.addData3f(vertices[i])
            normal.addData3f(normals[i])
            color.addData4f(colors[i])

        # Créer le GeomTriangles
        triangles = GeomTriangles(Geom.UHStatic)

        # Ajouter les triangles du rectangle 3D
        for i in range(12):
            triangles.addVertices(*indices[i])
            triangles.closePrimitive()

        # Créer le Geom et ajouter les triangles
        geom = Geom(vdata)
        geom.addPrimitive(triangles)

        # Créer le GeomNode et ajouter le Geom
        node = GeomNode('rectangle')
        node.addGeom(geom)

        # Créer le NodePath et ajouter le GeomNode
        rectangle3D_node = self.render.attachNewNode(node)

        # Changer la couleur du rectangle 3D
        rectangle3D_node.setColor(1, 0, 0, 1)  # rouge
        
        # Déplacer la caméra pour qu'elle pointe vers le rectangle 3D
        self.camera.lookAt(rectangle3D_node)

        
            
app=VueRobot()
app.run()