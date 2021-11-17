from brownie import accounts,config,SimpleStorage,network

def deploy_simple_storage():
    accountAddress = get_account()
    simple_storage = SimpleStorage.deploy({"from":accountAddress})
    stored_value = simple_storage.retrieve()
    print(stored_value)
    transaction = simple_storage.store(4324,{"from":accountAddress})
    transaction.wait(1)
    print( simple_storage.retrieve())



def main():
    deploy_simple_storage()

def get_account():   
    if network.show_active() =="development":
        return accounts[0]
    else:
        return accounts.add(config["wallets"]["from_key"]) 


command that makes a sure
