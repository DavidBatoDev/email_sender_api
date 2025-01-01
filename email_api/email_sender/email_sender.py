import smtplib
from email.message import EmailMessage

class EmailSender:
    def __init__(self, smtp_server: str, port: int, username: str, password: str):
        self.smtp_server = smtp_server
        self.port = port
        self.username = username
        self.password = password

    def send_email(self, subject: str, body: str, to_emails: list):
        try:
            msg = EmailMessage()
            msg["Subject"] = subject
            msg["From"] = self.username
            msg["To"] = ", ".join(to_emails)
            msg.set_content(body)

            with smtplib.SMTP_SSL(self.smtp_server, self.port) as server:
                server.login(self.username, self.password)
                server.send_message(msg)
                print("Email sent successfully.")
        except Exception as e:
            raise RuntimeError(f"Failed to send email: {e}")
