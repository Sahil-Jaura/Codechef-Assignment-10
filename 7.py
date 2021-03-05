
from random import randrange
del_arr=[]
ANSWER=[]
def partition(arr,left,right):
    m=left
    pivot_index=randrange(left,right)
    pivot=arr[pivot_index]
    arr[right],arr[pivot_index]=arr[pivot_index],arr[right]
    for i in range(left,right): 

        if (arr[i][0]/arr[i][1]) < (pivot[0]/pivot[1])  :
            arr[i],arr[m]=arr[m],arr[i]
            m+=1 
        if    (arr[i][0]/arr[i][1]) == (pivot[0]/pivot[1]):
            if (arr[i][1]*pivot[1]>0) and (arr[i][0]/arr[i][1]<0) and (pivot[0]/pivot[1]<0) and (abs(arr[i][0])<abs(pivot[0])):
                del_arr.append(pivot)
            if (arr[i][1]*pivot[1]>0) and (arr[i][0]/arr[i][1]<0) and (pivot[0]/pivot[1]<0) and (abs(arr[i][0])>abs(pivot[0])):
                del_arr.append(arr[i])
            if (arr[i][1]*pivot[1]<0) and (arr[i][0]/arr[i][1]<0) and (pivot[0]/pivot[1]<0) and (arr[i][1]>0 and pivot[1]<0):
                del_arr.append(pivot)
            if (arr[i][1]*pivot[1]<0) and (arr[i][0]/arr[i][1]<0) and (pivot[0]/pivot[1]<0) and (arr[i][1]<0 and pivot[1]>0):
                del_arr.append(arr[i])
            if (arr[i][0]/arr[i][1]>0 and pivot[0]/pivot[1]>0) and (arr[i][1]!=0 or pivot[1]!=0) : 
                if arr[i][0]<pivot[0]:
                    del_arr.append(pivot)
                else:
                    del_arr.append(arr[i])               


    arr[m],arr[right]=arr[right],arr[m]
    return m
def quick_sort(arr,left,right):
    if (left>=right):
        return
    pivot_index=partition(arr,left,right)   
    quick_sort(arr,left,pivot_index-1)
    quick_sort(arr,pivot_index+1,right) 
    return 



n = int(input())
arr_strip = list(map(int, input().split()))
arr = []
positive_infinity=[]
negative_infinity=[]
m=0
M=0
for i in range(0, 2*n, 2):
    if arr_strip[i+1]!=0 :
        arr.append((arr_strip[i], arr_strip[i+1]))
    elif arr_strip[i+1]==0 and arr_strip[i]>0:
        m=1
        positive_infinity.append(arr_strip[i])
    elif arr_strip[i+1]==0 and arr_strip[i]<0:
        M=1
        negative_infinity.append(arr_strip[i])
n=10000000000
if len(negative_infinity):
    n=max(negative_infinity)
p=10000000000
if len(positive_infinity):
    p=min(positive_infinity)

arr=set(arr)
arr=list(arr)
arr.sort()       
quick_sort(arr,0,len(arr)-1)    
x=set(del_arr)
LENGTH=len(arr)-len(del_arr)
if n!=10000000000 and p!=10000000000:
    LENGTH+=2
if (n!=10000000000 and p==10000000000) or (p!=10000000000 and n==10000000000):
    LENGTH+=1    
if n!=10000000000:
    ANSWER.append(n)
    ANSWER.append(0)
 
for i in arr:
    if i not in x:
        ANSWER.append(i[0])
        ANSWER.append(i[1])   
if p!=10000000000:
    ANSWER.append(p)
    ANSWER.append(0)
XX=int(len(ANSWER)/2)
print(XX)
for i in ANSWER:
    print(i,end=" ")

