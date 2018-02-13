'''
How to run:
Needs python shell.
1. import <me>
    `from mailDropper.sendmail import mail_Dropper`
2. Instatitate to verify and establish connection
    `md_obj = mail_Dropper("<sender_email_id>", "<sender_email_password>")`
3. Start sending mails
    `md_obj.process_csv("<absolute file path>")`

'''

import smtplib
import csv
import sys
import getpass
import os
import string 

class mail_Dropper(object):
    """docstring for mail_Dropper"""
    def __init__(self, *args):
        # super(mail_Dropper, self).__init__()
        self.args = args
        self.SMTPserver = 'smtp.gmail.com'
        try:
            print "\nValidating arguments. Please wait.... "
            validation_result = self.validate_args()
            if validation_result:
                print " Success!"
                print "\nEstablishing SMTP connection..."
                self.server_conn = smtplib.SMTP()
                self.server_conn.connect(self.SMTPserver)
                self.server_conn.starttls()
                self.server_conn.verify(self.sender_email)
                self.server_conn.login(self.sender_email, self.sender_pswd)
                print " Success!"

        except Exception as constructor_err:
            print 'Please enter a valid arguments'
            sys.exit()

    def validate_args(self):
        args_length = len(self.args)
        if args_length:
            if args_length == 2:
                self.sender_email = self.args[0] 
                self.sender_pswd = self.args[1] 
                return True
        print "Please enter email and password"
        return False


    def maildropper(self,user_dataset):
        mail_body = string.join((
            "From: %s" % self.sender_email,
            "To: %s" % user_dataset['EMAIL'],
            "Subject: %s" % user_dataset['SUBJECT'] ,
            "\nDear %s," % user_dataset['NAME'],"\n %s" % user_dataset['CONTENT'], 
            ), "\r\n")
        print "\n ----- Mail body BEGINS here ----"
        print mail_body
        print "\n ----- Mail body ENDS here ----"
        self.server_conn.sendmail(self.sender_email, [user_dataset['EMAIL']], mail_body)

    def process_csv(self):
        try:
            self.server_conn.ehlo()
        except Exception as e:
            print "The connection seems to be closed. Please re-establish."
            sys.exit()
        try:
            self.data_set_fp = raw_input('Enter ABSOLUTE csv file path: ')
            with open(self.data_set_fp) as csvfile:
                dataset = csv.DictReader(csvfile)
                print "\n Sending Email Notifications initiated."
                for user_data in dataset:
                    self.maildropper(user_data)
            print "\n Sending Email Notifications finished."
            self.close_conn = raw_input("Enter c/C to continue processing another data-set or anyother key to close the connection.")
            if self.close_conn not in ['c', 'C']:
                self.server_conn.quit()
            else:
                self.process_csv()
        except Exception as data_processing_err:
            print "\n Something went wrong. Please try again"
            self.process_csv()
            pass

    # sender_email = raw_input('Enter FROM email address: ')
    # sender_pswd = getpass.getpass("Please enter your password:")
