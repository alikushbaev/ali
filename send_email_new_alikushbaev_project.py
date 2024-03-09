# from twilio.rest import Client
# twilio_number = "+12567436668"
# my_number="+998990883881"
# client=Client("ACc37222e30197400ff05ff42739ae5925a","ob3f93e1080c8e677d52b90c3600313a")
# call=client.calls.create(url="https://demo.twilio.com/docs/voice.xml",to=my_number,from_=twilio_number)
# print(call.sid)
import smtplib
from email.mime.text import MIMEText
def send_email(message,password,sender,to,subject):
    server = smtplib.SMTP("smtp.gmail.com",587)
    server.starttls()
    try:
        server.login(sender,password)
        msg = MIMEText(message)
        msg["Subject"] = subject
        msg["To"] = to
        server.sendmail(sender,to,msg.as_string())
        print(f"send successful")
    except Exception as _ex:
        print(f"error:{_ex}")
# send_email("mr","amgxjzuoxjeacfet","iskandarovadilnoza250187@gmail.com","jamshidkushbaev@gmail.com")
