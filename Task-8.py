class menu_card:
    
    
    def __init__(self):
        self.list=['Dosa','Idly','Briyani']
        self.var=0
        
    def display(self):
     print(self.list)
     main()

    def add(self):
        input_item=input('Enter the add item:')
        self.list.append(input_item)
        print('Added menu:',self.list)
        main()

    def update(self):
        print(self.list ,'\n' ,'Which item u want to update')
        exist_item=input('Enter the Exist item:')
        new_item=input('enter the new item:')
        for i in self.list:
            if i==exist_item:
                
                self.var=self.list.index(i)
                self.list[self.var]=new_item
        print('Updated menu:',self.list)
        main()

    def delete(self):
        
        print(self.list)
        delete_item=input('Enter the Delete food:')
        self.list.remove(delete_item)
        print('Deleted menu:',self.list)
        main()

def main():
    
    obj=menu_card()
    
    print('1.Display \n' ,'2.Add \n' ,'3.Update \n' ,'4.Delet \n', '5.exit')
    print('Choose any one of them')
    inputs=int(input('Enter your Choose '))
    if(inputs==1):
        obj.display()
    elif(inputs==2):
        obj.add()
    elif(inputs==3):
        obj.update()
    elif(inputs==4):
        obj.delete()
    elif(inputs==5):
        exit()
    else:
        print('Enter the valid input')
        main()


if __name__=='__main__':
    main()