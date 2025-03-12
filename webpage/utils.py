import nltk
from textblob import TextBlob
from newspaper import Article

def summarize(url):
    nltk.download("punkt")

    article = Article(url)
    article.download()
    article.parse()
    article.nlp()

    title = article.title
    author = ', '.join(article.authors)
    date = article.publish_date
    summary = article.summary

    analysis = TextBlob(article.text)
    polarity = analysis.polarity
    polarity_analysis = "Positive" if analysis.polarity > 0 else "Negative"

    return title, author, date, summary, polarity, polarity_analysis