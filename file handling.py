#----------------------file Handling----------date-06/05/29------- 
#file = open('string.py')
#print(file.read())
#file.close()

#modes 

#W - write mode ( 1. agr file created nhi h toh ho jayegi ,2. agr purana data hai toh overwrite ho jayega)
#a - append mode
#x - creat mode
#r - creat mode

# file = open ('himawari.txt','r')

# for i in file:
#     print(i)
# file.close()    


#with statement
# with open('himawari.txt','r')as file:
#     print(file.read())

# with open('himawari.txt','w')as file:
#     file.write('content overwritten')
#     print('karya pura hua(done)')

#--------------------Path-------------------
#C:\Users\BiG BOSS\Desktop\python\himawari.txt
# from pathlib import Path
# p = Path('himawari.txt')
# if p.exists():
#     print('file exists')
# else:
#     print('file does not exist')    

