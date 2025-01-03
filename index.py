# addition
list=[1,5.6,8.4,58,63,42,87,-50,53]
sum=0
count=0
for i in list:
 sum =sum+i
 count=count+1
print(sum) 

# average
if count==0:
  print("empty list")
else:
 print(sum/count)

list2=[[1,54,6],[45,-12,78],[],[32,-61,94]]
sum=0
count=0
for i in list2:
    # print(i)
  for j in i:
    #    print(j)
    sum+=j
    count+=1
print(sum)
print(sum/count)


# functions
def calc_volume(r,pie):
  print("computation started")
  print((4/3)*pie* r*r*r)
  print("computed ended")
calc_volume(10,3.14)
calc_volume(20,3.14)
calc_volume(30,)
calc_volume(40,)



# def add(a,b,c):
#   print(a+b+c)
# add(8,12,80)


def sum(a,b,*c):
  print(c)
  sum=a+b
  for i in c:
    sum+=i
  return sum
sum(21,32,5,9,87,64,31)





