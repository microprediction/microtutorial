from credentials import ELFEST_BOBCAT  # You'll have to supply your own
import pandas as pd
from microprediction import MicroWriter

# Video explanation of this example:
# https://vimeo.com/443203883

mw = MicroWriter(write_key=ELFEST_BOBCAT) # See creating_a_key.py

def water_height():
    """ Get current water height from double-header no comma NOAA DART format (your tax dollars at work) """
    df = pd.read_csv('https://www.ndbc.noaa.gov/data/realtime2/21413.dart')
    return float(df.iloc[1, :].values[0].split(' ')[-1])   # (sound of Wes McKinney clearing his throat)


if __name__ == '__main__':
    mw.set(name='water.json', value=water_height())
