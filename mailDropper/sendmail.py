'''
Sample run command: python sendmail.py /home/rbk/rachana/Documents/data_sets/dataset.csv
What is maildropper?
    - It sends mail in bulk reading through a dataset.
    - It lands mails in inbox, not spam!
How does maildropper work?
    1. Asks to input from-email address and password.
    2. Verifies validity of from-email address and proceeds only on success.
    3. Reads dataset.csv having columns:
        EMAIL|NAME|SUBJECT|CONTENT
    4. Sends mail in following pattern:
        Dear <NAME>,
            <CONTENT>
'''

import smtplib
import csv
import sys
import getpass
import os
import string 

SMTPserver = 'smtp.gmail.com'

# sender_email = raw_input('Enter FROM email address: ')

try:
    # sender_pswd = getpass.getpass("Please enter your password:")
    server_conn = smtplib.SMTP()
    server_conn.connect(SMTPserver)
    server_conn.starttls()
    server_conn.verify("katkam.rachana@gmail.com")
    server_conn.login("katkam.rachana@gmail.com", "anahcar2419")

except Exception as ee:
    print ee
    print 'Please enter a valid email address'
    sys.exit()


def maildropper(user_dataset):
    mail_body = string.join((
        "From: rachana.katkam@tiss.edu",
        "To: %s" % user_dataset['EMAIL'],
        "Subject: %s" % user_dataset['SUBJECT'] ,
        "\nDear %s," % user_dataset['NAME'],"\n %s" % user_dataset['CONTENT'], " with server: %s" % SMTPserver, 
        ), "\r\n")
    server_conn.sendmail("rachana.katkam@tiss.edu", [user_dataset['EMAIL']], mail_body)

def process_csv(filepath):
    with open(filepath) as csvfile:
        dataset = csv.DictReader(csvfile)
        for user_data in dataset:
            maildropper(user_data)

if __name__ == "__main__":
    if len(sys.argv) == 2:
        data_set_fp = sys.argv[1]
        if os.path.exists(data_set_fp):
            process_csv(data_set_fp)
            server_conn.quit()
        else:
            print "\n Please enter absolute path of csv file"
    else:
        print "Please enter data-set(.csv) filepath"
