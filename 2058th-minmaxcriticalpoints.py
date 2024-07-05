class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
def listtonode(head):
    listnode = ListNode(head[0])
    current = listnode
    for i in head[1:]:
        current.next = ListNode(i)
        current = current.next
    return listnode

def nodetolist(head):
    res = []
    while head != None:
        res.append(head.val)
        head = head.next
    return res


class Solution:
    def nodesBetweenCriticalPoints(self, head: ListNode) -> list[int]:
        count = 1
        res = []
        minimum = 10**5+1
        while head.next != None and head.next.next != None:
            if (head.val < head.next.val and head.next.val > head.next.next.val) or (head.val > head.next.val and head.next.val < head.next.next.val):
                if res and  abs(res[-1]-count) < minimum:
                    minimum = abs(res[-1] - count)
                res.append(count)
            
            count += 1
            head = head.next
        
        if len(res) < 2:
            return [-1,-1]
        maximum = res[-1]-res[0]
        return [minimum, maximum]
    
head = [5,3,1,2,5,1,2]
listnode = listtonode(head)
solution = Solution()
print(solution.nodesBetweenCriticalPoints(listnode))