from getjson import getjson
from pprint import pprint
import operator


def descend(d):
    return {k: v for k, v in sorted(d.items(), key=lambda item: item[1], reverse=True)}


PRIZES = 'https://api.microprediction.org/prizes/'
pprint([list(zip(money, descend(getjson(url)))) for url, money in getjson(PRIZES).items()])
