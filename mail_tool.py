from google.appengine.api import mail
from random import randint

class Mailer:
    
    SENDER = "<noreply.shabb@gmail.com>"

    @staticmethod
    def send_mail(dest_list, subj_message, body):
        for dest_addr in dest_list:
            message = mail.EmailMessage(sender=Mailer.SENDER, subject=subj_message)
            message.to = "<" + dest_addr + ">"
            message.body = body
            message.send()