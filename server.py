import os
import feedparser
from flask import Flask, request, render_template, g, redirect, Response

tmpl_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'templates')
app = Flask(__name__, template_folder=tmpl_dir)

subscriptions = {
    "9GAG_Awesome" : "https://9gag-rss.com/api/rss/get?code=9GAGAwesome&format=2",
    "9GAG_Comic" : "https://9gag-rss.com/api/rss/get?code=9GAGComic&format=2",
    "9GAG_Funny" : "https://9gag-rss.com/api/rss/get?code=9GAGFunny&format=2",
    "9GAG_Hot" : "https://9gag-rss.com/api/rss/get?code=9GAGHot&format=2"


}

feed_data = {}
feed_last_update = {}

@app.before_request
def before_request():
    """
    This function is run at the beginning of every web request
    (every time you enter an address in the web browser).
    The variable g is globally accessible.
    """



@app.teardown_request
def teardown_request(exception):
    """
    At the end of the web request
    """



#
# @app.route is a decorator around index() that means:
#   run index() whenever the user tries to access the "/" path using a GET request
#
# If you wanted the user to go to, for example, localhost:8111/foobar/ with POST or GET then you could use:
#
#       @app.route("/foobar/", methods=["POST", "GET"])
#
# PROTIP: (the trailing / in the path is important)
# 
# see for routing: http://flask.pocoo.org/docs/0.10/quickstart/#routing
# see for decorators: http://simeonfranklin.com/blog/2012/jul/1/python-decorators-in-12-steps/
#
@app.route('/')
def index():
    """
    request is a special object that Flask provides to access web request information:

    request.method:   "GET" or "POST"
    request.form:     if the browser submitted a form, this contains the data in the form
    request.args:     dictionary of URL arguments, e.g., {a:1, b:2} for http://localhost?a=1&b=2

    See its API: http://flask.pocoo.org/docs/0.10/api/#incoming-request-data
    """

    return render_template("index.html")

#
# This is an example of a different path.  You can see it at:
# 
#     localhost:8111/another
#
# Notice that the function name is another() rather than index()
# The functions for each app.route need to have different names
#
@app.route('/awesome')
def awesome():
    feeds = feedparser.parse(subscriptions["9GAG_Awesome"])
    # print(feeds)
    # print(len(feeds['entries']))

    posts = []
    for post in feeds.entries:
        article = {}
        article["id"] = post.id
        article["title"] = post.title
        article["link"] = post.link
        article["summary"] = post.summary
        posts.append(article)

    context = dict(data=posts)

    return render_template("awesome.html", **context)

@app.route('/comic')
def comic():
    feeds = feedparser.parse(subscriptions["9GAG_Comic"])
    # print(feeds)
    # print(len(feeds['entries']))

    posts = []
    for post in feeds.entries:
        article = {}
        article["id"] = post.id
        article["title"] = post.title
        article["link"] = post.link
        article["summary"] = post.summary
        posts.append(article)

    context = dict(data=posts)

    return render_template("comic.html", **context)

@app.route('/funny')
def funny():
    feeds = feedparser.parse(subscriptions["9GAG_Funny"])
    # print(feeds)
    # print(len(feeds['entries']))

    posts = []
    for post in feeds.entries:
        article = {}
        article["id"] = post.id
        article["title"] = post.title
        article["link"] = post.link
        article["summary"] = post.summary
        posts.append(article)

    context = dict(data=posts)

    return render_template("funny.html", **context)

@app.route('/hot')
def hot():
    feeds = feedparser.parse(subscriptions["9GAG_Hot"])
    # print(feeds)
    # print(len(feeds['entries']))

    posts = []
    for post in feeds.entries:
        article = {}
        article["id"] = post.id
        article["title"] = post.title
        article["link"] = post.link
        article["summary"] = post.summary
        posts.append(article)

    context = dict(data=posts)

    return render_template("hot.html", **context)


if __name__ == "__main__":
    import click

    @click.command()
    @click.option('--debug', is_flag=True)
    @click.option('--threaded', is_flag=True)
    @click.argument('HOST', default='0.0.0.0')
    @click.argument('PORT', default=8111, type=int)
    def run(debug, threaded, host, port):
        """
        This function handles command line parameters.
        Run the server using:

            python server.py

        Show the help text using:

            python server.py --help

        """

        HOST, PORT = host, port
        app.run(host=HOST, port=PORT, debug=debug, threaded=threaded)


    run()
