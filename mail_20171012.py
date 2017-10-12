from email.mime.text import MIMEText
import smtplib
import logging

subject = "测试"
content = "这是小黑发送的测试邮件"
msg_from = "215603651@qq.com"
# msg_to = "204893985@qq.com"
password = "uwgwbarofitvbgfg"

msg_1 = MIMEText(content)
msg_1['Subject'] = subject
msg_1['From'] = msg_from
msg_1['To'] = msg_to

# msg_1 = MIMEText("这是小黑发送的测试邮件","plain","utf-8")

try:
    s = smtplib.SMTP_SSL("smtp.qq.com",465)
    s.login(msg_from,password)
    s.sendmail(msg_from,msg_to,msg_1.as_string())
    logging.info("发送成功")
except s.SMTPException as e:
    logging.error("发送失败")
finally:
    s.quit()



