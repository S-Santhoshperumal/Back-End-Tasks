fruits=['mango',['fruitpulp','mixedpulp'],'banana',('apple','grapes')]
print(fruits)
print(fruits[0])
print(fruits[1])
print(fruits[1][0])
print(fruits[1][1])
print(fruits[2])
print(fruits[3][0])
print(fruits[3][1])
#-------------------------------------------------------------------------------------------------


Menu=['Dal','Panner','Kofta','Tawa','Panner','Rice','Roti']
for i in range(0,len(Menu)):
    print(Menu[i])

print('*'*100)

Author_name=('j k rowling','Rachel aaron','hans aanrud','verna aardema')
for i in range(0,len(Author_name)):
    print(Author_name[i])

Timing='it\'s 7:30AM'
for i in range(0,len(Timing)):
    print(Timing[i])

#-------------------------------------------------------------------------------------------------

Name=input('Enter your Name:')
Salary=input('Enter your Salary:')
Company=input('Enter your Company:')
print(Name,Salary,Company)
#-------------------------------------------------------------------------------------------------

input_list=[]
size=int(input('Enter the size: '))
for i in range(size):
    value=float(input('Enter the values: '))
    input_list.append(value)

print(input_list)


input_list_1=[]
size=int(input('Enter the size: '))
for i in range(size):
    value=input('Enter the values: ')
    input_list_1.append(value)
print(input_list_1)

#-------------------------------------------------------------------------------------------------
i=0
Menu =['Dal','Paneer','Kofta','Tawa Paneer','Rice','Roti']
while(i<len(Menu)):
    print(Menu[i])
    i=i+1

j=0
author_name =('j k rowling','rachel aaron','hans aanrud','verna aardema')
while(j<len(author_name)):
    print(author_name[j])
    j=j+1
k=0
Timing = 'It\'s 7.30am'
while(k<len(Timing)):
    print(Timing[k])
    k=k+1
#-------------------------------------------------------------------------------------------------

for i in range(3,16,3):
    print(i)
    
for j in range(12,2,-3):
    print(j)
#-------------------------------------------------------------------------------------------------

Menu =['Dal','Paneer','Kofta','Tawa Paneer','Rice','Roti']
print(Menu)
Menu[3:]='Malai Panner','Tandoori Roti','Naan'
print(Menu)

#-------------------------------------------------------------------------------------------------

fruits = ['mango',['fruitpulp','mixedpulp'],'banana',('apple','grapes')]
for i in range(len(fruits)):
    print(fruits[i])

#-------------------------------------------------------------------------------------------------

val=input()
count=0

for i in val:
    count+=int(i)

print(count)

#-------------------------------------------------------------------------------------------------