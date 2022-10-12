# from audioop import reverse


class Item:
    def __init__(self,deadline, profit):
        self.deadline = deadline
        self.profit = profit

def jobsearch_maxprofit(Jobs,n):
    Jobs.sort(key = lambda x : x.profit , reverse=True)
    profit = 0
    count = 0
    result = [False]*100
    # print(Jobs)
    for i in range(0,n):  #0
        for j in range(Jobs[i].deadline-1,-1,-1): 
            if not result[j]:
                result[j] = True
                profit+=Jobs[i].profit
                count+=1
                break
    return [count,profit]
        

A = [Item(2, 100), Item(1, 50), Item(2, 10), Item(1, 20), Item(3,30)];
print(jobsearch_maxprofit(A,len(A)))
