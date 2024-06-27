from email.message import EmailMessage
import smtplib
import os

def send_email(email: str, subject: str, content: str):        
    message = EmailMessage() 
    message['Subject'] = subject
    message['From'] = os.getenv("EMAIL_USER") 
    message['To'] = email
    message.set_content(content)
    server = smtplib.SMTP(os.getenv("SMTP_HOST"), os.getenv("SMTP_PORT")) 
    server.ehlo() 
    server.starttls() 
    server.login(os.getenv("EMAIL_USER"), os.getenv("EMAIL_PASSWORD")) 
    server.send_message(message) 
    server.quit()
    server.close()