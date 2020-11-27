import rhinoscriptsyntax as rs


class RhinoRenderer():

    """

    Defined

    ### point
    vert = [x0, y0, z0]
    
    ### line
    vert2 = [[x0, y0, z0], [x1, y1, z1]]
    
    ### mesh
    vert3 = [[x0, y0, z0], [x1, y1, z1], [x2, y2, z2]]
    
    """


    def add_point(self, vert):
        
        return rs.AddPoint(vert)


    def add_line(self, vert2):

        p0 = rs.AddPoint(vert2[0])
        p1 = rs.AddPoint(vert2[1])
        
        return rs.AddLine(p0, p1)


    def vert3_to_points(self, vert3):
                
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