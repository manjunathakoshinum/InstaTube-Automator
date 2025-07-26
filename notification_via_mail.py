import smtplib
import ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import os
import logging

def send_alert(subject, message):
    """Send an alert email with the specified subject and message using Gmail."""
    sender_email = "username@gmail.com"  # Replace with your Gmail address
    receiver_email = "username@gmail.com"  # Replace with recipient email address
    password = "#####################"  # Replace with your Gmail password or app-specific password

    # Set up the email message
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = receiver_email
    msg['Subject'] = subject

    msg.attach(MIMEText(message, 'plain'))

    # Set up the SMTP server and send the email
    try:
        context = ssl.create_default_context()
        with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as server:
            server.login(sender_email, password)
            server.sendmail(sender_email, receiver_email, msg.as_string())
        logging.info(f"Alert sent: {subject}")
    except Exception as e:
        logging.error(f"Failed to send alert: {e}")

# Usage example
send_alert("Test Alert", "This is a test message.")
