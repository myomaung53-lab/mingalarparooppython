
# public, protected, private attrbutes, methods
class BankAccount:
    def __init__(self, name, balance, card_id):
        self.__name = name 
        self.__balance = balance
        self.__card_id= card_id
    
    def get_info(self): # public method
        print(self.__name, self.__balance, self.__card_id)
    
    def __change_card(self, newid): # private method
        self.__card_id = newid
    
    def public_change_card(self, new_cardid):
        self.__change_card(new_cardid)


account_1 = BankAccount("mgmg", 500, 12345)
print(account_1.__dict__)

# account_1.get_info()
# account_1.public_change_card(123456)
# account_1.get_info()

# print(account_1.__balance) # private attributes
# print(account_1.__name)
# print(account_1.__card_id)

# print(account_1._balance) # protected attributes
# print(account_1._name)
# print(account_1._card_id)

# print(account_1.balance) # public attributes
# print(account_1.name)
# print(account_1.card_id)






