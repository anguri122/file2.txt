def time():
     import time
     timestamp= time.strftime('%H:%M:%S')
     print(timestamp,sep=' ')
     t=int(time.strftime('%H'))
     print(t)
#time()


def calculator():
        number1=float(input('enter a number:'))
        number2=float(input('enter a number:'))
        print('''chose the value where\n 1==addition\n 2==substration\n 3==multplication\nand 4==division\n''')
        def switch(value):
    
            if value ==1:
                return number1+number2
            elif value ==2:
                return number1-number2
            elif value ==3:
                return number1*number2
            elif value ==2:
                return number1/number2
        c=switch(float(input('enter a value:')))
        print('resultis:',c)
calculator()
 

        
