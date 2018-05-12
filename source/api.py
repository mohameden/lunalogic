from bottle import run, template, get, post, request, static_file, template, redirect
import bottle
from publishprice import publish_price
from account import accounts

###### API #######

@get('/ping')
def ping():
    return 'pong'

####### UI #######
@get('/')
def index():
    return template('views/index.html')

@post('/publish')
def submit_create():
    #etf = append_etf(request.forms.get('symbol'), request.forms.get('description'), extract_components(request))
    country = request.forms.get('country')
    price = request.forms.get('price')
    print(country)
    print(price)
    publish_price(accounts[country], float(price))
    return redirect('/')


bottle.debug(True)
run(host='localhost', port=8080, reloader=True)
