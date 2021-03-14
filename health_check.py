#!/usr/bin/env python3

import shutil
import psutil
import socket
import emails

SENDER = "automation@example.com"
RECIPTENT = "student-01-94cdf5ef3fb7@example.com"
BODY = "Please check your system and resolve the issue as soon as possible."

def check_cpu_usage():
  if psutil.cpu_percent() >= 80:
    message =  emails.generate_error_report(SENDER, RECIPTENT, "Error - CPU usage is over 80%", BODY)
    emails.send_email(message)

def check_disk_usage():
  available = shutil.disk_usage("/").free/shutil.disk_usage("/").total * 100
  if available < 20:
    message = emails.generate_error_report(SENDER, RECIPTENT, "Error - Available disk space is less than 20%", BODY)
    emails.send_email(message)

def check_ram_usage():
  available = psutil.virtual_memory().available/1024/2024
  if available < 500:
    message = emails.generate_error_report(SENDER, RECIPTENT, "Error - Available memory is less than 500MB", BODY)
    emails.send_email(message)

def check_localhost():
  check = socket.gethostbyname('localhost')
  if check != '127.0.0.1':
    message = emails.generate_error_report(SENDER, RECIPTENT, "Error - localhost cannot be resolved to 127.0.0.1", BODY)
    emails.send_email(message)

def main():
  check_cpu_usage()
  check_disk_usage()
  check_ram_usage()
  check_localhost()

if __name__ == "__main__":
  main()
