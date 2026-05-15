# ------------------Sets------------------------------
# unordered (no indexing) 
# semi-multiple (can add, but cannot change or remove)
# Heterogeneous (Can contain different data types )

#---------------------Creating a set---------------------
# a = [] 
# b = {}
# c = set ()# types conversion


# # s = set 3 empty set 
# s = {1,2,3,4 ,4,5,4}
# print (type(s))

















#1. add()# for adding single element/value
#s= {1,2,3,4,5,6,3,5}
#s.add(6)

#2.update()# for adding multiple element/value
#s.update([6,7,8,9])
#print(s)

#3.remove()# if the value is not exist we will get an error
#s.remove(1)
#print(s)

#4.discard()
#s.discard
#print(s)

#5.pop()
#print (s.pop())# removes first elelment from the set

#6.clear()# removes all the elements and gives us an empty set
#s.clear()
#print(s)


# 1. intersection
# 2. union
# 3. differece
# 4. symmetric difference

#s1 = {1,2,3,4}
#s2 = {2,3,4,6}
#print(f"intersection :{s1.intersection(s2)}")
#print (f'union:{s1.union(s2)}')
#perimt (f"difference :{s1.difference(s2)}")