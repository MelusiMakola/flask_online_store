from flask import Flask
from flask_mail import Mail, Message

app = Flask(__name__)

# Email Configuration
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = 'melusimakola@gmail.com'
app.config['MAIL_PASSWORD'] = 'hhkh sjzb nvnd zvxn'
app.config['MAIL_DEFAULT_SENDER'] = 'melusimakola@gmail.com'


mail = Mail(app)

with app.app_context():
    try:
        msg = Message(
            subject="Test Email",
            recipients=["melusimakola@gmail.com"],  # Replace with your email
            body="This is a test email sent from Flask-Mail."
        )
        mail.send(msg)
        print("Email sent successfully!")
    except Exception as e:
        print(f"Error sending email: {e}")
