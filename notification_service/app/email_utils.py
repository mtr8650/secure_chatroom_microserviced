import smtplib
from email.mime.text import MIMEText
import os
from starlette.concurrency import run_in_threadpool

async def send_email_notification(to_email: str, subject: str, body: str):
    from_email = os.getenv("SMTP_EMAIL")
    password = os.getenv("SMTP_PASSWORD")

    if not from_email or not password:
        raise ValueError("SMTP credentials are not set in environment variables.")

    msg = MIMEText(body)
    msg["Subject"] = subject
    msg["From"] = from_email
    msg["To"] = to_email

    def send():
        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
            smtp.login(from_email, password)
            smtp.send_message(msg)

    await run_in_threadpool(send)
