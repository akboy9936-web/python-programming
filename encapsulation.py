#encapsulation
class bank:
    __amount=800
    def printamount(self):
        return self.__amount
hdfc=bank()
print(hdfc.printamount)
#abstraction
#feature
from abc import abc,abstractmethod
class payment(abc):
    @abstractmethod 
    def pay(self):
        pass
class UPI (payment):
    def pay(self):
        print("payment done using upi")
class phonepe(payment):
    def pay(self):
        print("payment done using phonepe")
payment=UPI()
payment.pay()
payment=phonepe
payment.pay