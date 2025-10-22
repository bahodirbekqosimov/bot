from datetime import datetime as dt

def writer(value):
    now = dt.now().strftime('%Y/%m/%d  %H:%M')
    print(now)
    with open("console.log","a+") as f:
        f.write(f"[{now}] -> {value}\n")
    

