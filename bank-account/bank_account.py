from multiprocessing import Lock, Process, Value

lock = Lock()
class BankAccount:
    def __init__(self):
        pass

    def get_balance(self):
        self.check_account()
        return self.balance.value

        
    def open(self):
        if hasattr(self, 'balance'):
            raise ValueError('There is already an account open')
        self.balance = Value('i')


    def deposit(self, amount):
        self.check_account()
        if amount < 0:
            raise ValueError('You cannot deposit a negative amount')
        pd = Process(target=self.deposits, args=(amount, lock))
        pd.start()
        pd.join()

    def deposits(self, amount, lock):   
        lock.acquire()
        self.balance.value += amount
        lock.release()


    def withdraw(self, amount):
        self.check_account()
        if (self.balance.value - amount) < 0:
            raise ValueError('You don\'t have enough funds to withdraw that much')
        if amount < 0:
            raise ValueError('You cannot withdraw a negative amount')
        pw = Process(target=self.withdraws, args=(amount, lock))
        pw.start()
        pw.join()
        
        
    def withdraws(self, amount, lock):
        lock.acquire()
        self.balance.value -= amount
        lock.release()


    def close(self):
        self.check_account()
        del self.balance


    def check_account(self):
        if not hasattr(self, 'balance'):
            raise ValueError('There is no account')

   


