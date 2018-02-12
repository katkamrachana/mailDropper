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

class mail_Dropper(object):
    """docstring for mail_Dropper"""
    def __init__(self, arg):
        super(mail_Dropper, self).__init__()
        self.arg = arg
        
        self.SMTPserver = 'smtp.gmail.com'
        try:
            validation_result = self.validate_args()
            if validation_result:
                self.server_conn = smtplib.SMTP()
                self.server_conn.connect(self.SMTPserver)
                self.server_conn.starttls()
                self.server_conn.verify(self.sender_email)
                self.server_conn.login(self.sender_email, self.sender_pswd)
        except Exception as ee:
            print ee
            print 'Please enter a valid arguments'
            sys.exit()

    def validate_args(self):
        args_length = len(self.arg)
        if args_length:
            if args_length == 3:
                self.sender_email = self.arg[0] 
                self.sender_pswd = self.arg[1] 
                self.data_set_fp = self.arg[2] 
                return True
        else:
            print "Please enter csv file name"
            return False


    def maildropper(self,user_dataset):
        mail_body = string.join((
            "From: %s" % self.sender_email,
            "To: %s" % user_dataset['EMAIL'],
            "Subject: %s" % user_dataset['SUBJECT'] ,
            "\nDear %s," % user_dataset['NAME'],"\n %s" % user_dataset['CONTENT'], " with server: %s" % SMTPserver, 
            ), "\r\n")
        self.server_conn.sendmail(self.sender_email, [user_dataset['EMAIL']], mail_body)

    def process_csv(self):
        with open(self.data_set_fps) as csvfile:
            dataset = csv.DictReader(csvfile)
            for user_data in dataset:
                self.maildropper(user_data)
        self.server_conn.quit()

    # sender_email = raw_input('Enter FROM email address: ')
    # sender_pswd = getpass.getpass("Please enter your password:")
