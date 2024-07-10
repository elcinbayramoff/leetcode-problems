class Solution:
    def averageWaitingTime(self, customers: list[list[int]]) -> float:
        sum_of_waiting = 0
        current_time = customers[0][0]
        
        
        for i in range(len(customers)):
            if current_time <= customers[i][0]:
                current_time = customers[i][0]
                
            sum_of_waiting += current_time - customers[i][0] + customers[i][1]
            current_time = current_time + customers[i][1]
            
        averagetime = sum_of_waiting/len(customers)
        
        return averagetime
    
solution = Solution()

print(solution.averageWaitingTime([[5,2],[5,4],[10,3],[20,1]]))