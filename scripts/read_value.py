from brownie import SimpleStorage, accounts, config


def read_contract():
    # launch the most recent deployment
    simple_storage = SimpleStorage[-1]

    # ABI
    # Address
    print(simple_storage.retrieve())


def main():
    read_contract()
