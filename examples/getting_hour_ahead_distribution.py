from microprediction import MicroReader
from pprint import pprint

mr = MicroReader()
HOUR = mr.DELAYS[3]
PRCTLS = mr.percentiles()
cdf = mr.get_cdf(name='altitude.json', delay=HOUR, values=PRCTLS)
