import time
print("Please enter your Card")

time.sleep(5)

password=1234

pin=int(input("Enter your ATM pin "))


balance = 5000


if pin==password:
    while True:
    
        print("""
              1 == balance
              2 == withdraw balance
              3 == deposit balance
              4 == exit
              """
              )

        try:
            option=int(input("Please enter your choice "))
        except:
            print("Please enter valid option")

        if option == 1:
            print(f"Your Current balance is {balance}")

            print("======================================================")
            print("======================================================")
            print("======================================================")
            
        if option == 2:

            withdraw_amount=int(input("Please enter withdraw amount "))

            print("======================================================")
            print("======================================================")

            balance=balance-withdraw_amount

            print(f"{withdraw_amount} is debited from your account")

            print("======================================================")
            print("======================================================")
            
            print(f"Your updated balance is {balance}")

            print("======================================================")
            print("======================================================")
    
        if option == 3:
            
            deposit_amount=int(input("Please enter deposit amount"))

            print("======================================================")
            print("======================================================")
          
            balance+=deposit_amount

            print(f"{deposit_amount} is credited to your account")

            print("======================================================")
            print("======================================================")
            
            print(f"Your updated balance is {balance}")

            print("======================================================")
            print("======================================================")

        if option == 4:
            break


else:
    print("Wrong pin Please try again")
