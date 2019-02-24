
**mailDropper is designed to:**
   1. Send bulk emails
   2. With a provision of variable email parameters such as - recipient name, subject and content

**How does maildropper work?**

- Log valid sender credentials. 
- Run the mailDropper script for the email recipients data.
- Parses dataset(csv format) of columns: `EMAIL|NAME|SUBJECT|CONTENT` and invokes `sendmail` for each record.
- The objective is to compose a customized email and drop it into recipient's inbox. Never spam!
