#!/usr/bin/env python3

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Define variables
EMAIL_LIST = "email_addresses.txt"
SUBJECT = "Resume for AWS DevOps Engineer"
BODY = """Hi,

PFA resume.

First Name:   Sachin
Last Name:    Maniyar
Contact No:   7990505920
Current Location:   Bangalore
Total Experience:   3.4 years
Relevant Experience:  3.4 years
Company Name:  Cognizant
Designation:   Associate
Notice Period:   Serving Notice Period(LWD - 17th May 2024)
Tech Stack : AWS, Devops, Docker, Kubernetes, Jenkins, Version Control, CFT, Python.

Thanks & Regards,
Sachin"""
ATTACHMENT = "Resume_Sachin_Maniyar_DevOps.pdf"
SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587
GMAIL_USERNAME = "sachinmaniyar3@gmail.com"
GMAIL_PASSWORD = "password"

# Function to send email
def send_email(email, attachment):
    try:
        # Create message container
        msg = MIMEMultipart()
        msg["From"] = GMAIL_USERNAME
        msg["To"] = email
        msg["Subject"] = SUBJECT

        # Attach body
        msg.attach(MIMEText(BODY, "plain"))

        # Attach attachment
        with open(attachment, "rb") as file:
            part = MIMEBase("application", "octet-stream")
            part.set_payload(file.read())
        encoders.encode_base64(part)
        part.add_header("Content-Disposition", f"attachment; filename= {attachment}")
        msg.attach(part)

        # Connect to SMTP server and send email
        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            server.starttls()
            server.login(GMAIL_USERNAME, GMAIL_PASSWORD)
            server.send_message(msg)

        logging.info(f"Email sent successfully to: {email}")
    except Exception as e:
        logging.error(f"Failed to send email to: {email}")
        logging.error(f"Error: {str(e)}")

# Read email addresses from file and send emails
logging.info("Starting email sending process...")
with open(EMAIL_LIST, "r") as file:
    for line in file:
        email = line.strip()
        send_email(email, ATTACHMENT)

logging.info("Email sending process completed.")