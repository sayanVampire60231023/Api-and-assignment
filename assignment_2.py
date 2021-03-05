def intersection(lst1, lst2): 
    return list(set(lst1) & set(lst2)) 
  
# Driver Code 
lst1 = [] 
lst2 = []
n=int(input())
n1=int(input())
for i in range (0,n):
    ele=int(input())
    lst1.append(ele)
    
for i in range (0,n1):
    ele1=int(input())
    lst2.append(ele1)
    
print(intersection(lst1, lst2)) 
