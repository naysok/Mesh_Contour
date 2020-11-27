import rhinoscriptsyntax as rs


class RhinoRenderer():

    def add_point(self, vert):
        
        ### vert = [x0, y0, z0]
        ### vert = point
        
        return rs.AddPoint(vert)


    def add_line(self, vert2):

        ### vert2 = [[x0, y0, z0], [x1, y1, z1]]
        ### vert2 = line

        p0 = rs.AddPoint(vert2[0])
        p1 = rs.AddPoint(vert2[1])
        
        return rs.AddLine(p0, p1)


    def vert3_to_points(self, vert3):
        
        ### vert3 = [[x0, y0, z0], [x1, y1, z1], [x2, y2, z2]]
        ### vert3 = mesh
        
        # print(vert3)

        points = []
        
        for i in xrange(len(vert3)):
            vert = vert3[i]
            # print(vert)
            p = rs.AddPoint(vert)
            points.append(p)
        
        points_geo = rs.coerce3dpointlist(points)
        
        return points_geo
    
    
    def add_mesh(self, verts3):
        
        ### Convert Number-List to Point
        
        ### vert3 = [[x0, y0, z0], [x1, y1, z1], [x2, y2, z2]]
        ### points = [Point3d, Point3d, Point3d]

        points = self.vert3_to_points(verts3)
        print(points)
        
        ### Create Mesh
        m = rs.AddMesh(points, [[0, 1, 2]])
        
        return m
    
    
    def add_meshes(self, meshes):
        
        render = []
        
        for i in xrange(len(meshes)):
            tmp = meshes[i]
            # print(tmp)
            m = self.add_mesh(tmp)
            render.append(m)
        
        return render