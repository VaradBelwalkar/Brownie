from brownie import SimpleStorage,accounts,config

def read_contract():
    print(SimpleStorage[0])
    print(SimpleStorage[1])
   
    
def main():
    read_contract()


