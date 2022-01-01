# Import our libraries
from imap_tools import MailBox, AND, OR
from requests import get
import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email.mime.application import MIMEApplication
from email import encoders

# Define a function that will send emails, given the email address to send to and the text of the body
def SendEmail(emailTo, subject, bodyText):
    # Set up the email
	message = MIMEMultipart("alternative")
	message["From"] = emailAddr
	message["To"] = emailTo
	message["Subject"] = subject
	message.attach(MIMEText(bodyText, "plain"))
	
    # Send the email
	context = ssl.create_default_context()
	server = smtplib.SMTP(smtpServer, 587)
	server.ehlo()
	server.starttls()
	server.ehlo()
	server.login(emailAddr, emailPass)
	server.sendmail(emailAddr, emailTo, message.as_string())
	server.quit()
	print(f"Send email = {bodyText}")

# Define all our of globabl variables
emailAddr =                                                                         # Email address to log into
emailPass =                                                                         # Password for access the email address
imapServer =                                                                        # imap server
smtpServer =                                                                        # smtp server
allowedEmails = []                                                                  # List of email addresses that we will reply to

# Next log to the mailbox via IMAP
with MailBox(imapServer).login(emailAddr, emailPass) as mb:
    # Fetch all the email that are marked as unseen, and set them as seen
    messages = mb.fetch(criteria=AND(seen=False), mark_seen=True, bulk=True)
    # Loop through all of these messages
    for msg in messages:
        print(f"message from {msg.from_}")                                          # General print statement so you can see who each email was from
        if msg.from_ in allowedEmails:                                              # If the email was someone in our allowed email address list, then we send them our public IP address
            ip = get('https://api.ipify.org').text                                  # Get the Public IC
            SendEmail(msg.from_, "IP", f"My Public IP is {ip}")                     # Send a reply email, with subject of IP and body of 'My Public IP is <IP>'
            mb.delete(msg.uid)                                                      # Next delete the original email, as it is no longer required.


    #mb.delete([msg.uid for msg in mb.fetch() if msg.from_ in allowedEmails])       # If you need to delete a group of emails based upon some criteria uncomment out this line

    #for f in mb.folder.list():                                                     # If you need to look at the folder names on the imap server, uncomment out these lines
    #    print(f)

    # Delete any emails in the Send Folder, where To contains an email from our allowed emails
    mb.folder.set('Sent')                                                           # Change folder to Sent
    messages = mb.fetch(mark_seen=True, bulk=True)                                  # Fetch all of the messages, and sent them all to as seen
    for msg in messages:                                                            # Loop through each of the messages
        print(f"message to {msg.to}")                                               # See who the message was sent to, normal in the form '(<email address> ,)'
        for ae in allowedEmails:                                                    # Since the To email address is not in the same form as our allowed email address, we can't just if msg.to in allowedEmail => delete
            if ae in msg.to:                                                        # Thus we check if each allowed email address is in msg.to and if so we delete it
                mb.delete(msg.uid)
            




