from flask import Flask, render_template, request
from transformers import pipeline

app = Flask(__name__)
summarizer = pipeline("summarization")

@app.route('/', methods=['GET', 'POST'])
def index():
    summary = ''
    if request.method == 'POST':
        text = request.form['text']
        if text.strip():
            summary = summarizer(text, max_length=150, min_length=40, do_sample=False)[0]['summary_text']
    return render_template('index.html', summary=summary)

if __name__ == '__main__':
    app.run()