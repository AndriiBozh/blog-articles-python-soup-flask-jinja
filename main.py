from flask import Flask, render_template
import datetime
from bs4 import BeautifulSoup
import requests


app = Flask(__name__)


@app.route('/')
def main_page():
    url = 'https://techcrunch.com/'
    page = requests.get(url)
    soup = BeautifulSoup(page.text, 'html.parser')
    articles = soup.find_all('header', class_='post-block__header')
    curr_year = datetime.datetime.now().year
    return render_template('welcome.html', current_year=curr_year, articles=articles)


if __name__ == '__main__':
    app.run(debug=True)
