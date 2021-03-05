#Given a non-empty array of integers, every element appears twice except for one. Find that single one.

def findSingle( ar, n):
	
        res = ar[0]
	
    
        for i in range(1,n):
            res = res ^ ar[i] #(2^2)=0 (1^0)=1
	
        return res


ar = [2, 2,1]#[4,2,2,1,2]
print(findSingle(ar, len(ar)))

