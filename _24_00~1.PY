
import smtplib, os
# import datetime
# One of the biggest errors is manually typing things out into the strings above, instead of just imported them into the code.


my_email1 = os.environ.get('my_email1')    #the API Key from the open weather website
print(f"my_email1 is: {my_email1}")

password = os.environ.get('password')    #the API Key from the open weather website
print(f"password is: {password}")

that_other_email3 = os.environ.get('that_other_email3')    #the API Key from the open weather website
print(f"that_other_email3 is: {that_other_email3}")

subject = "Subject:Greetings! This is the Subject1\n\n"
body = "The best way to succeed in this world is to act on the advice you give to others. -Unknown. Also, This is the Body1"

# connection.sendmail(from_addr=my_email1, to_addrs=their_email2, msg="Subject:Greetings, this is the Subject\n\nThe best way to succeed in this world is to act on the advice you give to others. -Unknown. This is the Body")

with smtplib.SMTP("smtp.gmail.com", port=587) as connection: # allows us to connect to our email provider's SMTP email server, and create an Object from the .SMTP(Class), location of the server (gmail = smtp.gmail.com)
    connection.starttls()   #tls = Transport Layer Security, a way of securing our connection to our email server. (encrypted and secure)) (indent block starts here)
    connection.login(user=my_email1, password=password)
    connection.sendmail(from_addr=my_email1,
                        to_addrs=that_other_email3,
                        msg=f"{subject}{body}")    # (indent block ends here.)
