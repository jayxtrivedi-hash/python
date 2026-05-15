#----------------------------Tuples-----------------------

#1. tuples are ordered (indexing)
#2. can have duplicacy
#3. are immutable
#4. are heterogenous


#t = ()#Empty tuple
#t = (1,2,3,4,5)
# direct loop
#for i in t:
#    print(i)
# index loop
#for i in range (len(t)):
#    print(i,t[i])

# for index , value in enumerate(t):
#     print(index,value)



#t = (1,2,3,4,5)
#print(t[2])
#printt[1:4]




#t = (1,2,3,4,5)
#methods in tuples
#1. count()-->we can count occurence of a value
#2. index()

#t = (1,2,3,3,3,3,3,2,2,2,4,4,4,4,4,5,5,5,5,6,6,6,6,)
#print(t.count(2))
#print(t.count(3))

#print(t.index(2))
#print(t.index(3))

#t = (1,2,2,2,3,4,5,3,1,4)
#print(3 in t)# membership oprerator
#print(9 in t)

#tuple unpacking
# t = (1,2,3,4,5)
# a,b,c,d,e = t unpacking
# print(a)
# print(b)
# print(c)
# print(d)
# print(e)

#a = 1,2 # this is packing


#------------------------star expression(*)-----------------------

#t = (1,2,3,4,5)
#a,*b,c = t (*k baad ki vale usme daal deta h )
#print(a)
#print(b)
#print(c)

#t = (1,2,3,4,5)
#a,*b,c = t
#print(a)
#print(c)
