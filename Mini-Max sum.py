# Given five positive integers, find the minimum and maximum values that can be calculated by summing exactly four of the five integers. Then print the respective minimum and maximum values as a single line of two space-separated long integers.

def miniMaxSum(arr):
    n=len(arr)
    sum=0
    final=[]
    for i in range(n):
        sum=sum+arr[i]

    for i in range(n):
        final.append(sum-arr[i])

    print(min(final),max(final))
