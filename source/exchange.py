from bitshares import BitShares
from bitshares.account import Account
from bitshares.asset import Asset
from bitshares.amount import Amount
from account import accounts
from transaction_balancing import myBuy

btsNode = 'wss://node.testnet.bitshares.eu'

def convertFromTEST():
    return

"""
Convert enough *current* currency to have *amount* *target* currency
It works by buying N TEST using *current* then buying *amount* *target* using TEST
"""
def convert(bitshares, current, target, amount, account):
    if current == target:
        return
    if current == "TEST":
        convertFromTEST()
        return
    if target == "TEST":
        #FIXME
        convertFromTEST()
        return

    amount = float(amount)
    current_ass = Asset(current, False, True, bitshares_instance=bitshares)
    print(current_ass.feed)
    curPerBts = current_ass.feed["settlement_price"]

    target_ass = Asset(target, False, True, bitshares_instance=bitshares)
    print(target_ass.feed)
    tarPerBts = target_ass.feed["settlement_price"]

    print(curPerBts)
    print(tarPerBts)

    amount_quot = Amount(float(tarPerBts), target, bitshares_instance=bitshares)
    amount_base = Amount(float(curPerBts), current, bitshares_instance=bitshares)
    myBuy(target, current, amount_quot, amount_base, amount, Account(account.name, bitshares_instance=bitshares), bitshares)

    return




"""
Transfert *amount* asset from acc_from to acc_to
"""
def transfert(acc_from, acc_to, asset, amount):
    bitshares = BitShares(btsNode, acc_from.name, acc_from.pwd)
    bitshares.wallet.unlock("supersecret")
    bitshares.transfer(acc_to.name, float(amount), asset, account=acc_from.name)
    bitshares.wallet.lock()


def payement(buyer, seller, amount, ccy_used, ccy_received):
    bitshares = BitShares(btsNode, buyer.name, buyer.pwd)

    # Buggy without it...
    current_ass = Asset("TESTMRU", False, True, bitshares_instance=bitshares)
    price = current_ass.feed["settlement_price"]
    # End of "hacks"

    convert(bitshares, ccy_used, ccy_received, amount, buyer)
    transfert(buyer, seller, ccy_received, amount)


if __name__ == "__main__":
    payement(accounts["bc-maroc"], accounts["bc-tunisie"], 10, accounts["bc-maroc"].asset, accounts["bc-tunisie"].asset)
