from datetime import datetime as dt

def writer(vale):
    now = dt.now().strftime('%Y/%m/%d  %H:%M')
    print(now)
    
    
writer()