
from brownie import accounts,SimpleStorage

def test_deploy_simple_storage():
    accountAddress = accounts[0]
    simple_storage = SimpleStorage.deploy({"from":accountAddress})
    returned_value = simple_storage.retrieve()
    expected_value = 1
    assert returned_value == expected_value








