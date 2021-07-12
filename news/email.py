from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string

# EmailMultiAlternatives: responsible for sending the emails
def send_welcome_email(name,receiver):
    # Creating message subject and sender
    subject = 'Welcome to the MoringaTribune NewsLetter'
    sender = 'peter.kiru@student.moringaschool.com'

    #passing in the context vairables
    text_content = render_to_string('email/newsemail.txt',{"name": name})
    html_content = render_to_string('email/newsemail.html',{"name": name})

    msg = EmailMultiAlternatives(subject,text_content,sender,[receiver])
    msg.attach_alternative(html_content,'text/html')
    msg.send()