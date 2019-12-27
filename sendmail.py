#!/urs/bin/python3
import smtplib
from string import Template
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def get_contacts(filename):
    """
    Return two lists names, emails containing names and email addresses
    read from a file specified by filename.
    """
    names = []
    emails = []
    with open(filename, mode='r', encoding='utf-8') as contacts_file:
        for a_contact in contacts_file:
            names.append(a_contact.split()[0])
            emails.append(a_contact.split()[1])
    return names, emails
def read_template(filename):
    """
    Returns a Template object comprising the contents of the 
    file specified by filename.
    """
    with open(filename, 'r', encoding='utf-8') as template_file:
        template_file_content = template_file.read()
    return Template(template_file_content)

if __name__ == "__main__":
    MY_ADDRESS = 'uername@gmail.com'
    PASSWORD = 'password'
    names, emails = get_contacts("mycontacts.txt")
    message_template = read_template('message.txt')
    # name = "Chuonglv"
    # email = 'lvchuong@irissec.net'
    try:
        server = smtplib.SMTP('smtp.gmail.com',587)
        server.ehlo()
        server.starttls()
        server.ehlo()
        server.login(MY_ADDRESS, PASSWORD)
        for name,email in zip(names,emails):
            message = message_template.substitute(PERSON_NAME=name.title())
            msg = MIMEMultipart() 
            msg['From']=MY_ADDRESS
            msg['To']=email
            msg['Subject']="This is TEST"
            msg.attach(MIMEText(message, 'plain'))
            text = msg.as_string()
            server.sendmail(MY_ADDRESS, email,text)
        server.quit()
        print("Mail sent")
    except:
        print('Something went wrong...')
