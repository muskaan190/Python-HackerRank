# Raghu is a shoe shop owner. His shop has X number of shoes.
# He has a list containing the size of each shoe he has in his shop.
# There are N number of customers who are willing to pay x amount of money only if they get the shoe of their desired size.
# Your task is to compute how much money Raghu earned.



num_of_shoes=int(input())
shoe_sizes=input().split(" ")
num_of_customers=int(input())
arr=[]
for i in range(0,num_of_customers):
    n=input().split(" ")
    arr.append(n)

cust_shoe_sizes=[]
cust_prices=[]
for i in range(0,num_of_customers):
  cust_shoe_sizes.append(arr[i][0])

# print(cust_shoe_sizes)

for i in range(0,num_of_customers):
  cust_prices.append(arr[i][1])

# print(cust_prices)
j=0
sum=0
for i in cust_shoe_sizes:
  if i in shoe_sizes:
    shoe_sizes.remove(i)
    sum=sum+int(cust_prices[j])
    j=j+1
  else:
    j=j+1

print(sum)
