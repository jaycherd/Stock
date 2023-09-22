from django.shortcuts import render
import yfinance as yf
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from io import BytesIO
import base64
from stockapp import utils

def index(request):
    plot_url = None
    if request.method == 'POST':
        symbol = request.POST.get('symbol')
        start_date,start_date_num = utils.getSpecificDate(num_days_ago=366)
        end_date,end_date_num = utils.getSpecificDate(num_days_ago=1)
        stock_data = yf.download(symbol, start=start_date, end=end_date)
        # Define the date format
        date_fmt = '%Y-%m-%d'  # e.g., 2023-09-22
        date_formatter = mdates.DateFormatter(date_fmt)
        # Get current axis and set the formatter
        plt.figure(figsize=(10,5))
        plt.xlim(start_date_num,end_date_num)
        plt.xticks(rotation=45)
        ax = plt.gca()
        ax.xaxis.set_major_formatter(date_formatter)
        ax.xaxis.set_major_locator(mdates.MonthLocator())   
        plt.plot(stock_data['Close'], label='Close Price')
        xtick_locs = ax.get_xticks()
        ymin,ymax = ax.get_ylim()
        plt.vlines(x=xtick_locs,ymin=ymin,ymax=ymax, color='#D3D3D3', linestyles='dashed', alpha=0.5)
        plt.title(f'{symbol} Close Price')
        plt.xlabel('Date')
        plt.ylabel('Close Price (USD)')
        plt.legend(loc='upper left')
        plt.tight_layout()

        img = BytesIO()
        plt.savefig(img, format='png')
        img.seek(0)
        plot_url = base64.b64encode(img.getvalue()).decode()

    return render(request, 'stockapp/index.html', {'plot_url': plot_url})
