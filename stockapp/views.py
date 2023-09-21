from django.shortcuts import render
import yfinance as yf
import matplotlib.pyplot as plt
from io import BytesIO
import base64

def index(request):
    plot_url = None
    if request.method == 'POST':
        symbol = request.POST.get('symbol')
        stock_data = yf.download(symbol, start='2022-01-01', end='2023-09-20')
        plt.figure(figsize=(10,5))
        plt.plot(stock_data['Close'], label='Close Price')
        plt.title(f'{symbol} Close Price')
        plt.xlabel('Date')
        plt.ylabel('Close Price (USD)')
        plt.legend(loc='upper left')

        img = BytesIO()
        plt.savefig(img, format='png')
        img.seek(0)
        plot_url = base64.b64encode(img.getvalue()).decode()

    return render(request, 'stockapp/index.html', {'plot_url': plot_url})
