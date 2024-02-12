import loging
class Account:
  
	def __init__(self, name, balance):
      self.name = name
      self.balance = balance

  	def deposit(self, amount):
      self.balance += amount

  	def withdraw(self, amount):  
		if amount > self.balance:
        	print("Insufficient funds")
      	else:
         	self.balance -= amount

 	def get_balance(self): 
		return self.balance

def main():
  accounts = {}
  while True:
      choice = input("1. Open Account\n2. Deposit\n3. Withdraw\n4. Check Balance\n5. Exit\n")
      if choice == "1":
          name = input("Enter your name: ")
          while True:
          	balance = float(input("Enter initial balance: "))
          	if balance > 0:
          		account = Account(name, balance)
          	else:
          		print(f'To open Account Initial Amount should be greather that 0')
          		if open_account != 1:
          			break
          accounts[name] = account
      elif choice == "2":
          name = input("Enter your name: ")
          amount = float(input("Enter deposit amount: "))
          accounts[name].deposit(amount)
      elif choice == "3":
          name = input("Enter your name: ")
          amount = float(input("Enter withdrawal amount: "))
          accounts[name].withdraw(amount)
      elif choice == "4":
          name = input("Enter your name: ")
          print(f"Your balance is: {accounts[name].get_balance()}")
      elif choice == "5":
          break
      else:
          print("Invalid choice")

if __name__ == "__main__":
  main()