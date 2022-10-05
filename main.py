from flask import Flask, render_template, request
import requests
import datetime as dt
import os
import smtplib

my_email = os.environ["my_email"]
password = os.environ["password"]
sent_email = os.environ["s_email"]

app = Flask("__main__")


@app.route('/')
def main():
    blog_url = "https://api.npoint.io/f9937b2bc2004f995507"
    response = requests.get(blog_url)
    all_posts = response.json()
    return render_template("index.html", posts=all_posts)


@app.route('/post/<int:num>')
def get_post(num):
    blog_url = "https://api.npoint.io/f9937b2bc2004f995507"
    response = requests.get(blog_url)
    all_posts = response.json()
    return render_template("post.html", posts=all_posts, num=num)


@app.route('/about')
def get_about():
    year = dt.datetime.today().year
    return render_template("about.html", year=year)


@app.route('/contact', methods=["GET", "POST"])
def get_contact():
    if request.method == "POST":
        name = request.form["name"]
        email = request.form["email"]
        phone = request.form["phone"]
        message = request.form["message"]
        print(f"{name}\n{email}\n{phone}\n{message}")
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(my_email, password)
            connection.sendmail(from_addr=my_email,
                                to_addrs=sent_email,
                                msg=f"Subject:Blog Contact!\n\nName={name}\nEmail={email}\nPhone={phone}\nMessage={message}")
        return render_template("contact.html", message="Successfully sent your message")
    return render_template("contact.html", message="Contact Me")


if __name__ == "__main__":
    app.run(debug=True)
