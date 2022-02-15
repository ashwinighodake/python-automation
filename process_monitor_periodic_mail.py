import psutil
import datetime
import schedule
import time
from fileinput import filename
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

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

def send_file_to_mail(filename):
    msg=MIMEMultipart()

    sender_mail='ashwini.python.testing@gmail.com'
    msg['Subject']='Log file created at:'+datetime.datetime.now().strftime("Date:%Y_%m_%d Time:%I:%M:%S %p")
    body='Details of the process which are running on your pc at time'+datetime.datetime.now().strftime("Date:%Y_%m_%d Time:%I:%M:%S %p")
    msg.attach(MIMEText(body,'plain'))
    msg['From']=sender_mail
    reciever_mail='ashwini.python.testing@gmail.com'
    msg['To']=reciever_mail
    password='______'

    attachment=open(filename,'rb')
    p=MIMEBase('application','octet-stream')
    p.set_payload((attachment).read())
    encoders.encode_base64(p)
    p.add_header('Content-Disposition',"attachment;filename=%s"%filename)
    msg.attach(p)

    server=smtplib.SMTP_SSL("smtp.gmail.com",465)
    server.login(sender_mail,password)
    text=msg.as_string()
    server.sendmail(sender_mail,reciever_mail,text)
    server.quit()

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
    send_file_to_mail(filename)
    

def main():
    print("Process Monitor with memory usage")
    listprocess=ProcessDisplay()
    schedule.every(1).minutes.do(lambda:task(listprocess))
    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__=="__main__":
    main()