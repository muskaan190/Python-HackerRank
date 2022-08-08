Sample Input 1

2
2
2
2
Sample Output 1

[[0, 0, 0], [0, 0, 1], [0, 1, 0], [0, 1, 2], [0, 2, 1], [0, 2, 2], [1, 0, 0], [1, 0, 2],[1, 1, 1], [1, 1, 2], [1, 2, 0], [1, 2, 1], [1, 2, 2], [2, 0, 1], [2, 0, 2], [2, 1, 0], [2, 1, 1], [2, 1, 2], [2, 2, 0], [2, 2, 1], [2, 2, 2]]


if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    
    
    lst=[]
    i=0
    j=0
    k=0
   
    for i in range(0,x+1):
        for j in range(0,y+1):
            for k in range(0,z+1):
                t=i+j+k
                if (t==n):
                    None
                else:
                    lst.append([i,j,k])

print(lst)
