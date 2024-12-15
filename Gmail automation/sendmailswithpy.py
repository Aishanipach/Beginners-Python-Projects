#smtp server (simple mail transfer protocol)
import smtplib
import stdiomask  #stdiomask is use for displaying a character instead of echoing the entered character.

smtp_obj= smtplib.SMTP('smtp.gmail.com',587) #You can use 465 (ssl call) and skip starttls() call in that case 
smtp_obj.ehlo()
smtp_obj.starttls()

email= input("Email: ")
password = stdiomask.getpass(prompt="Enter password: ", mask="*")  # using stdiomask to display "*" instead of the entered password
print(smtp_obj.login(email,password))
from_address= email
to_address= email
subject=input("Enter sub ")
message=input("Enter body ")
msg= "Subject: "+subject +'\n' +message

smtp_obj.sendmail(from_address, to_address, msg)
