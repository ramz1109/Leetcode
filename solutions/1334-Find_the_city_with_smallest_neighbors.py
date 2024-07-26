from typing import List
from math import inf
from heapq import heappop, heappush
from collections import defaultdict

class Solution:
    def findTheCity(self, n: int, edges, distanceThreshold):

        def dijkstras(source: int):
            distances = [inf] * n
            distances[source] = 0
            heap = [(0, source)]
            while heap:
                curr_dist, node = heappop(heap)
                if curr_dist > distances[node]:
                    continue
                for nei, weight in graph[node]:
                    dist = curr_dist + weight
                    if dist < distances[nei]:
                        distances[nei] = dist
                        heappush(heap, (dist, nei))
            _return = 0
            for i in range(n):
                if i != source and distances[i] <= distanceThreshold:
                    _return += 1
            return _return

        graph = defaultdict(list)
        for _from, _to, _weight in edges:
            graph[_from].append((_to, _weight))
            graph[_to].append((_from, _weight))

        _node = None
        _cities = None
        for i in range(n):
            curr = dijkstras(source=i)
            if _node is None or curr < _cities or (curr == _cities and _node < i):
                _node = i
                _cities = curr

        return _node