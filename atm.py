pin=1234  #any pin you can take of your choice
count=3
balance=90000
while count>0:
    
    print(f"Your Chances Left :{count} ")
    user_pin=int(input("enter you pin  "))
    if(user_pin==pin):
        print("you have sucessfyl login")
        options=int(input("press 1 to withdraw\npress 2 to check balance\npress 3 to change  pin "))
        if(options==2):
            print(balance)
            break
        elif(options==1):
            withdraw=int(input("enter how much you wnat to with draw "))
            balance=balance-withdraw
            print(balance)
            break
        elif(options==3):
            pin=int(input("change the pin "))
            print(pin)
            break
            
    
        
    else:
        print("incorrect password")  

    count-=1
    
    
    
 
        
    

