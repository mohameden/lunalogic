from bitshares import BitShares
from bitshares.account import Account
from bitshares.price import Price, PriceFeed
from bitshares.market import Market
from bitshares.asset import Asset
from bitshares.amount import Amount
from account import account, accounts

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
    print(curPerBts)

    target_ass = Asset(target, False, True, bitshares_instance=bitshares)
    print(target_ass.feed)
    tarPerBts = target_ass.feed["settlement_price"]
    print(tarPerBts)

    neededBts = float(amount) / float(tarPerBts)

    print(curPerBts)
    print(neededBts)
    bitshares.wallet.unlock("supersecret")
    market = Market("TEST:" + current, bitshares_instance=bitshares)

    test1 = Amount(1, "TEST", bitshares_instance=bitshares)
    market.buy(Price(test1, Amount(float(curPerBts), current, bitshares_instance=bitshares)), Amount(str(neededBts) + " TEST", bitshares_instance=bitshares), account=Account(account.name, bitshares_instance=bitshares))

    market = Market(target + ":TEST", bitshares_instance=bitshares)
    market.buy(Price(Amount(tarPerBts, target, bitshares_instance=bitshares), test1), Amount(str(amount) + " " + target, bitshares_instance=bitshares), account=Account(account.name, bitshares_instance=bitshares))

    bitshares.wallet.lock()



"""
Transfert *amount* asset from acc_from to acc_to
"""
def transfert(acc_from, acc_to, asset, amount):
    bitshares = BitShares(btsNode, acc_from.name, acc_from.pwd)
    bitshares.wallet.unlock("supersecret")
    bitshares.transfer(acc_to.name, float(amount), asset, account=acc_from.name)
    bitshares.wallet.lock()


if __name__ == "__main__":
    acc = account("test2017", "P5KHthsex8FJtWb7MXRqif9vZWmZA2YkMZCNn11thKoq7", "5KWUzPCHAH9nozGh6GMJn1ojjC8Xz5wsfHnQXJ8hGtJFLz1cm6H", "")
    bitshares = BitShares(btsNode, acc.name, acc.pwd)
    current_ass = Asset("TESTMRU", False, True, bitshares_instance=bitshares)
    price = current_ass.feed["settlement_price"]

    print("MRU")
    convert(bitshares, "TESTMRU", "TESTTND", 10, acc)

    transfert(accounts["maroc"], acc, "TEST", 10)
