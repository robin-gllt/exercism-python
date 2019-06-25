from threading import Lock, Thread

class BankAccount(object):
    
    lock = Lock()
    account_is_opened = False
    _balance = 0

    def __init__(self):
        pass

    def get_balance(self):
        if not self.account_is_opened:            
            raise ValueError("Account is closed")
        # self.lock.release()
        return self._balance

    def open(self):
        # self.lock.acquire()
        if self.account_is_opened:
 
            raise ValueError ("Account already opened")
        else:            
            self.account_is_opened = True

        return True

    def deposit(self, amount):
        self.lock.acquire()
        try:
            if not self.account_is_opened:
                raise ValueError ("You can't add money, the account is closed")
            
            if type(amount) != int or amount < 0:
                raise ValueError ("Deposit value '",amount,"' is not correct") 
            self._balance += amount 
        finally:
            self.lock.release()

        return True

    def withdraw(self, amount):
        self.lock.acquire()
        try:
            if not self.account_is_opened:
                raise ValueError ("You can't withdraw money, the account is closed")

            if type(amount) != int or amount < 0:
                raise ValueError ("Withdrawn value '",amount,"' is not correct")            

            if (self._balance - amount) < 0:
                raise ValueError ("Insufficient funds")
            else:
                self._balance -= amount
        finally:
            self.lock.release()

        return True

    def close(self):
      
        if not self.account_is_opened:
            raise ValueError("Account already closed")
        
        self.account_is_opened = False
        self._balance = 0
        
        return True


if __name__ == "__main__":

    account = BankAccount()
    account.open()
    account.deposit(1000)
    account.withdraw(50)
    
