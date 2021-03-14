#!/usr/bin/python3
from email.message import EmailMessage
import os
import mimetypes
import smtplib

def generate_email(sender, reciptent, subject, body, attachment):
  message = EmailMessage()
  message["From"] = sender
  message["To"] = reciptent
  message["Subject"] = subject
  message.set_content(body)
  attachment_path = attachment
  attachment_filename = os.path.basename(attachment_path)
  mime_type, _ = mimetypes.guess_type(attachment_path)
  mime_type, mime_subtype = mime_type.split('/', 1)
  with open(attachment, 'rb') as ap:
    message.add_attachment(ap.read(),maintype=mime_type,subtype=mime_subtype,filename=os.path.basename(attachment))
  return message

def generate_error_report(sender, reciptent, subject, body):
  message = EmailMessage()
  message["From"] = sender
  message["To"] = reciptent
  message["Subject"] = subject
  message.set_content(body)
  return message

def send_email(message):
  mail_server = smtplib.SMTP("localhost")
  mail_server.send_message(message)
  mail_server.quit()
