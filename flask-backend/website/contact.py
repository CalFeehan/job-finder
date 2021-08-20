import smtplib
import os


def send_email(contact_name: str, contact_email: str, contact_company: str, contact_phone: str, contact_interest: str, contact_message: str) -> bool:

    msg = f'''New message from Job Finder Website. 
    Name: {contact_name}, 
    Email: {contact_email}, 
    Company: {contact_company}, 
    Phone: {contact_phone}, 
    Interest: {contact_interest},
    Message: {contact_message}'''
    message = f"""From: Callum Feehan <{os.getenv('GOOGLE_USER')}>
    To: Callum Feehan <{os.getenv('HOTMAIL')}>
    Subject: Job Finder Contact Form

    {msg}
    """
    try:
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(os.getenv('GOOGLE_USER'), os.getenv('GOOGLE_PASS'))
        server.sendmail(os.getenv('GOOGLE_USER'),
                        "feehan07@hotmail.co.uk", message)
        server.quit()
        return True
    except:
        return False
