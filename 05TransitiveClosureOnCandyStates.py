from collections import defaultdict
from heapq import *

from FileOperator import FileOperator
states = FileOperator("data/data28.txt").get_data_splitted_by_separator()


class CandyStates(object):

    def __init__(self, data):
        self.number_of_roads = int(data[0])
        self.roads = data[1:((self.number_of_roads*3)+1)]
        self.number_of_roads_to_find = int(data[(self.number_of_roads*3)+1])
        self.roads_to_find = data[((self.number_of_roads*3)+2):(((self.number_of_roads+self.number_of_roads_to_find)*3)+2)]

    def change_to_list_of_roads(self, number, road):
        lists = []
        index = 0
        for i in range(0, number):
            temporary_list = []
            temporary_list.append(road[index])
            temporary_list.append(road[index+2])
            lists.append(temporary_list)
            index += 3
        return lists

    def list_of_roads(self):
        lists = self.change_to_list_of_roads(self.number_of_roads, self.roads)
        index_x = 0
        for x in range(0, len(lists)):
            temporary_list = []
            temporary_list.append(lists[index_x][1])
            temporary_list.append(lists[index_x][0])
            lists.append(temporary_list)
            index_x += 1
        return lists

    def add_step(self):
        lists = self.list_of_roads()
        for x in lists:
            x.append(1)
        return lists

    def list_of_roads_to_find(self):
        return self.change_to_list_of_roads(self.number_of_roads_to_find, self.roads_to_find)


founding = (CandyStates(states).list_of_roads_to_find())
lists = (CandyStates(states).add_step())

"""To jest skopiowane z githuba, bo nie rozumiem dijkstra/algorytmu Floyda-Warshalla,
więc nie ma pojęcia co oznacza ten kod :(, a próbowałam znależć inny sposób na wyliczenie
najkrótszej ścieżki, ale mi się nie udało.."""


def dijkstra(edges, f, t):
    g = defaultdict(list)
    for l, r, c in edges:
        g[l].append((c, r))

    q, seen, mins = [(0, f, ())], set(), {f: 0}
    while q:
        (cost, v1, path) = heappop(q)
        if v1 not in seen:
            seen.add(v1)
            path = (v1, path)
            if v1 == t: return (cost, path)

            for c, v2 in g.get(v1, ()):
                if v2 in seen: continue
                prev = mins.get(v2, None)
                next = cost + c
                if prev is None or next < prev:
                    mins[v2] = next
                    heappush(q, (next, v2, path))

    return float("inf")


if __name__ == "__main__":
    edges = lists
"""I dotąd jest skopiowane, czyli tak właściwie najważniejsze.."""

def results(function):
    all_steps = ""
    for x in range(0, len(function)):
        result = dijkstra(edges, str(function[x][0]), str(function[x][1]))
        steps = result[0]
        all_steps += " " + str(steps)
    return all_steps


print(results(founding))
