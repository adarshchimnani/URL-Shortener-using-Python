#1. URL-Shortener using *pyshortners* library.

# from flask import Flask, render_template, request
# import pyshorteners
# app = Flask(__name__)

# @app.route("/", methods=['POST', 'GET'])
# def home():
#     if request.method=="POST":
#         url_received = request.form["url"]
#         short_url = pyshorteners.Shortener().tinyurl.short(url_received)  #Using *tiny-url* module
#         # short_url = pyshorteners.Shortener().osdb.short(url_received)   #Using *osdb* module
#         return render_template("form.html", new_url=short_url, old_url=url_received)
#     else:
#         return render_template('form.html')

# if __name__ == "__main__":
#   app.run()


#2. URL-Shortener using *Bitly API* module.

from flask import Flask, render_template, request
import bitly_api
app = Flask(__name__)

bitly_access_token = "YOUR ACCESS TOKEN"

@app.route("/", methods=['POST', 'GET'])
def home():
    if request.method=="POST":
        url_received = request.form["url"]
        bitly = bitly_api.Connection(access_token=bitly_access_token)
        short_url = bitly.shorten(url_received)
        return render_template("form.html", new_url=short_url.get('url'), old_url=url_received)
    else:
        return render_template('form.html')

if __name__ == "__main__":
  app.run()