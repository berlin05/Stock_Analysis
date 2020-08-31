# INCLUDING ALL THE REQUIRED LIBRARIES

import pandas_datareader.data as web
import os
import datetime
import time
import shutil
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# INITIALISING TICKERS AND COMPANY'S NAME

tickers = ['BOMDYEING.BO','BHARATFORG.BO','COLPAL.BO','TATASTEEL.BO','EICHERMOT.BO','TITAN.BO','RAYMOND.BO',
'LT.BO','ITC.BO','BHEL.BO','SAIL.BO','SBIN.BO','TATAMOTORS.BO','BRITANNIA.BO']
t = ['The_Bombay_Dyeing_and_Manufacturing_Company_Limited','Bharat_Forge_Limited','Colgate_Palmolive_Limited',
'Tata_Steel_Limited','Eicher_Motors_Limited','Titan_Company_Limited','Raymond_Limited','Larsen_toubro_Limited',
'ITC_Limited','Bharat_Heavy_Electricals_Limited','Steel_Authority_of_India_Limited','State_Bank_Of_India',
'Tata_Motors_Limited','Britannia_Industries_Limited']



# GREETINGS
print("*************************************************************************************************")
print("########     WELCOME TO THE PREDICTION AND ANALYSIS OF TREND OF STOCK MARKET     ###########")
print("*************************************************************************************************")
print("\n")
print("CREATED BY:-\nADHISHWAR NARAYAN TIWARI\nARCHI TIWARI\n")

# CREATING THE STORAGE DIRECTORY IN WHICH ALL THE COMPANY'S DATA WILL BE STORED

print("THE 14 COMPANIES FROM WHICH YOU CAN SELECT IS AS FOLLOWING:-\n")
d={}
end = datetime.datetime.now()
end = '%s-%s-%s' % (end.month,end.day,end.year)
start = '1-1-1996'

directory = 'Stock_Data_Storage'
if os.path.exists(directory):
    shutil.rmtree(directory, ignore_errors=True)
    os.makedirs(directory)
else:
    os.makedirs(directory)
c=0
for ticker in tickers:
    d[ticker] = web.DataReader(ticker,"yahoo",start,end)
    df=d[ticker]
    df.reset_index(level=0,inplace=True)
    df.index = np.arange(1,len(df)+1)
    df.index.name='Index'
    filename=directory+'/'+t[c]+'.csv'
    c=c+1
    df.to_csv(filename,index=True, encoding='utf-8') 


# DISPLAYING 14 COMPANY'S NAME

c=1
for x in t:
    print(c,''+x)
    c=c+1


# SELECTING THE NUMBER OF COMPANIES AND COMPANIES FOR COMPARISON

n=int(input("\nENTER THE NUMBER OF COMPANIES YOU WANT TO COMPARE\n"))
l=[]
on=[]
if n!=14 and n<14:
    print("\nSELECT",n,"COMPANIES AND ENTER THEIR RESPECTIVE SERIAL NUMBER")
    d=1
    while d<=n:
        x=int(input(""))
        new=tickers[x-1]
        new2=t[x-1]
        l.append((new))
        on.append((new2))
        d=d+1
elif n==14:
    l=tickers
    on=t
else:
    print("\nWRONG INPUT!! TRY AGAIN PLEASE\n")


# MAKING THE ACTIVE DIRECTORY CONTAINING SELECTED COMPANY'S DATA

d2={}
end = datetime.datetime.now()
end = '%s-%s-%s' % (end.month,end.day,end.year)
start = '1-1-1996'

directory2 = 'Stock_Data_Active'
if os.path.exists(directory2):
    shutil.rmtree(directory2, ignore_errors=True)
    os.makedirs(directory2)
else:
    os.makedirs(directory2)
c=0
for r in l:
    d2[r] = web.DataReader(r,"yahoo",start,end)
    df2=d2[r]
    df2.reset_index(level=0,inplace=True)
    df2.index = np.arange(1,len(df2)+1)
    df2.index.name='Index'
    filename2=directory2+'/'+on[c]+'.csv'
    c=c+1
    df2.to_csv(filename2,index=True, encoding='utf-8')


# READING DATA
data=[]
for x in on:
    da=pd.read_csv(directory2+'/'+x+'.csv')
    data.append((da))
#for g in range(0,len(data)):
 #   data[g].index=data[g]['Date']
 #   data[g].drop(inplace=True,columns='Date')
    

# TECHNICAL INDICATORS / ANALYSIS

