# Dijkstra’s algorithm.
import math


def argmin(T, s):
    amin = -1
    m = math.inf  # maximum distance
    for i, t in enumerate(T):
        if t < m and i not in s:
            m = t
            amin = i
    return amin


def get_link_v(v, D):
    for i, weight in enumerate(D[v]):
        if weight > 0:
            yield i


D = ((0, 3, 1, 3, math.inf, math.inf),
     (3, 0, 4, math.inf, math.inf, math.inf),
     (1, 4, 0, math.inf, 7, 5),
     (3, math.inf, math.inf, 0, math.inf, 2),
     (math.inf, math.inf, 7, math.inf, 0, 4),
     (math.inf, math.inf, 5, 2, 4, 0))

N = len(D)
print("Number of vertices:", N)

T = [math.inf] * N  # the last row of the table

v = 0  # starting vertex
T[v] = 0  # distance to itself is zero
s = {v}  # set of visited vertices
M = [0] * N  # to store the minimum distances

while v != -1:  # continue until all vertices are visited
    for j in get_link_v(v, D):  # for each vertex connected to v
        if j not in s:
            w = T[v] + D[v][j]  # calculate the distance to j through v
            if w < T[j]:
                T[j] = w
                M[j] = v  # store the previous vertex for path reconstruction

    v = argmin(T, s)  # find the next vertex with the minimum distance
    if v >= 0:
        s.add(v)

start = 0
end = 4

P = [end]
while end != start:
    end = M[P[-1]]
    P.append(end)

print("Minimum distances from vertex", start, "to all others:", T)
print(P)
