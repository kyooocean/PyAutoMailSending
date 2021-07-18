import datetime
import smtplib
import ssl
from email.mime.text import MIMEText

import sys,io
sys.stdout = io.TextIOWrapper(sys.stdout,encoding='utf-8')

#mail sending

gmail_account = "kyoceantech@gmail.com"
gmail_password = "kyokyo817#"
mail_to = "kyoceantech@gmail.com"
send_name = "キョロちゃん"

today_date = datetime.date.today()
delivery_date = today_date + datetime.timedelta(days=7)
print(today_date,delivery_date)

# MIME
subject = "{0}様、{1}に受験された試験の結果をお送りします。".format(send_name,today_date)
body = "試験結果をお送りします。<br>添付ファイルをご確認ください。<br>なお、本試験の合格者の入学手続きは{0}までとなります。<br><br>学校法人モリモリ学園".format(delivery_date)

msg = MIMEText(body, "html")
print(msg)

