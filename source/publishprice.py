from bitshares import BitShares
from bitshares.account import Account
from bitshares.price import Price

from account import accounts

wallet_pwd = "supersecret"

def publish_price(account, price):
    btsNode = 'wss://node.testnet.bitshares.eu'
    bitshares = BitShares(btsNode, account.name, account.pwd)

    price = float(price)
    stlprice = Price(price, "TEST/" + account.asset, bitshares_instance=bitshares)

    btsAccount = Account(account.name, bitshares_instance=bitshares)

    bitshares.wallet.unlock(wallet_pwd)
    bitshares.publish_price_feed(account.asset, stlprice, account=btsAccount)
    bitshares.wallet.lock()

if __name__ == "__main__":
    publish_price(accounts["bc-mauritanie"], 35.5)
