from flask import Flask,render_template
import json
import requests

app=Flask(__name__)

@app.route('/')
def home():
    url=f'https://newsapi.org/v2/top-headlines?country=in&apikey=e9647a3d2760405c94495a5493f0c2d1'
    response = requests.get(url)
    return render_template("home.html",context=json.loads(response.text)['articles'])

if __name__== '__main__':
  app.debug = True
  app.run()