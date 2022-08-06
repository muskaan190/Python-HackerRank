# Given an array of integers, where all elements but one occur twice, find the unique element.

def lonelyinteger(a):
    while a !=None:
        for i in a:
            count=0
            while i in a:
                a.remove(i)
                count=count+1
            if(count==1):
                return i
  
