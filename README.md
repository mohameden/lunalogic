Idea
-------

The goal of this project is in two parts. First to create smartcoins (or Market Pegged Assets) that will
constantly have the same values than the currencies they are tracking and have the central banks publish
the values of their currency. Second part is the automatic conversion of the currency while paying, this
allow the user to pay as easily in a specific currency as in its own. When paying MAD with TND, a
buy transaction will be done to get TND using MAD then a transfer of the acquired MAD.


This project contains 2 separate modules:
-----------------------------------------

* bitshares-ui: a customized version of the official bitshares wallet.
* smartcoin-management: a python modules that interact with the bitshares blockchain to manage smartcoin lifecycle. It leverage on the py_bitshares api to interface with bitshares blockchain and on the bottle lightweight web server for the associated website.

 Building the bitshares-ui
 -----------------------------------------
 

```
npm install
npm start
goto http://localhost:8080
```

Building the smartcoin-management (source folder)
-----------------------------------------

```
cd source
pip install bitshares bottle
python main.py
goto http://localhost:8088
```


Connection to BitShares
-----------------------
- URL : https://testnet.bitshares.eu or http://localhost:8080 if installation has been done
- account's information are stored in the filed lunalogic/source/account.py using the format ("account's name", "password", other informations)

For example, to connect using "maroc-telecom", you can find the following line:

"maroc-telecom": account("maroc-telecom", "P5KVVNcEBtGwsMAD5zscmufDj4TpisnYNCPdtdZvKAqAZ", ...)

Use "maroc-telecom" as "ACCOUNT NAME" and "P5KVVNcEBtGwsMAD5zscmufDj4TpisnYNCPdtdZvKAqAZ" as "PASSWORD"


Testable functionality
-----------------------

##### http://localhost:8088 : Update of smartcoin's value
Use one of the following fields in "Country" :
[ bc-maroc ; bc-tunisie ; bc-mauritanie] and the value relative to USD in field "Price".

You can see the impacted value in the field "Feed Price" in https://testnet.bitshares.eu/market/TEST[MAD | TND | MRU]_TEST.

If you update the smartcoin of "bc-maroc", you can see it in https://testnet.bitshares.eu/market/TESTMAD_TEST

##### http://localhost:8088/pay : Simulate the payment of a bill in MAD using TND
Click on the "A payer - 100 MAD" button, feed the field "Nom du compte" with one of the
accounts (fatim-a and ahm-ed recommanded), the password field is not yet handled.

The account used will then buy MAD and transfer it. You can see the result by connecting to
https://testnet.bitshares.eu with either "maroc-telecom" or the account used in the section "Dashboard"
then "Activity".


##### python lunalogic/source/exchange.py : Transfer TND from MAD
The account "bc-maroc" transfer 10 TND to "bc-tunisie" using its MAD. You can see the result by connecting in
https://testnet.bitshares.eu with accounts "bc-maroc" or "bc-tunisie" in either "Dashboard/Portfolio" to see
the assets or "Dashboard/Activity" to see the different steps.
