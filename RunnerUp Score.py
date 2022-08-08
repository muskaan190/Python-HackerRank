# Given the participants' score sheet for your University Sports Day, you are required to find the runner-up score. You are given  scores. Store them in a list and find the score of the runner-up.

if __name__ == '__main__':
    n=int(input())
    arr=map(int,input().split())
    new=[]
    a=list(arr)
    mx=a[0]
    for i in range(0,n):
        if a[i]>mx:
            mx=a[i]
    
    for i in range(0,n):
        if a[i]==mx:
            a[i]=-111110
    
    new_max=a[0]
    for i in range(0,n):
        if a[i]>new_max:
            new_max=a[i]
    print(new_max)
