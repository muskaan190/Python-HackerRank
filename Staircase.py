# This is a staircase of size n=4 :

   
#    #
#   ##
#  ###

# Complete the staircase function in the editor below.


def staircase(n):
    j=n-1
    for i in range(1,n+1):
        print(" "*j+"#"*i)
        j=j-1
  
