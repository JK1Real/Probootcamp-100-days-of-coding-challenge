import smtplib
from email.message import EmailMessage

def send_emial(result):
    Name = result['name']
    Email = result['email']
    Phone_No = result['phone']
    Message = result['message']
    
    msg = EmailMessage()
    msg['Subject'] = "New Message"
    msg['From'] = 'thisisnotallowed384@gmail.com'
    msg['To'] = 'thisisnotallowed384@gmail.com'
    msg.preamble = 'Hello How are you.\n'
    msg.set_content(f'Name:{Name}\n'
                    f'Email   :   {Email}\n'
                    f'Phone No:{Phone_No}\n'
                    f'Message:{Message}\n')
    

    # SMTP configuration for Gmail
    smtp_server = 'smtp.gmail.com'
    smtp_port = 587
    username = 'thisisnotallowed384@gmail.com'  # Replace with your Gmail username
    password = 'kwsr ypcf qnbc fzxl'  # Replace with your Gmail password

    # Sending the email
    try:
        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls()  # Secure the connection
            server.login(username, password)  # Login to the SMTP server
            server.send_message(msg)  # Send the email
            print("Email sent successfully")
    except Exception as e:
        print(f"Failed to send email: {e}")