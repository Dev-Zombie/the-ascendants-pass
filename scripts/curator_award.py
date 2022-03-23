#!/usr/bin/python3
import os
from brownie import TheAscendantsPass, accounts, network, config


def main():
    dev = accounts.add(config["wallets"]["from_key"])
    print(network.show_active())
    deployed_contract = TheAscendantsPass[len(TheAscendantsPass) - 1]
    # deployed_contract.curatorAward(1, 3, {"from": dev})
    deployed_contract.curatorAward(2, 45, {"from": dev})
