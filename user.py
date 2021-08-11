class User:		# here's what we have so far
    # Constructor
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account_balance = 0
    
    # adding the deposit method
    def make_deposit(self, amount):	# takes an argument that is the amount of the deposit
    	self.account_balance += amount	# the specific user's account increases by the amount of the value received
    
    # adding the withdrawal method
    def make_withdrawal(self, amount):	# takes an argument that is the amount of the deposit
    	self.account_balance -= amount	# the specific user's account decrease by the amount of the value withdrawn
    
    # adding the display method
    def display_user_balance(self):	# no arguments needed. Prints the user name and its actual balance
    	print(f"User:{self.name}, Balance: {self.account_balance}")
    
    # adding the transfer method
    def transfer_money(self, amount, user_recipient): # takes two argumens: the amount transfered and the user who is going to receive the transfer
        self.account_balance -= amount
        user_recipient.account_balance += amount

# 3 users are created
guido = User("Guido van Rossum", "guido@python.com")
monty = User("Monty Python", "monty@python.com")
greg = User("Greg Petersen", "greg@python.com")

# First user make 3 deposits and 1 withdrawals
guido.make_deposit(100)
guido.make_deposit(200)
guido.make_deposit(300)
guido.make_withdrawal(250)
guido.display_user_balance()

# Second user make 2 deposits and 2 withdrawals
monty.make_deposit(500)
monty.make_deposit(300)
monty.make_withdrawal(100)
monty.make_withdrawal(150)
monty.display_user_balance()

# Third user make 1 deposits and 3 withdrawals
greg.make_deposit(500)
greg.make_deposit(50)
greg.make_withdrawal(100)
greg.make_withdrawal(50)
greg.display_user_balance()

# Third user transfer money to thir user

guido.transfer_money(50, greg)
greg.display_user_balance()
greg.display_user_balance()