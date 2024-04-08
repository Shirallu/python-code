# -*- coding: utf-8 -*-
"""assign12.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1AV-GN4LyvSV3zwuUBe1b-M8k8EK8gJNL
"""

#Assignment12
class Bank:
  def __init__(self):
    self.name = None
    self.type_of_acc = None
    self.age = None
    self.address = None
    self.balance = None

  def createAccount(self,name,age,address,type_of_acc):
    if (age < 18):
        raise ValueError("Age should be greater than 18\nAccount Not created")
    else:
      self.name = name
      self.type_of_acc = type_of_acc
      self.age = age
      self.address = address
      self.balance = 0
      print("Account created successfully")

  def DepositAmount(self,amt_to_deposit):
    if (amt_to_deposit <= 0):
      raise ValueError("Amount to deposit should be greater than 0")
    else:
      self.balance += amt_to_deposit
      print("Amount deposited Successfully")

  def WithdrawAmount(self,amt_to_withdraw):
    if (amt_to_withdraw > self.balance):
      raise ValueError("Insufficient Balance!!!")
    else:
      self.balance -= amt_to_withdraw
      print(f"Amount of rupees {amt_to_withdraw} is withdrawn successfully")

  def UpdateAccount(self):
    print("Enter which Information to Update")
    print("1. Name\n2. Age\n3. Address")
    choice = int(input("Enter your choice: "))
    if (choice == 1):
      name = input("Enter new name: ")
      self.name = name
      print("Name updated Successfully!!")
    elif (choice == 2):
      age = int(input("Enter new Age: "))
      if (age < 18):
        raise ValueError("Age should be greater than 18\nAge not updated!!")
      else:
        self.age = age
        print("Age updated Successfully!!")
    if (choice == 3):
      address = input("Enter new Address: ")
      self.address = address
      print("Address updated Successfully!!")

  def display(self):
    print(f"Name : {self.name}")
    print(f"Age : {self.age}")
    print(f"Type of account : {self.type_of_acc}")
    print(f"Balance :  {self.balance}")

  def displayBalance(self):
     print(f"Balance :  {self.balance}")

obj = Bank()

while(True):
  print("1. TO create new account\n2. To update Account\n3. Withdraw Amount\n4. Deposit Amount\n5. Display Balance\n6. Display Account Information\n7. To exit")
  choice = int(input("Enter your choice: "))

  try:
   if (choice == 1):
     name = input("Enter your name: ")
     age = int(input("Enter your age: "))
     address = input("Enter your address: ")
     type_of_acc = input("Enter type of account(Current/Savings): ")
     obj.createAccount(name,age,address,type_of_acc)
   elif (choice == 2):
     obj.UpdateAccount()
   elif (choice == 3):
     amt_to_withdraw = int(input("Enter the amount to Withdraw: "))
     obj.WithdrawAmount(amt_to_withdraw)
   elif (choice == 4):
     amt_to_deposit = int(input("Enter amount to Deposit: "))
     obj.DepositAmount(amt_to_deposit)
   elif (choice == 5):
     obj.displayBalance()
   elif (choice == 6):
     obj.display()
   elif (choice == 7):
     print("Exiting the program...")
     break
   else:
     print("Invalid choice entered")
  except ValueError as e:
    print(e)