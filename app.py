from flask import Flask, request, render_template, jsonify
import requests
import re

app = Flask(__name__)

def extract(url):
	r = requests.get(url)
	urls = re.findall('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+',str(r.content))
	return urls

@app.route('/')
def form():
	return render_template('index.html')

@app.route('/form-handler', methods=['POST'])
def get_form_data():
	url = request.form['text']
	urls = extract(url)

	print(urls)
	
	return render_template('result.html',url_to_extract=url, items=urls)

if __name__ == '__main__':
	app.run(debug=True)