# Definition for singly-linked list.
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

'''
class Solution: # first submission runtime 973ms
    def mergeNodes(self, head: ListNode):
        value = 0
        status = False
        result = []
        def listtonode(arr):
            listnode = ListNode(arr[0])
            current = listnode
            for i in arr[1:]:
                current.next = ListNode(i)
                current = current.next
            return listnode
        
        while head != None:
            
            while head.val != 0:
                value += head.val
                head = head.next
                status = True
            if status:
                result.append(value)
            head = head.next
            value, status = 0, False
        return listtonode(result)

'''
'''
class Solution: #Second submission runtime 1223ms
    def mergeNodes(self, head: ListNode) -> ListNode:
        value = 0
        status = False
        result = ListNode(0)
        current = result
        while head != None:
            
            while head.val != 0:
                value += head.val
                head = head.next
                status = True
            if status:
                current.next = ListNode(value)
                print(value)
                current = current.next
            head = head.next
            value, status = 0, False
        return result.next
'''


class Solution: #Last and best submission 943 ms
    def mergeNodes(self, head: ListNode) -> ListNode:
        value = 0
        result = ListNode(0)
        current = result
        head = head.next
        while head != None:
            if head.val != 0:
                value += head.val
            else:
                current.next = ListNode(value)
                value = 0
                current = current.next
            head = head.next
        return result.next
    
    



solution = Solution()
head = [0,3,1,0,4,5,2,0]
listnode = listtonode(head)
print(nodetolist(solution.mergeNodes(listnode)))