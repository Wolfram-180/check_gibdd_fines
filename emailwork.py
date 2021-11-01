import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.utils import formatdate

# smtp acc
_server = 'smtp.'
_user = ''
_pass = ''


def send_mail(send_to, subject, text, user=_user, server=_server, __pass=_pass):
    try:
        msg = MIMEMultipart()
        msg['From'] = user
        msg['To'] = send_to
        msg['Date'] = formatdate(localtime=True)
        msg['Subject'] = subject
        msg['Content-Type'] = "text/html; charset=utf-8"
        msg.attach(MIMEText(text))

        smtp = smtplib.SMTP(server, 587)
        smtp.login(user, __pass)
        smtp.sendmail(user, send_to, msg.as_string())
        smtp.close()

        return True
    except Exception as exc:
        print("send_mail: {} \n {} \n {} \n".format(type(exc), exc.args, exc))
        return False


