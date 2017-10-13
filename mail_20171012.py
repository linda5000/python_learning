import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header
from email.mime.image import MIMEImage
from email import encoders
import logging

class MailCreator:
    def __init__(self):
        self.mailserver = "smtp.qq.com"          # 邮箱服务器
        self.port = 465                            # 邮箱服务器端口
        self.mail_user = "215603651@qq.com"     # 发件人邮箱
        self.mail_pwd = "uwgwbarofitvbgfg"      # 发件人邮箱授权码


    def send(self,msg_to,subject,content,attachlist=[]):
        # 创建一个带附件的实例
        msg = MIMEMultipart()

        msg_from = self.mail_user
        pwd = self.mail_pwd

        msg['Subject'] = subject
        msg['From'] = msg_to
        msg['To'] = msg_to

        # 邮件正文内容
        text_msg = MIMEText(content,'html', 'utf-8')
        msg.attach(text_msg)
        if attachlist:
            for i in attachlist:
                # 构造附件
                with open(i, 'rb') as fp:
                    attach = MIMEText(fp.read(), 'base64', 'utf-8')
                    attach["Content-Type"] = 'application/octet-stream'
                    attach.add_header('Content-Disposition', 'attachment',filename=('gbk', '',i))
                    msg.attach(attach)



        try:
            s = smtplib.SMTP_SSL(self.mailserver,self.port)
            s.login(msg_from,pwd)
            s.sendmail(msg_from,msg_to,msg.as_string())
            logging.info("邮件发送成功")
        except s.SMTPException as e:
            logging.error("邮件发送失败")
        finally:
            s.quit()




mail = MailCreator()

# 发送邮件信息
subject = "小黑的测试邮件"
content = "请查收20171010作业测试报告，谢谢！"
# msg_to = "215603651@qq.com"
msg_to = "204893985@qq.com"
file = ['测试.txt','HttpTestResult2017-10-12_22_55_24.html','tx.gif']

mail.send(msg_to,subject,content,file)
