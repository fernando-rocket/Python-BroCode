import smtplib

sender = ""
receiver = ""
password = ""
subject = "Python email test"
body = "I wrote an email! :D"

# header
message = f"""From: {sender}
To: {receiver}
Subject: {subject}\n
{body}
"""

try:
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(sender, password)
    print("Logged in")
    server.sendmail(sender, receiver, message)
    print("Email has been sent")
except:
    print("Unable to sign in")

# Para funcionar tem que desativar uma função de segurança da sua conta google.
