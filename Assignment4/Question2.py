# Question 2
# Implement binary search using python language.
# (Write a function which returns the index of x in given array arr if present, else returns -1)

#Answer :::

def binary_search(arr,x,f,l):
    if l >= f:
        mid = f+(l-1)//2
        if arr[mid] == x:
            return mid

        elif arr[mid] > x:
            
            return binary_search(arr,x,f,mid-1)
        else:
            return binary_search(arr,x,mid+1,l)
    else:
        return -1
    

a = list(map(int,input().split(" ")))
x = int(input())
#sorting

for i in range(0,len(a)):
    swaping = 0
    for j in range(0,len(a)-i-1):
        if a[j] > a[j+1]:
            a[j],a[j+1] = a[j+1],a[j]
            swaping = 1
    if swaping == 0:
        break

print(binary_search(a,x,0,len(a)-1))





