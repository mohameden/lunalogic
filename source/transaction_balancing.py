from bitshares import BitShares
from bitshares.account import Account
from bitshares.price import Price
from bitshares.market import Market
from bitshares.amount import Amount
from account import accounts
from time import sleep

btsNode = 'wss://node.testnet.bitshares.eu'

def myBuy(ccy_quot, ccy_base, amount_quot, amount_base, amount, account, bitshares):
    acc2 = accounts["test2017"]
    bts2 = BitShares(btsNode, acc2.name, acc2.pwd)
    market = Market(ccy_quot + ":" + ccy_base, bitshares_instance=bts2)
    bts2.wallet.unlock("supersecret")
    market.sell(Price(amount_quot, amount_base, bitshares_instance=bts2), Amount(str(amount) + " " + ccy_quot, bitshares_instance=bts2), account=Account(acc2.name, bitshares_instance=bts2))
    bts2.wallet.lock()

    market = Market(ccy_quot + ":" + ccy_base, bitshares_instance=bitshares)
    bitshares.wallet.unlock("supersecret")
    market.buy(Price(amount_quot, amount_base, bitshares_instance=bitshares), Amount(str(amount) + " " + ccy_quot, bitshares_instance=bitshares), account=account)
    bitshares.wallet.lock()

    sleep(2)
    return



def mySell():
   # market = Market(target + ":TEST", bitshares_instance=bitshares)
   # market.buy(Price(Amount(tarPerBts, target, bitshares_instance=bitshares), test1), Amount(str(amount) + " " + target, bitshares_instance=bitshares), account=Account(account.name, bitshares_instance=bitshares))
    return
