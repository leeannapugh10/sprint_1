import pandas as pd
# NOTES NOTES NOTES NOTES -----------------------------------------------
# Build my class of type DataFrame
# df holds a DataFrame "object"
# When I create a new object and save it to a variable,
# I say that I have "instantiated" that object.
# OOP = Object Oreneited Project
# df = pd.DataFrame({'a': [1,2,3], 'b': [4,5,6]})

# if __name__ == '__main__':

# Variables that form part of an "object"
# are called "attributes"
# we will access them using "dot-notation"
#    print(df.shape)
#    print(df.dtypes)
#    print(df.index)
#    print(df.columns)

# Functions that form part of an "object"
# are called "methods"
# They have "invoking paraenthesis"
#    print(df.head())
#    print(df.describe())
#    print(df.isnull().sum())

# a method associated with a Pandas "series" object
# aka "column"
# which lives inside of a dataframe
#    print(df['a'].value_counts())
# -----------------------------------------------------------------------


class Wallet:
    '''# first thing to run when we make a new class
    # outline required user-provided input values here
    # parameters with default values assigned are optional **add =0**
    '''
    def __init__(self, initial_amount=0):
        # save the user-provided initial_amount as an attribute
        # self refers to whatever object I'm working with
        self.balance = initial_amount

    # spend cash METHOD
    def spend_cash(self, amount):
        '''
        function docstring
        '''
        if self.balance < amount:
            return "Not enough money"
        self.balance = self.balance - amount
        return f"remaining balance: ${self.balance}"

    def add_cash(self, amount):
        '''
        function docstring
        '''
        self.balance = self.balance + amount
        return f"new balance of: ${self.balance}"

    # __repr__ method
    # changes how the "object" looks when it is print out
    # presence of the self keyword allows me to access or
    # modify class attributes within this function
    def __repr__(self):
        return f"Wallet with balance of: ${self.balance}"


if __name__ == "__main__":
    wallet1 = Wallet(100)
    wallet2 = Wallet(1300)
    wallet3 = Wallet(5)
    print(wallet1)
    print(wallet2.spend_cash(120))
    print(wallet1.spend_cash(60))
    print(wallet1.balance)
    print(wallet3.add_cash(600))
    print(wallet2.spend_cash(480))
    # I can get just the balance if:
    # print(wallet1.balance)
