import os
import requests
from dotenv import load_dotenv

load_dotenv()  # take environment variables from .env.

DOMAIN = os.getenv("MAILGUN_DOMAIN")

def send_simple_message():
    return requests.post(
        f"https://api.mailgun.net/v3/{DOMAIN}/messages",
        auth=("api", os.getenv('MAILGUN_API_KEY', 'MAILGUN_API_KEY')),
        data={"from": f"Mailgun Sandbox <postmaster@{DOMAIN}>",
                "to": "Shai Turjeman <shaiturjeman@icloud.com>",
                "subject": "Hello Shai Turjeman",
                "text": "Congratulations Shai Turjeman, you just sent an email with Mailgun! You are truly awesome!"})


def send_user_registration_email(email, username):
    return send_simple_message(
        email,
        "Welcome to our store!",
        f"Hi {username}, thank you for registering at our store."
    )