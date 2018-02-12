from unittest import TestCase

from mailDropper.sendmail import mail_Dropper

class TestMail(TestCase):
    def test_sendmail(self):
        s = mail_Dropper()
        print s
        self.assertTrue(isinstance(s, basestring))