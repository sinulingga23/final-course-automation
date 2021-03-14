#!/usr/bin/python3

import os
import datetime

from reportlab.platypus import SimpleDocTemplate
from reportlab.platypus import Paragraph, Spacer, Table, Image
from reportlab.lib.styles import getSampleStyleSheet

def generate_report(attachment, title, paragraph):
  descriptions = os.listdir('supplier-data/descriptions')
  styles = getSampleStyleSheet()
  report = SimpleDocTemplate(attachment)
  report_title = Paragraph(title, styles["h1"])
  report_body = Paragraph(paragraph)
  report.build([report_title, report_body])