while True:
    print("\nTHE TECHNICAL INDICATORS ARE AS FOLLOWS:-\n")
    print("1. SIMPLE GRAPH OF OPEN\n2. SIMPLE GRAPH OF HIGH\n3. SIMPLE GRAPH OF LOW\n4. SIMPLE GRAPH OF CLOSE\n"
    "5. SIMPLE GRAPH OF VOLUME\n6. SIMPLE GRAPH OF ADJCENT CLOSE\n7. 52 WEEK MOST ACTIVE\n8. ALL TIME MOST ACTIVE\n"
    "9. 5,10,20 DAYS SIMPLE MOVING AVERAGE\n10. 50,100,200 DAYS SIMPLE MOVING AVERAGE\n11. DAILY RETURNS\n"
    "12. CUMULATICVE RETURNS\n13. BOLLINGER BANDS\n")
    select=int(input("CHOOSE ANY TECHNICAL INDICATORS FOR FURTHER ANALYSIS AND COMPARISON\n"))
    
    
    if select==1:
        for x in range(0,len(data)):
            data[x]['Open'].plot(label=on[x],figsize=(16,8),title="OPEN PRICE")
        plt.legend();
        plt.show();
    
    
    elif select==2:
        for x in range(0,len(data)):
            data[x]['High'].plot(label=on[x],figsize=(16,8),title="HIGHEST PRICE")
        plt.legend();
        plt.show();
    
    
    elif select==3:
        for x in range(0,len(data)):
            data[x]['Low'].plot(label=on[x],figsize=(16,8),title="LOWEST PRICE")
        plt.legend();
        plt.show();


    elif select==4:
        for x in range(0,len(data)):
            data[x]['Close'].plot(label=on[x],figsize=(16,8),title="CLOSE PRICE")
        plt.legend();
        plt.show();
    
    
    elif select==5:
        for x in range(0,len(data)):
            data[x]['Volume'].plot(label=on[x],figsize=(16,8),title="VOLUME TRADED")
        plt.legend();
        plt.show();
        for x in range(0,len(data)):
            max=data[x]['Volume'].idxmax()
            date=data[x].loc[max,'Date']
            volume=data[x].loc[max,'Volume']
            print("ON "+date+" "+on[x]+" Traded",int(volume)," Shares Which was all Time Maximum")
    
    
    elif select==6:
        for x in range(0,len(data)):
            data[x]['Adj Close'].plot(label=on[x],figsize=(16,8),title="ADJCENT CLOSE PRICE")
        plt.legend();
        plt.show();
    
    
    elif select==7:
        new={}
        for x in l:
            new[x] = web.DataReader(x,"yahoo",'2018-01-01','2019-01-01')
            new[x].reset_index(level=0,inplace=True)
            new[x].index = np.arange(1,len(new[x])+1)
            new[x].index.name='Index'
        traded=[]
        for x in range(0,len(new)):
            new[l[x]]['Most_Active']=(((new[l[x]]['Close']+new[l[x]]['Open']+new[l[x]]['High']+new[l[x]]['Low'])/4)*new[l[x]]["Volume"])
            maxt=new[l[x]]['Most_Active'].sum()
            traded.append((maxt))
            new[l[x]]['Most_Active'].plot(label=on[x],figsize=(16,8),title="MOST ACTIVE")
        plt.legend();
        plt.show();
        maxtr=np.max(traded)
        inmax=traded.index(maxtr)
        print("\nTHE MOST ACTIVE AMONG ",len(new)," COMPANIES YOU SELECTED IS "+on[inmax]+"\n")
   
   
    elif select==8:
        traded=[]
        for x in range(0,len(data)):
            data[x]['Most_Active']=(((data[x]['Close']+data[x]['Open']+data[x]['High']+data[x]['Low'])/4)*data[x]["Volume"])
            maxt=data[x]['Most_Active'].sum()
            traded.append((maxt))
            data[x]['Most_Active'].plot(label=on[x],figsize=(16,8),title="MOST ACTIVE")
        plt.legend();
        plt.show();
        maxtr=np.max(traded)
        inmax=traded.index(maxtr)
        print("\nTHE MOST ACTIVE AMONG ",len(data)," COMPANIES YOU SELECTED IS "+on[inmax]+"\n")
    
    
    elif select==9:
        close=data[0]["Adj Close"]
        sma5 = close.rolling(window=5).mean()
        sma10 = close.rolling(window=10).mean()
        sma20 = close.rolling(window=20).mean()
        plt.style.use('fivethirtyeight')
        plt.figure(figsize = (16,8))
        plt.plot(close, label='SPY Adj Close', linewidth = 2)
        plt.plot(sma5, label='5 day rolling SMA', linewidth = 2)
        plt.xlabel('Date')
        plt.ylabel('Adjusted closing price ($)')
        plt.title('Price with a single Simple Moving Average')
        plt.legend()
        plt.show();
    
        plt.style.use('fivethirtyeight')
        plt.figure(figsize = (16,8))
        plt.plot(close, label='SPY Adj Close', linewidth = 2)
        plt.plot(sma10, label='10 day rolling SMA', linewidth = 2)
        plt.xlabel('Date')
        plt.ylabel('Adjusted closing price ($)')
        plt.title('Price with a single Simple Moving Average')
        plt.legend()
        plt.show();
    
        plt.style.use('fivethirtyeight')
        plt.figure(figsize = (16,8))
        plt.plot(close, label='SPY Adj Close', linewidth = 2)
        plt.plot(sma20, label='20 day rolling SMA', linewidth = 2)
        plt.xlabel('Date')
        plt.ylabel('Adjusted closing price ($)')
        plt.title('Price with a single Simple Moving Average')
        plt.legend()
        plt.show();
    
        plt.style.use('fivethirtyeight')
        plt.figure(figsize = (16,8))
        plt.plot(close, label='SPY Adj Close', linewidth = 2)
        plt.plot(sma5, label='5 day rolling SMA', linewidth = 2)
        plt.plot(sma10, label='10 day rolling SMA', linewidth = 2)
        plt.plot(sma20, label='20 day rolling SMA', linewidth = 2)
        plt.xlabel('Date')
        plt.ylabel('Adjusted closing price ($)')
        plt.title('Price with three Simple Moving Average')
        plt.legend()
        plt.show();
     
     
    elif select==10:
        close=data[0]["Adj Close"]
        sma50 = close.rolling(window=50).mean()
        sma100 = close.rolling(window=100).mean()
        sma200 = close.rolling(window=200).mean()
        plt.style.use('fivethirtyeight')
        plt.figure(figsize = (16,8))
        plt.plot(close, label='SPY Adj Close', linewidth = 2)
        plt.plot(sma50, label='50 day rolling SMA', linewidth = 2)
        plt.xlabel('Date')
        plt.ylabel('Adjusted closing price ($)')
        plt.title('Price with a single Simple Moving Average')
        plt.legend()
        plt.show();
         
        plt.style.use('fivethirtyeight')
        plt.figure(figsize = (16,8))
        plt.plot(close, label='SPY Adj Close', linewidth = 2)
        plt.plot(sma100, label='100 day rolling SMA', linewidth = 2)
        plt.xlabel('Date')
        plt.ylabel('Adjusted closing price ($)')
        plt.title('Price with a single Simple Moving Average')
        plt.legend()
        plt.show();
        
        plt.style.use('fivethirtyeight')
        plt.figure(figsize = (16,8))
        plt.plot(close, label='SPY Adj Close', linewidth = 2)
        plt.plot(sma200, label='200 day rolling SMA', linewidth = 2)
        plt.xlabel('Date')
        plt.ylabel('Adjusted closing price ($)')
        plt.title('Price with a single Simple Moving Average')
        plt.legend()
        plt.show();
        
        plt.style.use('fivethirtyeight')
        plt.figure(figsize = (16,8))
        plt.plot(close, label='SPY Adj Close', linewidth = 2)
        plt.plot(sma50, label='50 day rolling SMA', linewidth = 2)
        plt.plot(sma100, label='100 day rolling SMA', linewidth = 2)
        plt.plot(sma200, label='200 day rolling SMA', linewidth = 2)
        plt.xlabel('Date')
        plt.ylabel('Adjusted closing price ($)')
        plt.title('Price with three Simple Moving Average')
        plt.legend()
        plt.show();
    
    
    elif select==11:
        for x in range(0,len(data)):
            data[x]["Returns"]=data[x]['Close'].pct_change(1)
            data[x]['Returns'].hist(bins=100,figsize=(16,8))
            plt.xlabel('Date')
            plt.ylabel('Returns ($)')
            plt.title(on[x])
            plt.show()
        for x in range(0,len(data)):
            data[x]["Returns"]=data[x]['Close'].pct_change(1)
            data[x]['Returns'].hist(bins=100,label=on[x],figsize=(16,8),alpha=0.5)
        plt.legend()        

    
    elif select==12:
        for x in range(0,len(data)):
            data[x]["Returns"]=data[x]['Close'].pct_change(1)
            data[x]['Cumulative Return']=(1+data[x]['Returns']).cumprod()
            data[x]['Cumulative Return'].plot(label=on[x],figsize=(16,8),title='CUMULATIVE RETURN')
        plt.legend();
    
    
    elif select==13:
        for i in range(0,len(data)):
            data[i]['20 Day MA'] = data[i]['Adj Close'].rolling(window=20).mean()
            data[i]['20 Day STD'] = data[i]['Adj Close'].rolling(window=20).std()
            data[i]['Upper Band'] = data[i]['20 Day MA'] + (data[i]['20 Day STD'] * 2)
            data[i]['Lower Band'] = data[i]['20 Day MA'] - (data[i]['20 Day STD'] * 2)
            data[i][['20 Day MA','20 Day STD','Upper Band','Lower Band']].plot(figsize=(16,8),title='Bollinger Bands Of '+on[i])
        plt.legend()
        plt.show(block=False)
    
    else:
        print("\nWRONG INPUT OUT OF THE OPTIONS!!!\n PLEASE TRY AGAIN\n")
        
        
    choose=input("\nDO YOU WANT TO CONTINUE AND USE MORE TECHNICAL INDICATORS\n 1. y/Y for yes\n 2. n/N for NO\n")
    if choose=='N' or choose=='n':
        break;


print("\n\n********************HAPPY INVESTING!!!********************\n")