from flask import Blueprint, render_template, request, redirect, url_for, flash

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
        # Extract form data
        name = request.form.get("name_surname")
        location = request.form.get("location")
        transportation = request.form.get("transportation")
        size = request.form.get("size")
        phone = request.form.get("phone")
        email = request.form.get("email")

        # Simple server-side validation
        if not all([name, location, transportation, size, phone, email]):
            flash("All fields are required. Please fill out the form completely.", "error")
            return redirect(url_for("main.purchase"))

        # Log the received data (replace with database saving logic)
        print(f"Order Received: {name}, {location}, {transportation}, {size}, {phone}, {email}")

        # Flash a success message
        flash("Your order has been submitted successfully!", "success")
        return redirect(url_for("main.purchase"))

    # Render the purchase form for GET requests
    return render_template("purchase.html")
