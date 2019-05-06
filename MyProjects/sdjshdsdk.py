import smtplib
from email import encoders
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
email='prasadnaidu766@gmail.com'
to_emails="prasadlegend766@gmail.com"
password='njzgvtdzgjruayoa'
subject='python'
msg=MIMEMultipart()
msg['From']=email
msg['To']=to_emails
msg['Subject']=subject
server=smtplib.SMTP('smtp.gmail.com',587)
server.starttls()
server.login(email,password)
message="Hi prasad this is python Message"
msg.attach(MIMEText(message,'plain'))
filname="media\\prasad\\1.jpg"
attachment=open(filname,'rb')       
part=MIMEBase('application','octet-stream')
part.set_payload((attachment).read())
encoders.encode_base64(part)
part.add_header('Context-Dispositioon','attachment; filename='+filname)
msg.attach(part)

text=msg.as_string()
server.sendmail(email,to_emails,text)
server.quit()  