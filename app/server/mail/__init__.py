import os
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail
from flask import current_app, flash, redirect, url_for
from functools import wraps
from flask_login import current_user

def send_mail(to, subject, message):

    message = Mail(
         from_email='ssm29@njit.edu',
         to_emails=to,
         subject=subject,
         html_content=message)

    try:
        #API key loaded from .env file and can be found in comments
        api_key = os.environ.get('SENDGRID_API_KEY')
        sg = SendGridAPIClient(api_key)
        response = sg.send(message)
        print(response.status_code)
        print(response.body)
        print(response.headers)

    except Exception as e:
        print(e.message)


def check_confirmed(func):
    @wraps(func)
    def decorated_function(*args, **kwargs):
        if current_user.confirmed is False:
            flash('Please confirm your account!', 'warning')
            return redirect(url_for('index_bp.unconfirmed'))
        return func(*args, **kwargs)

    return decorated_function
