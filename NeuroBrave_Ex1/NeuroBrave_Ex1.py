from pynput.mouse import Listener
import os
import json
import smtplib, ssl
import time

boolfindjson = 1  # if no .json file exist
filesinDirectory = os.listdir()  # Read files in directory
for files in filesinDirectory:  # run on files in directory
    if str(files).find('.json') > 0:  # Check if there is a .json file
        boolfindjson = 0
        with open(files) as f:  # Read .json file
            data = json.load(f)

if boolfindjson:  # If no .json file found
    print("No suitable .json file")
    import sys

    sys.exit()  # stop executing


def on_move(x, y):  # if mouse moves on screen
    print('Pointer moved to {0}'.format((x, y)))
    if float(data['x1']) < x < float(data['x2']) \
            and float(data['y1']) < y < float(data['y2']):  # If mouse is in rectangle
        sendEmail()
        time.sleep(30)


def sendEmail():  # sends email
    port = 587  # For starttls
    smtp_server = "smtp.gmail.com"
    sender_email = "nircaf2@gmail.com"
    receiver_email = data['target_email']  # get target email from .json file
    password = "nir159Caf"
    message = """\ 
    Subject: Hi NeuroBrave

    This message is sent from Python."""  # Email message

    context = ssl.create_default_context()
    with smtplib.SMTP(smtp_server, port) as server:
        server.ehlo()  # Can be omitted
        server.starttls(context=context)
        server.ehlo()  # Can be omitted
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, message)
    print("Email sent from {0} to {1}".format(sender_email, receiver_email))


# Collect events until released
with Listener(  # Refreshes mouse move
        on_move=on_move,
) as listener:
    listener.join()
