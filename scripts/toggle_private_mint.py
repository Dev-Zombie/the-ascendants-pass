#!/usr/bin/python3
import os
from brownie import TheAscendantsPass, accounts, network, config


def main():
    dev = accounts.add(config["wallets"]["from_key"])
    print(network.show_active())
    deployed_contract = TheAscendantsPass[len(TheAscendantsPass) - 1]
    # deployed_contract.togglePrivateSaleOpen(1, {"from": dev})
    deployed_contract.togglePrivateSaleOpen(1, {"from": dev})

