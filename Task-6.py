search=int(input('Enter the input search number:'))
size=int(input('Enter the input size number:'))
num_list=[]

for i in range(size):
   save=int(input())
   num_list.append(save)
print (num_list)

count=1
for j in range(len(num_list)):
   if j==search:
      count+=1
print(f'the {search} number is repeated for:',count)


print('*'*100)

questions_list=[]
for i in range(4):
    questions=input('Ask the questions :')
    questions_list.append(questions)

print('---------the questions are-------------')
print(*questions_list ,sep='\n')

print('*'*100)


size=int(input('Enter the input size :'))
num_list=[]

for i in range(size):
   save=int(input())
   num_list.append(save)
print (num_list)

min,max=num_list[0],0
add=0
for i in num_list:
   
   if i>max:max=i
   if i<min:min=i
   add+=i
print(min,max,add)
      
     
         



