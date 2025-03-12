from flask import Flask, request, render_template
from utils import summarize

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/summarize', methods=['POST'])
def summarize_article():
    url = request.form['url']
    title, author, date, summary, polarity, polarity_analysis = summarize(url)
    return render_template('result.html', title=title, author=author, date=date, summary=summary, polarity=polarity, polarity_analysis=polarity_analysis)

if __name__ == '__main__':
    app.run(debug=True)