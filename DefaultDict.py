# In this challenge, you will be given 2 integers, n and m. There are n words, which might repeat, in word group A. There are m words belonging to word group B . For each m words, check whether the word has appeared in group A or not. Print the indices of each occurrence of m in group A. If it does not appear, print -1.


a,b=input().split(" ")
x=int(a)
y=int(b)
arr1=[]
arr2=[]

for i in range(0,x):
    n=input()
    arr1.append(n)

# print(arr1)
i=0

for i in range(0,y):
    n=input()
    arr2.append(n)

# print(arr2)

final=""
# print(x,y)
for i in range(0,y):
  final=""
  for j in range(0,x):
    if(arr1[j]==arr2[i]):
      final=final+str(j+1)+" "
  # print(i)
  if arr2[i] not in arr1:
    final=-1
  print(final)
