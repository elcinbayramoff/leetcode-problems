class Solution:
    def survivedRobotsHealths(self, positions: List[int], healths: List[int], directions: str) -> List[int]:
        res = []
        for i in sorted(range(len(positions)), key = lambda i: positions[i]):
            if directions[i] == 'R':
                res.append(i)
            else:
                while res and healths[res[-1]] < healths[i]:
                    healths[i] -= 1
                    healths[res.pop()] = 0
                if res:
                    if healths[res[-1]] == healths[i]:
                        healths[res.pop()] = 0
                    else:
                        healths[res[-1]] -= 1
                    healths[i] = 0
        return [h for h in healths if h] 