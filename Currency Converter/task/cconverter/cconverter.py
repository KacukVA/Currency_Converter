import requests
import json
a = input().upper()
cache = dict()
other = dict()
requests_result = requests.get(f'http://www.floatrates.com/daily/{a}.json')
result = json.loads(requests_result.text)
for i in result:
    if i == 'eur' or i == 'usd':
        cache.update({i.upper(): result[i]['rate']})
    else:
        other.update({i.upper(): result[i]['rate']})
while other != {}:
    currency = input().strip().upper()
    if currency == '':
        break
    money = float(input())
    if money == '':
        break
    print('Checking the cache...')
    if currency in cache:
        print('Oh! It is in the cache!')
        print(f'You received {round(money * cache.get(currency), 2)} {currency}.')
    else:
        print('Sorry, but it is not in the cache!')
        cache.update({currency: other.pop(currency)})
        print(f'You received {round(money * cache.get(currency), 2)} {currency}.')
