import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header
from email.mime.image import MIMEImage
from email import encoders
from public.log import Log
from public.config import Config

class Mail:
    def __init__(self):
        c = Config()
        self.mailserver = c.getConfig("mail", "mailserver")         # 邮箱服务器
        self.port = c.getConfig("mail", "port")                      # 邮箱服务器端口
        self.mail_user = c.getConfig("mail", "mail_user")            # 发件人邮箱
        self.mail_pwd = c.getConfig("mail", "mail_pwd")              # 发件人邮箱授权码


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
            Log('sendmail').info("邮件发送成功")
        except Exception as e:
            Log('sendmail').error("邮件发送失败")
        finally:
            s.quit()





