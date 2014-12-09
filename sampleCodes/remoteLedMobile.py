import os
import glob
import mimetypes 
from email import encoders
from email.mime.audio import MIMEAudio
from email.mime.base import MIMEBase
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def attach_files(msg, attachements):
  for attachment in attachments:
    attachment = attachment.strip()
    for path in glob.glob(attachment):
      filename = os.path.basename(path)
      if not os.path.isfile(path):
        continue
      # Guess the content type based on the file's extension.  Encoding
      # will be ignored, although we should check for simple things like
      # gzip'd or compressed files.
      ctype, encoding = mimetypes.guess_type(path)
      if ctype is None or encoding is not None:
        # No guess could be made, or the file is encoded (compressed), so
        # use a generic bag-of-bits type.
        ctype = 'application/octet-stream'
      maintype, subtype = ctype.split('/', 1)
      if maintype == 'text':
        fp = open(path)
        # Note: we should handle calculating the charset
        part = MIMEText(fp.read(), _subtype=subtype)
        fp.close()
      elif maintype == 'image':
        fp = open(path, 'rb')
        part = MIMEImage(fp.read(), _subtype=subtype)
        fp.close()
      elif maintype == 'audio':
        fp = open(path, 'rb')
        part = MIMEAudio(fp.read(), _subtype=subtype)
        fp.close()
      else:
        fp = open(path, 'rb')
        part = MIMEBase(maintype, subtype)
        part.set_payload(fp.read())
        fp.close()
        # Encode the payload using Base64
        encoders.encode_base64(part)
      # Set the filename parameter
      part.add_header('Content-Disposition', 'attachment', filename=filename)
      msg.attach(part)

def sendemail(email_name, email_user, email_pswd, mailto, subject, body, attachments):
  import smtplib

  # DON'T CHANGE THIS!
  # ...unless you're rewriting this script for your own SMTP server!
  smtp_server = 'smtp.gmail.com'
  smtp_port = 587

  # Build an SMTP compatible message
  msg = MIMEMultipart()
  msg['Subject'] = subject
  msg['To'] = mailto
  msg['From'] = email_name + " <" + email_user + ">"
  msg.attach(MIMEText(body, 'plain'))
  attach_files(msg, attachments)

  # Attempt to connect and send the email
  try:
    smtpObj = '' # Declare within this block.
    # Check for SMTP over SSL by port number and connect accordingly
    if( smtp_port == 465):
      smtpObj = smtplib.SMTP_SSL(smtp_server,smtp_port)
    else:
      smtpObj = smtplib.SMTP(smtp_server,smtp_port)
    smtpObj.ehlo()
    # StartTLS if using the default TLS port number
    if(smtp_port == 587):
      smtpObj.starttls()
      smtpObj.ehlo
    # Login, send and close the connection.
    smtpObj.login(email_user, email_pswd)
    smtpObj.sendmail(email_user, mailto, msg.as_string())
    smtpObj.close()
    return 1  # Return 1 to denote success!
  except Exception, err:
    # Print error and return 0 on failure.
    print err
    return 0

import sys
import android

droid = android.Android()

email_name = "Your Name"
email_user = "emailid@gmail.com"
email_pswd = "password"
mailto = "emailid@gmail.com"
subject = "LED"
attachments = ''

body = droid.recognizeSpeech().result


if (sendemail(email_name, email_user, email_pswd, mailto, subject, body, attachments)):
      sys.exit(0)
else:
      droid.makeToast("Failed to send email")
  
