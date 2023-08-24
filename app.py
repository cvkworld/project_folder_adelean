import requests
from flask import Flask, render_template, request

app = Flask(__name__)

# Configuration of API URL and Token URL
API_URL = "https://api.beta.all.site/api/v1/search/search"
TOKEN_URL = "https://api.beta.all.site/api/v1/user/guest/login"
USERNAME = "candidate@adelean.com"
PASSWORD = "candidateforadelean"

def get_token():
    response = requests.post(TOKEN_URL, json={"username": USERNAME, "password": PASSWORD})
    token = response.json().get("token")
    return token

@app.route("/", methods=["GET", "POST"])
def search_page():
    if request.method == "POST":
        search_text = request.form.get("search_text")
        token = get_token()
        
        if token:
            headers = {"Authorization": f"Bearer {token}"}
            payload = {
                "text": search_text,
                "searchEngineId": "5fd744113dd37c717e16356a"
            }
            response = requests.post(API_URL, json=payload, headers=headers)
            search_results = response.json()
            return render_template("results.html", results=search_results)
    
    return render_template("search.html")

if __name__ == "__main__":
    app.run(debug=True)
