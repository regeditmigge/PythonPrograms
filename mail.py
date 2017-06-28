from email import encoders
from email.header import Header
from email.mime.text import MIMEText
from email.utils import parseaddr, formataddr
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase

import smtplib


def _format_addr(s):
    name, addr = parseaddr(s)
    return formataddr((Header(name, 'utf-8').encode(), addr))

from_addr = '发件箱地址'
password = '发件箱密码'
to_addr = '收件人邮箱'
smtp_server = 'SMTP服务器地址'

msg = MIMEMultipart()
msg['From'] = _format_addr('Python_User <%s>' % from_addr)
msg['To'] = _format_addr(to_addr)
msg['Subject'] = Header('From Python SMTP...', 'utf-8').encode()

msg.attach(MIMEText('<html><body><h1>Hello</h1>' +
                    '<p><img src="cid:0"></p>' +
                    '</body></html>', 'html', 'utf-8'))

with open('D:\\RazerChroma_1920x1080.png', 'rb') as f:
    # 设置附件的MIME和文件名，这里是png类型:
    mime = MIMEBase('image', 'png', filename='RazerChroma_1920x1080.png')
    # 加上必要的头信息:
    mime.add_header('Content-Disposition', 'attachment',
                    filename='RazerChroma_1920x1080.png')
    mime.add_header('Content-ID', '<0>')
    mime.add_header('X-Attachment-Id', '0')
    # 把附件的内容读进来:
    mime.set_payload(f.read())
    # 用Base64编码:
    encoders.encode_base64(mime)
    # 添加到MIMEMultipart:
    msg.attach(mime)

server = smtplib.SMTP(smtp_server, 25)
server.set_debuglevel(1)
server.login(from_addr, password)
server.sendmail(from_addr, [to_addr], msg.as_string())
server.quit()
