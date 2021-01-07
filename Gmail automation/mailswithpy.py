#smtp server (simple mail transfer protocol)
import smtplib
import getpass
smtp_obj= smtplib.SMTP('smtp.gmail.com',587)
smtp_obj.ehlo()
smtp_obj.starttls()

email= getpass.getpass(prompt="Email: ")
password =getpass.getpass(prompt="Enter password: ")
print(smtp_obj.login(email,password))
from_address= email
to_address= email
subject=input("Enter sub ")
message=input("Enter body ")
msg= "Subject: "+subject +'\n' +message

smtp_obj.sendmail(from_address, to_address, msg)