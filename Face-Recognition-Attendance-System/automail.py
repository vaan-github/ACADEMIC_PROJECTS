import yagmail
import os
import datetime
import Info
import pandas as pd
import numpy as np

date = datetime.date.today().strftime("%B %d, %Y")
path = 'C:\\Users\\ray\\Desktop\\Face-Recognition-Attendance-System\\Attendance'
os.chdir(path)
files = sorted(os.listdir(os.getcwd()), key=os.path.getmtime)
df = pd.read_csv('C:\\Users\\ray\\Desktop\\Face-Recognition-Attendance-System\\StudentsDetails\\StudentsDetails.csv')   
        
receivers = df['Email']
newest = files[-1]
filename = newest
sub = "Attendance Report for " + str(date)
body = " Attendance Submitted."

for receiver in receivers:
    # mail information
    if pd.isnull(receiver):
        continue
    else:
        yag = yagmail.SMTP(Info.EMAIL_ID, Info.PASSWORD)

        # sent the mail
        yag.send(
            to=receiver,
            subject=sub, # email subject
            contents=body,  # email body
            attachments= filename  # file attached
        )
        print("Email Sent to "+receiver)