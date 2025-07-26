import json
import random
import string
from pathlib import Path


class Bank:
    database = 'data.json'  # fixed typo here
    data = []

    # Load data from file if exists
    try:
        if Path(database).exists():
            with open(database) as fs:
                data = json.loads(fs.read())
        else:
            print('no data exists')
    except Exception as err:
        print(f'an exception occurred: {err}')

    @classmethod
    def __update(cls):
        with open(cls.database, 'w') as fs:
            fs.write(json.dumps(Bank.data, indent=4))
      



    @classmethod
    def __accountgenerator(cls):
        alpha=random.choices(string.ascii_letters, k=3)
        num=random.choices(string.digits, k=3)
        special=random.choices("@#$%^&*",k=1)
        id=alpha+num+special 
        random.shuffle(id)
        return"".join(id)



    def create_account(self):  # fixed method name and indentation
        info = {
            'name': input('Enter your name: '),
            'age': int(input('Enter your age: ')),
            'email': input('Enter your email: '),
            'phone': input('Enter your phone number: '),
            'pin': input('Enter your 4-digit pin: '),
            'account_number': Bank.__accountgenerator(),  # fixed method call
            'balance': 0,
        }

        if info['age'] < 18 or len(info['pin']) != 4:
            print('You are not eligible to create an account')
        else:
           
            print('Account created successfully!\n')
            for i, value in info.items():
                print(f'{i} : {value}')
            print('\n Please note down your account number ')
        Bank.data.append(info)
        Bank.__update()  # Now it saves the full data list

    def deposit_money(self):
        acc_number = input('Please enter your account number: ')
        pin = input('Enter your 4-digit PIN: ')

        userdata = [i for i in Bank.data if i['account_number'] == acc_number and i['pin'] == pin]

        if not userdata:
            print(' Sorry, no matching data found.')
            return
        else:
           
                amount = int(input('Enter amount to deposit: '))
                if amount > 50000 or amount < 0:
                    print(' You can only deposit between 0 and 50000.')
                else:
                    userdata[0]['balance'] += amount
                    Bank.__update()
                    print(' Amount deposited successfully.')

    def withdraw_money(self):
        acc_number = input('Please enter your account number: ')
        pin = input('Enter your 4-digit PIN: ')

        userdata = [i for i in Bank.data if i['account_number'] == acc_number and i['pin'] == pin]

        if not userdata:
            print(' Sorry, no matching data found.')
            return
        else:
           
                amount = int(input('Enter amount to withdraw: '))
                if amount > userdata[0]['balance']:
                    print(f' sorry! you can not withdraw {amount}rs ')
                else:
                    userdata[0]['balance'] -= amount
                    Bank.__update()
                    print(' Amount withdrew successfully.')

    def check_balance(self):
        acc_number = input('Please enter your account number: ')
        pin = input('Enter your 4-digit PIN: ')

        userdata = [i for i in Bank.data if i['account_number'] == acc_number and i['pin'] == pin]

        if not userdata:
            print(' Sorry, no matching data found.')
            return
        else:
            print(f"Your  available balance is: {userdata[0]['balance']}")

    def view_details(self):
         acc_number = input('Please enter your account number: ')
         pin = input('Enter your 4-digit PIN: ')
         userdata = [i for i in Bank.data if i['account_number'] == acc_number and i['pin'] == pin]

         if not userdata:
            print(' Sorry, no matching data found.')
            return
         else:
            print('your account details are:/n/n/n')
            for i in userdata[0]:
                print(f"{i} : {userdata[0][i]}")
        
    
    def updata_details(self):
        acc_number = input('Please enter your account number: ')
        pin = input('Enter your 4-digit PIN: ')
        userdata = [i for i in Bank.data if i['account_number'] == acc_number and i['pin'] == pin]

        if not userdata:
            print(' Sorry, no matching data found.')
            return
        else:  # This method needs to be defined

          print('you can not update your balance or account number')
          print('fill the details which you want to update if you did not want to update any field just press enter')
        newdata={
              'name':input('enter your name or press enter to skip : '),
              'email':input('enter your email or press enter to skip: '),
              'pin':input('enter your 4-digit PIN or press enter to skip: '),
              'phone':input('enter your phone number or press enter to skip: '),
          }
        if newdata['name']=='':
            newdata['name']=userdata[0]['name']
        if newdata['email']=='':
            newdata['email']=userdata[0]['email']
        if newdata['pin']=='':
            newdata['pin']=userdata[0]['pin']
        if newdata['phone']=='':
            newdata['phone']=userdata[0]['phone']   

        newdata['age']=userdata[0]['age']  
        newdata['account_number']=userdata[0]['account_number']
        newdata['balance']=userdata[0]['balance']  

     
                    
        for i in newdata:
            if newdata[i]==userdata[0][i]:
                continue
            else:
                userdata[0][i]=newdata[i]
        Bank.__update()
        print('Updated data successfully')


    def delete_account(self):
         acc_number = input('Please enter your account number: ')
         pin = input('Enter your 4-digit PIN: ')
         userdata = [i for i in Bank.data if i['account_number'] == acc_number and i['pin'] == pin]

         if not userdata:
            print(' Sorry, no sucha data exists.')
            return
         else:
             print('Are you sure you want to delete your account? (1/2)')
             check=int(input('Enter your choice:'))

            

             if check==1:
                  index=Bank.data.index(userdata[0])
                  Bank.data.pop(index)
                  print('Account deleted successfully.')
             else:
                  if check==2:
                    print('Account not deleted')

                  
                  
             Bank.__update()
                 




# ---- MAIN PROGRAM ----
user = Bank()

print('\nOptions:')
print(' press 1. Create Bank Account')
print(' press2. Deposit Money')
print(' press 3. Withdraw Money')
print(' press 4. Check Balance')
print('press 5. View Account Details')
print(' press 6. Update details')  # This method needs to be defined
print(' press 7. Delete Account')

check = int(input('\nEnter your choice: '))

if check == 1:
    user.create_account()  # fixed case

elif check == 2:
    user.deposit_money()
elif check == 3:
    user.withdraw_money()  # This method needs to be defined    
elif check == 4:
    user.check_balance()
elif check==5:
    user.view_details()
elif check==6:
    user.updata_details()  # This method needs to be defined    
elif check==7:
    user.delete_account()