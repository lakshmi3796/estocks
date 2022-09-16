from django.shortcuts import render,redirect
import datetime
import os
import sys
import pandas as pd
import yfinance as yf
from django.http import JsonResponse

def homeindex(request):
    return redirect('homepage')

def HomePage(request):
    try:
        ticker_dict={'Meta Platforms, Inc.':'META','NVIDIA Corporation':'NVDA','Apple Inc.':'AAPL','Aditxt, Inc.':'ADTX','Akero Therapeutics, Inc.':'AKRO','ADT Inc.':'ADT'}
        stockname = request.GET.get('stockname')
        start_date = request.GET.get('start_date')
        end_date = request.GET.get('end_date')
        print("stcok",stockname)
        symbol=""
        if stockname in ticker_dict.keys():
            symbol=ticker_dict[stockname]
        else:
            symbol = "AAPL"
            stockname = "Apple Inc."
            start_date=datetime.date.today()-datetime.timedelta(7)
            end_date = datetime.date.today()
        try:
            current_format = '%m/%d/%Y'
            target_format = '%Y-%m-%d'
            input_date = datetime.datetime.strptime(start_date, current_format).date()
            start_date = input_date.strftime(target_format)
            input_date1 = datetime.datetime.strptime(end_date, current_format).date()
            end_date = input_date1.strftime(target_format)
        except Exception as E:
            exc_type, exc_obj, exc_tb = sys.exc_info()
            print(f"date_str_formatter Error: {E} at {exc_tb.tb_lineno}, Exception Type: {exc_type}")
        print("start date",start_date)
        print("end date",end_date)
        ticker=yf.Ticker(symbol)
        df=ticker.history(start= start_date, end=end_date)
        data=df.to_html()
        print(df)
        print(stockname)
        if request.is_ajax():
            return JsonResponse({'stock_name':list(ticker_dict.keys()),'data':df.to_html(classes='table table-striped borderless'),'stockname':stockname})
        else:
            return render(request, 'eStockZone/home.html',{'stock_name':ticker_dict.keys(),'data':df.to_html(classes='table table-striped borderless'),'stockname':stockname})
    except Exception as E:
        exc_type, exc_obj, exc_tb = sys.exc_info()
        print(f"Home page Error: {E} at {exc_tb.tb_lineno}, Exception Type: {exc_type}")
        return render(request, 'eStockZone/home.html')

