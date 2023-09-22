from datetime import date,timedelta
import pandas as pd

import matplotlib.dates as mdates

def getCurrDay() -> str:
    return date.today()

def getSpecificDate(num_days_ago) -> (str,'numpy.float64'):
    day = (pd.Timestamp(date.today()) - timedelta(days=num_days_ago)).strftime("%Y-%m-%d")
    return day,mdates.datestr2num(day)

def getSpecificDateNum(num_days_ago) -> 'numpy.float64':
    day = (pd.Timestamp(date.today()) - timedelta(days=num_days_ago)).strftime("%Y-%m-%d")
    return mdates.datestr2num(day)
