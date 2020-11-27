import sys


from . import calc_vector
reload(calc_vector)
cv = calc_vector.CalcVector()


class LinePlaneIntersection():


    def calc_line_plane_intersection(self, line, height):

        ### line = [[x0, y0, z0], [x1, y1, z1]]
        ### height = value (Z-Pos)

        ### Ray Triangle Intersection
        ### https://pheema.hatenablog.jp/entry/ray-triangle-intersection

        p0 = line[0]
        p0_p1 = cv.vector_add(line[1], cv.vector_reverse(line[0]))

        o = p0
        d = p0_p1
        v0 = [0, 0, height]
        v1 = [10, 0, height]
        v2 = [0, 10, height]

        e1 = cv.vector_subtract(v1, v0)
        e2 = cv.vector_subtract(v2, v0)

        ### https://qiita.com/ikuzak/items/1332625192daab208e22
        kEpsilon = sys.float_info.epsilon

        alpha = cv.vector_cross(d, e2)
        det = cv.vector_dot(e1, alpha)

        # print(alpha)
        # print(det)

        ### (1) Check Parallel
        if (-kEpsilon < det) and (det < kEpsilon):
            # print("Parallel")
            return None
        
        det_inv = 1.0 / det
        r = cv.vector_subtract(o, v0)

        ### (2) Calc u-Value
        u = cv.vector_dot(alpha, r) * det_inv

        beta = cv.vector_cross(r, e1)

        ### (3) Clac v-Value
        v = cv.vector_dot(d, beta) * det_inv

        ### (4) Check t_value (t >= 0)
        t = cv.vector_dot(e2, beta) * det_inv
        if (t < 0.0) or (t > 1.0):
            return None

        ### Intersett : True !!
        # intersect_val = [t, u, v]

        ### Barycenrinc_Coordinate >> XYZ
        ### ((1 - u - v) * v0) + (u * v1) + (v * v2)
        new_v0 = cv.vector_multiplicate(v0, (1.0 - u - v))
        new_v1 = cv.vector_multiplicate(v1, u)
        new_v2 = cv.vector_multiplicate(v2, v)
        
        intersect_pos = cv.vector_add_3(new_v0, new_v1, new_v2)

        return intersect_pos
    

    def calc_mesh_plane_intersection(self, mesh, height):

        ### mesh = [[x0, y0, z0], [x1, y1, z1], [x2, y2, z2]]
        ### height = value (Z-Pos)

        result = []

        line_0 = [mesh[0], mesh[1]]
        line_1 = [mesh[0], mesh[2]]
        line_2 = [mesh[1], mesh[2]]

        r0 = self.calc_line_plane_intersection(line_0, height)
        r1 = self.calc_line_plane_intersection(line_1, height)
        r2 = self.calc_line_plane_intersection(line_2, height)

        if r0 != None:
            result.append(r0)
        if r1 != None:
            result.append(r1)
        if r2 != None:
            result.append(r2)

        return result