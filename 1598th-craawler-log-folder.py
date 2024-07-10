

''' Using this solution we can also get current path
class Solution:
    def minOperations(self, logs: List[str]) -> int:
        path = ['main']
        
        for i in logs:
            if i == '../' and len(path) > 1:
                path.pop(-1)
            elif '/' in i and ('.' not in i):
                path.append(i.split('/'))
        return len(path) - 1
'''

'''  this is better in memory and time complexity but this is only needed when current path is not necessary
class Solution:
    def minOperations(self, logs: List[str]) -> int:
        path = 0
        
        for i in logs:
            if i == '../':
                if path > 0:
                    path -= 1
            elif i == './':
                pass
            else:
                path += 1
        return path
'''