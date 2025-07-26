import smtplib
import ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def send_alert(subject, message_dict):
    """Send an alert email with the specified subject and message using Gmail."""
    sender_email = "username@gmail.com"  # Replace with your Gmail address
    receiver_email = "username@gmail.com"  # Replace with recipient email address
    password = "*****************"  # Replace with your Gmail password or app-specific password

    # Create a well-organized message string from the dictionary
    message_lines = [f"{key}: {value}" for key, value in message_dict.items()]
    message = "\n".join(message_lines)

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
        print(f"Alert sent: {subject}")
    except Exception as e:
        print(f"Failed to send alert: {e}")

# Usage example with a dictionary
alert_data = {
    "Error Type": "Connection Timeout",
    "Error Code": 504,
    "Timestamp": "2024-08-25 12:34:56",
    "Description": "The server did not respond in time."
}


send_alert("Server Alert", alert_data)

