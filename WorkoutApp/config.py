import os

class Config:
    # Generated using secrets.token_hex(16)
    SECRET_KEY = os.environ.get('7673ae427b92edacdcf02dacd0b5dc1f')
    SQLALCHEMY_DATABASE_URI = os.environ.get('sqlite:///site.db')
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get('EMAIL_USER')
    MAIL_PASSWORD = os.environ.get('EMAIL_PASS')