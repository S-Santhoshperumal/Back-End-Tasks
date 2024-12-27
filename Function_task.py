def circle(Rad,pi):
    output=pi*Rad*Rad
    return output


def main():

   Rad=float(input('Enter the RAdius Value'))
   print('Positional Argument:',circle(Rad,3.14))
   
   print('Keyword Argument:',circle(pi=3.14,Rad=Rad))
   print('Keyword Argument:',circle(Rad,pi=3.14))






if __name__=='__main__':
    main()