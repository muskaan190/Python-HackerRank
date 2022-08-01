# Given an integer, , perform the following conditional actions:

# If n is odd, print Weird
# If n is even and in the inclusive range of 2 to 5 , print Not Weird
# If n is even and in the inclusive range of 6 to 20, print Weird
# If n is even and greater than 20 , print Not Weird



import math
import os
import random
import re
import sys

lst=list(range(2,6))
lst2=list(range(6,21))
n=int(input())
if(n%2!=0):
    print("Weird")
else:
    if(n in lst):
        print("Not Weird")
    elif(n in lst2):
        print("Weird")
    else:
        print("Not Weird")
