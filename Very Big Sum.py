# In this challenge, you are required to calculate and print the sum of the elements in an array, keeping in mind that some of those integers may be quite large.

def aVeryBigSum(ar):
    sum=0
    for x in ar:
        sum=sum+x
    return sum
