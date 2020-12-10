from . import line_plane_intersection, stl_parser
# reload(line_plane_intersection)
reload(stl_parser)
lp = line_plane_intersection.LinePlaneIntersection()
sp = stl_parser.StlParser()


class RunMeshContour():


    def read_meshes(self, file_path):

        meshes_parsed = sp.stl2meshes(file_path)
        ranges_meshes = sp.meshes_z_range(meshes_parsed)

        return meshes_parsed, ranges_meshes


    def fillter_mesh(self, meshes, ranges, height):

        mesh_filtered = []

        for i in range(len(meshes)):
            m = meshes[i]
            r = ranges[i]
            r_min = r[0]
            r_max = r[1]

            if (r_min < height) and (height < r_max):
                mesh_filtered.append(m)

        return mesh_filtered


    def set_mesh(self, file_path):

        meshes, ranges = self.read_meshes(file_path)
        return meshes, ranges


    def run_contour(self, meshes, ranges, height):

        meshes_filtered = self.fillter_mesh(meshes, ranges, height)

        lines = lp.calc_meshes_plane_intersection(meshes_filtered, height)
        return meshes_filtered, lines
