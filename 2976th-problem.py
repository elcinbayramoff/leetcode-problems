import math

class Solution:
    def minimumCost(self,source: str, target: str, original: list[str], changed: list[str], cost: list[int]) -> int:
        all_unique = {value: index for index, value in enumerate(set(source) | set(target) | set(original) | set(changed))}  
        dist = [[math.inf]*len(all_unique) for _ in range(len(all_unique))]
        
        for i in range(len(dist)):
            dist[i][i] = 0

        
        for i in range(len(original)):
            dist[all_unique[original[i]]][all_unique[changed[i]]] = min(dist[all_unique[original[i]]][all_unique[changed[i]]],cost[i])
        
        
        for k in all_unique:
            for i in all_unique:
                if dist[all_unique[i]][all_unique[k]] < math.inf:
                    for j in all_unique:
                        if dist[all_unique[k]][all_unique[j]] < math.inf:
                            dist[all_unique[i]][all_unique[j]] = min(dist[all_unique[i]][all_unique[j]], dist[all_unique[i]][all_unique[k]]+dist[all_unique[k]][all_unique[j]])
        res = 0
        for i in range(len(source)):
            if math.isinf(dist[all_unique[source[i]]][all_unique[target[i]]]):
                return -1
            res += dist[all_unique[source[i]]][all_unique[target[i]]]

        return res