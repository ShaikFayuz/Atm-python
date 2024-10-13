#Project ATM Functionality
#SBI Bank by Fayuzsystems

import time

import sys

user_balance = 2000

trans1 = 'NA'
trans2 = 'NA'
trans3 = 'NA'
trans4 = 'NA'
trans5 = 'NA'
trans6 = 'NA'
trans7 = 'NA'
trans8 = 'NA'
trans9 = 'NA'
trans10 = 'NA'

print('''P.S The code is 1212.
Don't use caps.
You can only see your previous 10 transactions.''')
time.sleep(1)
print('Welcome to SBI Banking.')
print()
time.sleep(1)
attempts = True

while attempts == True:

    attempt1 = input('Please enter PIN: ')

    if attempt1 == '2912':
        print('Correct Pin')
        time.sleep(1)
        break

    else:
        print("incorrect")
        time.sleep(0.75)
        attempt2 = input('please enter correct PIN: ')
        if attempt2 == '2912':
            print("correct PIN")
            break

        else:
            print("incorrect PIN")
            time.sleep(0.75)
            print("you have 1 more attempt: ")
            attempt3 = input("Please enter correct PIN: ")
            if attempt3 == '2912':
                print("Correct PIN:")
                break

            else:
                print('Incorrect PIN:')
                print('Wait 2 minutes to try again (or restart code):')
                time.sleep(120)
                print()

yes = 0

valid_option = True
while valid_option == True:
    time.sleep(0.75)
    menu = input('''
Please select an option:
                 
Welcome to SBI Banking.
1 - Display balance
2 - Withdraw funds
3 - Deposit funds
4 - Print List of transactions
9 - Return card
                 
---> : ''')
    
    print()
    if menu == "1":

        print("Display Balance")
        
        print('$', user_balance)

        print()
        time.sleep(0.25)
        
    elif menu == "2":
         print("Withdraw Funds")
         time.sleep(0.75)
         wf = int(input('''
How much would you like to  withdraw?
Your options are:
10:
50:
100:
200:
500:
1000:
2000:
7 - Other(must be a multiple of 10):
8 - Return to main menu:
9 - Return card:

--->:    '''))

if wf == user_balance:

    print("Congratulations you broke, you now have $ 0 in your bank account")
    user_balance = 0
    never = 'Withdrew', wf

elif wf > user_balance:
    print("you don't that much money")
    never = 0

    yes = yes - 1

elif wf == 10:
    print("Successful withdrawn $ 10, you now have", user_balance - 10)

    user_balance = user_balance - wf

    never = 'Withdrew', wf

elif wf == 50:
    print("Successful withdrawn $ 50, you now have", user_balance - 50)

    user_balance = user_balance - wf

    never = 'Withdrew', wf

elif wf == 100:
    print("Successful withdrawn $ 100, you now have", user_balance - 100)

    user_balance = user_balance - wf

    never = 'Withdrew', wf

elif wf == 200:
    print("Successful withdrawn $ 200, you now have", user_balance - 200)

    user_balance = user_balance - wf

    never = 'Withdrew', wf

elif wf == 500:
    print("Successful withdrawn $ 500, you now have", user_balance - 500)

    user_balance = user_balance - wf

    never = 'Withdrew', wf

elif wf == 1000:
    print("Successful withdrawn $ 1000, you now have", user_balance - 1000)

    user_balance = user_balance - wf

    never = 'Withdrew', wf

elif wf == 7:
    print("Other amount")

    ea = int(input("How much would you like to withdraw?: "))

    if ea ==user_balance:
        print("Congratulations you broke, you now have $ 0 in your bank account")
        user_balance = 0
        never = 'withdrew', ea
    
    elif ea > user_balance:

        print("you don't have that much money")
        never = never
        yes = yes -1
    
    elif ea % 10 == 0:
         print("Successfully withdraw $", ea, "you now have $", user_balance - ea)
         user_balance = user_balance - ea
         never = 'Withdrew', ea

    else:
        print("Invalid")
        print("Make sure it is a multiple of 10 and numbers only")
        never = never
        yes = yes - 1

elif wf == 8:
    print()
    never = never
    yes = yes - 1

elif wf == 9:
    print('Thank you for Banking at SBI Bank')
    sys.exit()
else:
    print("Invalid")
    yes = yes - 1

yes = yes + 1
if yes > 10:
    trans1 = trans2
    trans2 = trans3
    trans3 = trans4
    trans4 = trans5
    trans5 = trans6
    trans6 = trans7
    trans7 = trans8
    trans8 = trans9
    trans9 = trans10
    trans10 = never
elif yes == 1:
    trans1 = never
elif yes == 2:
    trans2 = never
elif yes == 3:
    trans3 = never
elif yes == 4:
    trans4 = never
elif yes == 5:
    trans5 = never
elif yes == 6:
    trans6 = never
elif yes == 7:
    trans7 = never
elif yes == 8:
    trans8 = never
elif yes == 9:
    trans9 = never
elif yes == 10:
    trans10 = never

elif menu == "3":
    print("Deposit Funds")
    EA = int(input('''
Chose an option:
1 - Deposit
2 - Return to main menu
9 - Return card

--->: '''))
    if EA == 1:
        dp = int(input("How much would you like to deposit?: "))
        if dp > 0:
            print("Successfully Deposited", dp, "you now have $", user_balance + dp)
            user_balance = user_balance + dp
            never = 'Deposited', dp
        
        elif dp < 0:
            print("you can't use negative numbers")
            never = never
            yes = yes - 1

    elif EA == 2:
        print()
        never = never
        yes = yes -1
    elif EA == 9:
        print("Thank you for using SBI banking:")
        sys.exit()

    yes = yes + 1
    if yes > 10:
     trans1 = trans2
     trans2 = trans3
     trans3 = trans4
     trans4 = trans5
     trans5 = trans6
     trans6 = trans7
     trans7 = trans8
     trans8 = trans9
     trans9 = trans10
     trans10 = never

elif yes == 1:
    trans1 = never
elif yes == 2:
    trans2 = never
elif yes == 3:
    trans3 = never
elif yes == 4:
    trans4 = never
elif yes == 5:
    trans5 = never
elif yes == 6:
    trans6 = never
elif yes == 7:
    trans7 = never
elif yes == 8:
    trans8 = never
elif yes == 9:
    trans9 = never
elif yes == 10:
    trans10 = never

elif menu == "4":
    print("Print list of transactions")
    time.sleep(0.75)
    print()
    print(trans1)
    print(trans2)
    print(trans3)
    print(trans4)
    print(trans5)
    print(trans6)
    print(trans7)
    print(trans8)
    print(trans9)
    print(trans10)

elif menu =="9":
    print("Thank you for using SBI Banking:")
    sys.exit()

else:
    print("please choose a valid")








