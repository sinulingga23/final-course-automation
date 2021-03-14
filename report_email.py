#!/usr/bin/env python3

import os
import reports
from datetime import date
import emails

def generate_pdf():
  descriptions = os.listdir("supplier-data/descriptions")
  body_pdf = "<br/>"
  for desc in descriptions:
    with open('supplier-data/descriptions/'+desc, mode='r') as opened:
      temp = opened.readlines()
      body_pdf += "name: " + temp[0].strip() + "<br/>"
      body_pdf += "weight: " + temp[1].strip()
      body_pdf += "<br/><br/>"
      opened.close()
  attachment = "/tmp/processed.pdf"
  today = date.today()
  d2 = today.strftime("%B %d, %Y")
  title = "Processed Update on " + d2
  paragraph = body_pdf
  reports.generate_report(attachment, title, paragraph)

def main():
  generate_pdf()

  sender = "automation@example.com"
  reciptent = "student-01-94cdf5ef3fb7@example.com"
  subject = "Upload Completed - Online Fruit Store"
  body = "All fruits are uploaded to our website successfully. A detailed list is attached to this email."
  attachment = "/tmp/processed.pdf"
  message = emails.generate_email(sender, reciptent, subject, body, attachment)
  emails.send_email(message)

if __name__ == "__main__":
  main()
