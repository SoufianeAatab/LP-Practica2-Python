import math
import random
from PIL import Image, ImageDraw


class ConvexPolygon:
    # @brief constructor
    # @params ini_vertices a list of vertices to construct the polygon
    def __init__(self, ini_vertices):
        self.vertices = ini_vertices
        self.vertices = self.__hull()
        self.edges = self.__edges()
        self.color = [0, 0, 0]

    # @brief returns the list of vertices of the polygon in clockwise order
    # PRE: compute the convex hull
    def get_vertices(self):
        return self.vertices

    # @brief returns a list with edges of the polygon
    # PRE: compute the convex hull
    def get_edges(self):
        return self.edges

    # @brief returns number of vertices
    # PRE: compute the convex hull
    def get_n_vertices(self):
        return len(self.vertices)

    # @brief returns number of edges
    # PRE: compute the convex hull
    def get_n_edges(self):
        return len(self.edges)

    # @brief returns the perimeter of the polygon
    # PRE: compute the convex hull and edges method
    def perimeter(self):
        p = 0
        for e in self.edges:
            p = p + self.__length(e)

        return p

    # @brief: returns the list with the vertices in clockwise order
    def get_hull(self):
        return self.vertices

    # @brief returns the area of the polygon
    # PRE: compute the convex hull
    def area(self):
        area = 0
        for i in range(len(self.vertices)):
            j = (i+1) % len(self.vertices)
            area = area + self.__cross(self.vertices[j], self.vertices[i])
        return area * 0.5

    # @brief: Check whether the point a is inside the polygon or not
    # returns 0 if the point lies on an edge of the polygon
    # returns 1 if the point lies inside the polygon
    # return -1 if the point lies outside the polygon
    # PRE: compute convex hull
    def contains(self, a):
        side = None
        for i in range(len(self.vertices)):
            v = self.vertices[i]
            vnext = self.vertices[(i+1) % len(self.vertices)]
            nside = self.__orientation(v, vnext, a)
            if nside == 0:
                return 0
            if side is None:
                side = nside
            elif side != nside:
                return -1
        return 1

    # @brief: check whether polygon A lies inside polygon B,
    # Check if polygon A(self) contains all vertices of polygon B
    def inside(self, B):
        side = None
        for v in B.get_vertices():
            nside = self.contains(v)
            if side is None:
                side = nside
            elif side != nside:
                return 'no'
        return 'yes'

    # @brief Compute the intersection of two polygons and returns a new polygon
    # with the vertices of the intersection
    # Inspired by Sutherland-Hodgman polygon clipping
    def intersection(self, p2):
        clipPolygon = p2.get_vertices()

        def inside(p):
            return(cp2[0]-cp1[0])*(p[1]-cp1[1]) <= (cp2[1]-cp1[1])*(p[0]-cp1[0])

        # @brief: Compute the intersection between 2 points
        def computeIntersection():
            dc = [cp1[0] - cp2[0], cp1[1] - cp2[1]]
            dp = [s[0] - e[0], s[1] - e[1]]
            n1 = cp1[0] * cp2[1] - cp1[1] * cp2[0]
            n2 = s[0] * e[1] - s[1] * e[0]
            n3 = 1 / (dc[0] * dp[1] - dc[1] * dp[0])
            return (int((n1*dp[0] - n2*dc[0]) * n3), int((n1*dp[1] - n2*dc[1]) * n3))

        outputList = self.vertices
        cp1 = clipPolygon[-1]
        for clipVertex in clipPolygon:
            cp2 = clipVertex
            inputList = outputList
            outputList = []

            if len(inputList) > 0:
                s = inputList[-1]
            else:
                return ConvexPolygon([])

            for subjectVertex in inputList:
                e = subjectVertex
                if inside(e):
                    if not inside(s):
                        outputList.append(computeIntersection())
                    outputList.append(e)
                elif inside(s):
                    outputList.append(computeIntersection())
                s = e
            cp1 = cp2
        return ConvexPolygon(outputList)

    # @brief: Compute and returns a new polygon with the union of two polygons A and B
    @staticmethod
    def union(A, B):
        # [:] copy by value not by reference
        nv = A.vertices[:]
        for v in B.get_vertices():
            if v not in nv:
                nv.append(v)
        return ConvexPolygon(nv)

    # @brief: Check whether the polygon is regular or not, (all edges same length)
    def is_regular(self):
        len_edge = __length(edges[0])
        for v in edges:
            if len_edge != __length(v):
                return 'no'
        return 'yes'

    # @brief: Compute the centroid of the polygon
    def centroid(self):
        size = len(self.vertices)
        if size > 0:
            x, y = 0, 0
            for xs, ys in self.vertices:
                x += xs
                y += ys
            return ((round(x/size, 3), round(y/size, 3)))
        else:
            return None

    # @brief check if the two polygons are equal(same vertices both)
    def equal(self, p):
        if p.get_vertices() == self.vertices:
            return 'yes'
        else:
            return 'no'

    # @brief returns an integer that represents the orientation of a point with respect to an edge
    # We obtain the edge that goes from A to B and we calculate the cross product with C
    # If the result is a positive number, c is to the left of the edge
    # If the result is a negative number, c is to the right of the edge
    # Otherwise the edge contains point c
    # @params: a, b, c vertices
    def __orientation(self, a, b, c):
        ab = self.__sub(a, b)
        ac = self.__sub(a, c)
        v = self.__cross(ab, ac)
        if v > 0:
            return 1
        elif v < 0:
            return -1
        else:
            return 0

    # @brief computes the cross product of two points
    # v⃗ × w⃗ > 0: w⃗  is to the left of v
    # v⃗ × w⃗ < 0: w⃗  is to the right o v
    # v⃗ × w⃗ = 0: w⃗  and v⃗  are aligned
    def __cross(self, a, b):
        return a[0] * b[1] - a[1] * b[0]

    # @brief Computes the vector that goes from b to a
    # @params: a, b points
    def __sub(self, a, b):
        return (b[0] - a[0], b[1]-a[1])

    # @brief Returns the edges of the polygon
    def __edges(self):
        edges = []
        for i in range(len(self.vertices)):
            v = self.vertices[i]
            vnext = self.vertices[(i+1) % len(self.vertices)]
            edges.append(self.__sub(v, vnext))
        return edges

    # @brief returns the length of a vector A
    def __length(self, a):
        return math.sqrt(a[0]**2 + a[1]**2)

    # @brief computes convex hull of the polygon
    def __hull(self):
        h = []
        n = len(self.vertices)
        if n > 0:
            z = self.vertices[0]
            left = 0
            for i in range(n):
                if self.vertices[i][0] < self.vertices[left][0]:
                    z = self.vertices[i]
                    left = i
            p = left
            while True:
                if self.vertices[p] not in h:
                    h.append(self.vertices[p])
                q = (p + 1) % n
                for i in range(n):
                    orientation = self.__orientation(self.vertices[p], self.vertices[q], self.vertices[i])
                    if orientation > 0:  # cross product > 0 => is at left of
                        q = i
                p = q
                if p == left:
                    break
        return h

    # @brief computes the box with the smallest measure within which all the points of the polygon lie
    def boundingbox(self):
        minX = float('inf')
        minY = float('inf')
        maxX = float('-inf')
        maxY = float('-inf')

        for i in range(len(self.vertices)):
            vertex = self.vertices[i]
            minX = min(minX, vertex[0])
            maxY = max(maxY, vertex[1])
            maxX = max(maxX, vertex[0])
            minY = min(minY, vertex[1])
        return [(minX, minY), (minX, maxY), (maxX, maxY), (maxX, minY)]

    # @brief generate a convex polygon with n vertices
    # @params Integer n
    @staticmethod
    def generate(n):
        vList = []
        for i in range(n):
            vList.append(tuple((random.uniform(0, 1), random.uniform(0, 1))))
        return ConvexPolygon(vList)

    # @brief attach the given color to the polygon
    def set_color(self, color):
        self.color = color

    # @brief returns the color of the polygon
    def get_color(self):
        return (self.color[0], self.color[1], self.color[2])

    # @brief Generate a image and draw the list of polygons that receive as parameter
    # @params List of polygons, String image file name
    @staticmethod
    def draw(polygons, filename):
        # @brief auxiliar function that scales the point A to 398px
        def px(a, max):
            return a * 398 / max

        img = Image.new('RGB', (400, 400), 'White')
        dib = ImageDraw.Draw(img)
        for p in polygons:
            maxX = float('-inf')
            maxY = float('-inf')
            for v in p.get_vertices():
                maxX = max(maxX, v[0])
                maxY = max(maxY, v[1])
        for p in polygons:
            vertices = []
            for x, y in p.get_vertices():
                vertices.append((px(x, maxX), 398-px(y, maxY)))
            dib.polygon(vertices, 'White', p.get_color())
        img.save(filename)
        return filename
