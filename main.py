from flask import Flask, render_template
import requests

app = Flask(__name__)

endpoint = 'https://api.npoint.io/674f5423f73deab1e9a7'

response = requests.get(endpoint)
data = response.json()


@app.route('/')
def home():    
    return render_template("index.html", data = data)

@app.route('/about/')
def about():
    return render_template('about.html')

@app.route('/contact/')
def contact():
    return render_template('contact.html')

@app.route('/post/<int:number>/')
def post(number):
    return render_template('post.html', data=data, number = number)

if __name__ == "__main__":
    app.run(debug=True)