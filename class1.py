class Account:
    def __init__(self, accountName, accountBranch, accountNumber):
        self.__accountName = accountName
        self.__accountBranch = accountBranch
        self.__accountNumber = accountNumber
    
    def getAccountName(self):
        return self.__accountName
    
    def setAccountName(self, accountName):
        self.__accountName = accountName
    
    def getAccountBranch(self):
        return self.__accountBranch
    
    def setAccountBranch(self, accountBranch):
        self.__accountBranch = accountBranch
    
    def getAccountNumber(self):
        return self.__accountNumber
    
    def setAccountNumber(self, accountNumber):
        self.__accountNumber = accountNumber
account = Account("Ravi varma", "Kumar", "1234567890")
print(account.getAccountName())         
account.setAccountBranch("Boyez")   
print(account.getAccountBranch())   
