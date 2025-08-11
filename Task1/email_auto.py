import smtplib

sender_email = input('Sender mail: ')
receriver_mail = input('Receiver mail:')
app_password = 'xlgj fcgi vrgu lxdo'
subject = input('Subject: ')

messages = [
    'Hi, just following up meeting up today. I have attach the docs.',
    'This is a friendly reminder that our event is happening tomorrow.',
    'Hope you are having a great morning',
    'if you didnot make any changes plz contact the company']

try:
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(sender_email, app_password)

    for i, msg in enumerate(messages):
        text = f'Subject: {subject} \n {msg}'
        server.sendmail(sender_email, receriver_mail, text)
        print(f'Email {i + 1} has been send to {receriver_mail}.')

except:
    print('Error Occured!')
finally:
    server.quit()