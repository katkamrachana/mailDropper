'''
How to run:
In python shell.
1. import <me>
    `from mailDropper.sendmail import mail_Dropper`
2. Instatitate to verify and establish connection
    `md_obj = mail_Dropper()`

'''
import json
import smtplib
import csv
import sys

class mail_Dropper(object):
    """
    Establishes SMTP connection with sender credentials.
    """
    def __init__(self, *args):
        super(mail_Dropper, self).__init__()
        self.args = args
        self.SMTPserver = 'smtp.gmail.com'
        try:
            print("Valid arguments.")
            print("\nEstablishing SMTP connection...")
            self.server_conn = smtplib.SMTP()
            self.server_conn.connect(self.SMTPserver)
            self.server_conn.starttls()
            self.validate_credentials()
            print("Successfully established connection.")
        except Exception as e:
            print('ValidationError: Please enter valid arguments', e)
            sys.exit()

    def validate_credentials(self):
        self.cred_file_path = raw_input('Please enter Absolute file path of credentials.json: ')
        #load json file and read email and pwd
        try:
            with open(self.cred_file_path) as cred_in:
                print("\nValidating credentials. Please wait.")
                self.cred_dict = json.loads(cred_in.read())
                self.sender_email = self.cred_dict.get("email") 
                self.sender_pswd = self.cred_dict.get("password")
                self.server_conn.verify(self.sender_email)
                self.server_conn.login(self.sender_email, self.sender_pswd)
                self.process_csv()
                return True
        except Exception as e:
            print('ValidationError: Please input valid credentials',e)
            sys.exit()

    def maildropper(self,user_dataset):
        mail_body = "From: {} \nTo: {} \nSubject: {}\nDear {},\n{}" .format(self.sender_email, user_dataset['EMAIL'], user_dataset['SUBJECT'], user_dataset['NAME'], user_dataset['CONTENT'])
        self.server_conn.sendmail(self.sender_email, [user_dataset['EMAIL']], mail_body)

    def process_csv(self):
        try:
            self.server_conn.ehlo()
        except Exception as e:
            print("The connection seems to be closed. Please re-establish.")
            sys.exit()
        try:
            self.data_set_fp = raw_input('Please enter Absolute file path of dataset(csv): ')
            with open(self.data_set_fp) as csvfile:
                dataset = csv.DictReader(csvfile)
                print("\n Sending Email Notifications initiated.")
                for user_data in dataset:
                    self.maildropper(user_data)
            print("\n Sending Email Notifications finished.")
            self.close_conn = raw_input("Enter c/C to continue processing another data-set or anyother key to close the connection.")
            if self.close_conn not in ['c', 'C']:
                self.server_conn.quit()
            else:
                self.process_csv()
        except Exception as data_processing_err:
            print("\n Something went wrong. Please try again")
            self.process_csv()
            pass
