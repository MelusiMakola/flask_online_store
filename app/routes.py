from flask import Blueprint, render_template, request, redirect, url_for, flash
from app import db
from app.models import Order
from app.utils import send_order_email

main = Blueprint('main', __name__)

# Home Page
@main.route("/")
def home():
    return render_template("index.html")

# About Page
@main.route("/about")
def about():
    return render_template("about.html")


@main.route("/gallery")
def gallery():
    return render_template("gallery.html")  # Ensure this template exists


# Contact Page
@main.route("/contact")
def contact():
    return render_template("contact.html")

# Purchase Page with Order Form Handling
@main.route("/purchase", methods=["GET", "POST"])
def purchase():
    if request.method == "POST":
        # Get form data
        name = request.form.get("name_surname")
        location = request.form.get("location")
        transportation = request.form.get("transportation")
        size = request.form.get("size")
        phone = request.form.get("phone")
        email = request.form.get("email")

        # Simulate saving order to database
        order_details = f"Location: {location}, Transportation: {transportation}, Size: {size}, Phone: {phone}"
        new_order = Order(user_id=1, product_id=1, quantity=1, total_price=99.99)
        db.session.add(new_order)
        db.session.commit()

        # Send email notification
        send_order_email(email, name, order_details)

        # Flash success message
        flash("Your order has been placed successfully!", "success")
        return redirect(url_for("main.purchase"))

    return render_template("purchase.html")