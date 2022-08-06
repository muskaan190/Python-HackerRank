# Given an array of integers, calculate the ratios of its elements that are positive, negative, and zero. Print the decimal value of each fraction on a new line with  places after the decimal.

def plusMinus(arr):
    pos=0.0
    neg=0.0
    neutral=0.0
    n=len(arr)
    for x in arr:
        if x>0:
            pos=pos+1
        elif x<0:
            neg=neg+1
        else:
            neutral=neutral+1
    
    print(float(pos/n))
    print(float(neg/n))
    print(float(neutral/n))
