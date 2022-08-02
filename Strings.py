# The included code stub will read an integer,n, from STDIN.
# Without using any string methods, try to print the following:
# 12345...n

if __name__ == '__main__':
    n = int(input())
    lst=list(range(1,n+1))
    a=""
    for i in lst:
        a=a+str(i)
    
    print(a)
