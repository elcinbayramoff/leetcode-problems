
class Solution:
    def findTheCity(self,n: int, edges: list[list[int]], distanceThreshold: int) -> int:
        distance_matrix = [[10**4 +1]*n for _ in range(n)]
        
        for i in range(n):
            distance_matrix[i][i] = 0
        
        for i in edges:
            _from, _to, _weight = i
            distance_matrix[_from][_to] = _weight
            distance_matrix[_to][_from] = _weight
            
        for k in range(n):
            for i in range(n):
                for j in range(n):
                    distance_matrix[i][j] = min(distance_matrix[i][j], distance_matrix[i][k] + distance_matrix[k][j])
        
        min_city =   n
        res = -1
        for i in range(n):
            sumof = 0
            for j in range(n):
                if distance_matrix[i][j] <= distanceThreshold:
                    sumof +=1
            if sumof <= min_city:
                min_city = sumof
                res = i
        return res