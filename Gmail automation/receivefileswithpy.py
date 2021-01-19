import imaplib
import getpass
mail= imaplib.IMAP4_SSL("imap.gmail.com")

em=getpass.getpass(prompt="Email: ")
password =getpass.getpass(prompt="Enter password: ")
mail.login(em,password)
mail.select('inbox')
typ, data= mail.search(None, 'FROM aishani.pachauri@gmail.com' )
print("\n{}".format(typ))

find_first_of_that_type= data[0][1]
print(find_first_of_that_type)
res, first_data= mail.uid('fetch',str(data[0][1]),"(RFC822)") #Second argument is protocol to call string
raw=first_data[0][1]
raw_email_string = raw.decode('utf-8')
import email
email_message = email.message_from_string(raw_email_string)
for part in email_message.walk():
    if part.get_content_type() == "text/plain":
        body = part.get_payload(decode=True)
        print(body)
