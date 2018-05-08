#-*- coding=utf-8 -*-
import smtplib
from email.mime.text import MIMEText
msg_from='zhaoming0018@126.com'             
passwd='13852274170'                          
msg_to='1786796646@qq.com'           
                            
subject = "python"
content = "123456"
msg = MIMEText(content)
msg['Subject'] = subject
msg['From'] = msg_from
msg['To'] = msg_to
s = smtplib.SMTP("smtp.126.com",25)
s.login(msg_from, passwd)
s.sendmail(msg_from, msg_to, msg.as_string())
print("发送成功")