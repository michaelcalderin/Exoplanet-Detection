from flask import Flask, render_template, request
import requests

# Initialize app
app = Flask(__name__)

# Fetch response from chatbot which is hosted on Google Cloud as a function
def fetch_response(user_msg):

    # Google Cloud URL
    url = 'https://python-http-function-326290605488.us-east1.run.app'

    # Fetch information from Google Cloud (will call Open AI API)
    data = {'message': user_msg}
    bot_response = requests.post(url, json=data).text
    return bot_response

# Page with chat boxes
@app.route("/", methods=['GET', 'POST'])
def index():
    # Handle user's message in the text box
    if request.method == 'POST':
        user_msg = request.form['message']
        bot_response = fetch_response(user_msg)
        return render_template("index.html", user_msg=user_msg, bot_response=bot_response)

    return render_template("index.html", user_msg=None, bot_response=None)

# Run app
if __name__ == "__main__":
    app.run(debug=True)