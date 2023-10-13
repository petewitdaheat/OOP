from transaction.transaction import *

class account(transaction):
    """The Account class includes methods to manage the balance
    of a bank account.

    Args:
        transaction (transacction): abstract class that 
        defines methods that may be implemented by an account class.
    """    
    def __init__(self, *args):
        """Constructs an account with a specified balance if args length
        is 1, else constructs an account with a balance of 0.

        Raises:
            ValueError: indicates args[0] is less than 0.
        """        
        #print(args)
        if (len(args) == 1):
            try:
                if (args[0] < 0.0):
                    raise ValueError("Balance is less than zero.")
            except ValueError as e:
                exit(e)
            finally:
                self.__balance = float(args[0]) # this is a private instance variable
                self.public = 'public'          # this is a public instance variable
                self._protected = 'protected'   # this is a protected instance variable
        else:
            self.__balance = 0.0

    def __privateMethod(self):
        print('Private Method')

    def _protectedMethod(self):
        print('Protected Method')

    def publicMethod(self):
        print('Public Method')

        """def __del__(self):
            print('Account destroyed')
        """

    def getBalance(self):
        """Returns the balance of the calling account.

        Returns:
            float: the balance.
        """        
        return self.__balance
    
    def isEmpty(self):
        """Checks if the balance for the calling account is zero.

        Returns:
            Boolean: True if the balance for the calling account is zero,
            else False.
        """        
        return self.__balance == 0
    
    def credit(self, amount: float):
        """Increases the balance of the calling account by the specified amount.

        Args:
            amount (float): the amount to increase the balance by

        Raises:
            ValueError: indicates the specified amount is less than zero.
        """        
        try:
            if (amount < 0.0):
                raise ValueError("Credit amount is less than zero.")
        except ValueError as e:
            exit(e)
        else:
            self.__balance += amount

    def debit(self, amount: float):
        """Decreases the balance of the calling account by the specified amount.

        Args:
            amount (float): the amount to decrease the balance by.

        Raises:
            ValueError: indicates the specified amount is less than 0
            ValueError: indicates the specified amount is greater than the 
            balance of the calling account
        """        
        try:
            if (amount < 0.0):
                raise ValueError("Debit amount is less than zero.")
            if (amount > self.__balance):
                raise ValueError("Debit amount is greater than the balance.")
        except ValueError as e:
            exit(e)
        else:        
            self.__balance -= amount

    def __str__(self):
        return f"account balance={self.__balance}"
    
    def __eq__(self, other):
        # check if other is not None
        if other is not None:
            # check if other is an account type
            if isinstance(other, account):
                # check if other's balance is equal to the balance
                # of the calling object
                if other.__balance == self.__balance:
                    return True
                
        return False
    
    @staticmethod
    def sum(account1, account2):
        if (account1 is None or account2 is None):
            return 0.0
        elif (not isinstance(account1, account) or not isinstance(account2, account)):
            return 0.0
        else:
            return account1.__balance + account2.__balance
        
    @staticmethod
    def transfer(a, amount: float):
        try:
            if (amount < 0.0):
                raise ValueError("Debit amount is less than zero.")
            elif (a is None):
                raise ValueError("Account is None.")
            elif (not isinstance(a, account)):
                raise AttributeError("a is not an account type.")
            elif (amount > a.getBalance()):
                raise ValueError("Debit amount is greater than the balance in the specified account.")
        except ValueError as e:
            exit(e)
        else:
            a.debit(amount)
            newAccount = account(amount)
            return newAccount