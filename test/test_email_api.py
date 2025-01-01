import pytest
from email_api.email_sender.email_sender import EmailSender

def test_email_sender():
    try:
        sender = EmailSender("smtp.gmail.com", 465, "test@gmail.com", "testpassword")
        sender.send_email(
            subject="Test Email",
            body="This is a test email.",
            to_emails=["recipient@example.com"]
        )
    except Exception:
        pytest.fail("EmailSender raised an exception unexpectedly.")
