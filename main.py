from flask import Flask, render_template
import requests
import datetime as dt


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


@app.route('/contact')
def get_contact():
    return render_template("contact.html")


if __name__ == "__main__":
    app.run(debug=True)
