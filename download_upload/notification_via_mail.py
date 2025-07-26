import smtplib
import ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def error_message(receiver_email,subject, message_dict):
    """Send an alert email with the specified subject and message using Gmail."""
    sender_email = "hmanjunathah30@gmail.com"  # Replace with your Gmail address
    
    password = "vpny ajpe gmca cuzo "  # Replace with your Gmail password or app-specific password

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
        print(f"message sent: {subject}")
    except Exception as e:
        print(f"Failed to send message: {e}")

def send_alert(subject, alert_data):
    match(type):
        case 0:    
            receiver_email = "hmanjunath532@gmail.com"  # error_reciver_mail address
            subject ="Error_Report"
        case 1:
            receiver_email = "kingojyothi@gmail.com" # execution reciver_mail data
            subject = "Execution_Report"
    error_message(receiver_email,subject, alert_data)

