def max_val(arr):
    max_val=arr[0]
    for num in arr[1:]:
        if num>max_val:
            max_val=num
    return max_val
def count_sort(arr,pos):
    n=len(arr)
    count=[0]*10
    output=[0]*n
    for num in arr:
        index=(num//pos)%10
        count[index]+=index
    for i in range(1,10):
        count[i]=count[i]+count[i-1]
    for num in reversed(arr):
        index=(num//pos)%10
        output[count[index]-1]=num
        count[index]-=index
    for i in range(n):
        arr[i]=output[i]
def radix_sort(arr):
    maximum_val=max_val(arr)
    pos=1
    while max_val//pos>0:
        count_sort(arr,pos)
        pos*=10
def print(arr):
    for num in arr:
        print(num,end=" ")
n=int(input("enter the size:"))
arr=[]
for _ in range(n):
    arr.append(int(input()))
radix_sort(arr)
print(arr)

