
from brownie import accounts, StoreValue, network

def deploy_store_value():
    account = get_account()

    storeValue = StoreValue.deploy({"from": account})
    value = storeValue.retrieve()
    print(value)
    transaction = storeValue.store(15, {"from": account})
    transaction.wait(1)
    value = storeValue.retrieve()
    print(value)


def get_account():
    if network.show_active() == "development":
        return accounts[0]
    else:
        return accounts.load("my-sepolia-account")


def main():
    deploy_store_value()
