from flask_mail import Message
from app import mail

def send_order_email(customer_email, customer_name, order_details):
    try:
        msg = Message(
            subject="New Order Received",
            recipients=["your-email@gmail.com"],  # Your email
        )
        msg.body = f"Order from {customer_name} ({customer_email}):\n\n{order_details}"
        mail.send(msg)
    except Exception as e:
        print(f"Error sending email: {e}")
