from fileinput import filename
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

msg=MIMEMultipart()

sender_mail=input("Enter sender mail-id:")
msg['Subject']=input("Enter subject:")
body=input("Enter the message here:")
msg.attach(MIMEText(body,'plain'))
msg['From']=sender_mail
reciever_mail=input("Enter receiver email id:")
msg['To']=reciever_mail
password=input("Enter your gmail password:")

filename='log_file'
attachment=open(filename,'rb')
p=MIMEBase('application','octet-stream')
p.set_payload((attachment).read())
encoders.encode_base64(p)
p.add_header('Content-Disposition',"attachment;filename=%s"%filename)
msg.attach(p)

server=smtplib.SMTP_SSL("smtp.gmail.com",465)
#server.starttls()

server.login(sender_mail,password)
text=msg.as_string()
server.sendmail(sender_mail,reciever_mail,text)
server.quit()