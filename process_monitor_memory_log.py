import psutil
import datetime
import schedule
import time
def ProcessDisplay():
    listprocess = []
    
    for proc in psutil.process_iter():
        try:
            pinfo=proc.as_dict(attrs=['pid','name','username'])
            pinfo['vms']=proc.memory_info().vms/(1024*1024)

            listprocess.append(pinfo)
        except(psutil.NoSuchProcess,psutil.AccessDenied,psutil.ZombieProcess):
            pass
    return listprocess

def task(listprocess):
    print("Current time is:",datetime.datetime.now())
    filename='log_file'+datetime.datetime.now().strftime("_%Y_%m_%d_%I_%M_%S_%p")+'.txt'
    log_file=open(filename,'wt')
    header="-"*80
    heading="********Log file Created at:"+datetime.datetime.now().strftime("Date:%Y_%m_%d Time:%I:%M:%S %p")+"*********"
    log_file.write(f'{header}"\n"{heading}"\n"{header}"\n"')
    for items  in listprocess:
        log_file.write(f'{items}"\n"')
    log_file.close()
    

def main():
    print("Process Monitor with memory usage")
    listprocess=ProcessDisplay()
    schedule.every(1).hours.do(lambda:task(listprocess))
    while True:
        schedule.run_pending()
        time.sleep(1)


if __name__=="__main__":
    main()