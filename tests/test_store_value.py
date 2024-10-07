
from brownie import StoreValue, accounts

def test_deploy():

    account = accounts[0]

    simple_storage = StoreValue.deploy({"from": account})
    value = simple_storage.retrieve()
    expected = 0

    assert value == expected


def test_store():

    account = accounts[0]
    store_value = StoreValue.deploy({"from": account})

    expected = 99
    txn = store_value.store(expected, {"from": account})
    txn.wait(1)

    assert expected == store_value.retrieve()