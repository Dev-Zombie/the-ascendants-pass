#!/usr/bin/python3
from brownie import TheAscendantsPass, accounts, network, config


def main():
    dev = accounts.add(config["wallets"]["from_key"])
    print(network.show_active())
    deployed_contract = TheAscendantsPass[len(TheAscendantsPass) - 1]

    deployed_contract.mint(dev, 1,{"from": dev})
    deployed_contract.mint(dev, 2,{"from": dev})

