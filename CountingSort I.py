# Complete the countingSort function in the editor below.

# countingSort has the following parameter(s):
# arr[n]: an array of integers
# Returns
# int[100]: a frequency array

def countingSort(arr):
    a=[]
    a=[0 for i in range(100)]
    for i in arr:
        if a[i] in a:
            a[i]=a[i]+1
        else:
            a[i]=1
  
    return a
