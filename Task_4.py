Menu_card=['Dosa','Idly','Briyani']

def display():
     print(Menu_card)
     main()

def add():
    input_item=input('Enter the add item:')
    Menu_card.append(input_item)
    print('Added menu:',Menu_card)
    main()

def update():
     print(Menu_card ,'\n' ,'Which item u want to update')
     exist_item=input('Enter the Exist item:')
     new_item=input('enter the new item:')
     for i in Menu_card:
        if i==exist_item:
          var=Menu_card.index(i)
          Menu_card[var]=new_item
     print('Updated menu:',Menu_card)
     main()

def delete():
     print(Menu_card)
     delete_item=input('Enter the Delete food:')
     Menu_card.remove(delete_item)
     print('Deleted menu:',Menu_card)
     main()

def main():
    print('1.Display \n' ,'2.Add \n' ,'3.Update \n' ,'4.Delet \n', '5.exit')
    print('Choose any one of them')
    inputs=int(input('Enter your Choose '))
    if(inputs==1):
        display()
    elif(inputs==2):
        add()
    elif(inputs==3):
        update()
    elif(inputs==4):
        delete()
    elif(inputs==5):
        exit()
    else:
        print('Enter the valid input')
        main()


if __name__=='__main__':
    main()