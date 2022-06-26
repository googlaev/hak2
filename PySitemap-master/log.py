import datetime
def log_write(name):
    now = datetime.datetime.now()
    f=open("log.txt",'a')
    date_time = now.strftime("%m/%d/%Y, %H:%M:%S")

    f.write(date_time+" "+ name+'\n')
    f.close()

def site_write(name,site):
    now = datetime.datetime.now()
    f=open(site,'a')
    date_time = now.strftime("%m/%d/%Y, %H:%M:%S")

    f.write(date_time+", "+ name+'\n')
    f.close()