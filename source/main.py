from bottle import run, get, post, request, static_file, template, redirect
import bottle
from publishprice import publish_price
from account import accounts
from exchange import payement

####### UI #######
@get('/assets/<filepath:re:.*\.*>')
def css(filepath):
    return static_file (filepath, root="assets/")

@get('/')
def index():
    return template('views/index.html')

@get('/pay')
def pay():
    return template('views/factures.html')

@post('/paybts')
def paybts():
    email = request.forms.get('email')
    password = request.forms.get('password')
    amount = 100
    payement(accounts[email], accounts["maroc-telecom"], amount, accounts[email].asset, accounts["maroc-telecom"].asset)
    return redirect('/pay')

@post('/publish')
def submit_create():
    country = request.forms.get('country')
    price = request.forms.get('price')
    publish_price(accounts[country], float(price))
    return redirect('/')


bottle.debug(True)
run(host='localhost', port=8088, reloader=True)
