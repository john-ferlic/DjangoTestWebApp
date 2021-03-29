import requests
import json
from .AlphaRoute import Route

KEY = "Q4A5RYR91VTSMIGK"
BASE_URL = f"https://www.alphavantage.co/query?function=OVERVIEW&symbol="

def getStockOverviewData(ticker):
    response = requests.get(f'{BASE_URL}{ticker}&apikey={KEY}')
    resp_dict = json.loads(response.text)
    return resp_dict