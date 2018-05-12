This project contains 2 separate modules:

* bitshares-ui: a customized version of the official bitshares wallet.
* smartcoin-management: a python modules that interact with the bitshares blockchain to manage smartcoin lifecycle. It leverage on the py_bitshares api to interface with bitshares blockchain and on the bottle lightweight web server for the associated website.

Builing the bitshares-ui
npm install
npm start
goto http://localhost:8080

Building the smartcoin-management

pip install bitshares bottle
python main.py
goto http://localhost:9090
