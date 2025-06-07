from flask import Flask, render_template, request
import requests

app = Flask(__name__)

# Mapping layanan ke endpoint GraphQL
GRAPHQL_ENDPOINTS = {
    "user": "http://localhost:5001/graphql",
    "inventory": "http://localhost:5002/graphql",
    "category": "http://localhost:5003/graphql",
    "supplier": "http://localhost:5004/graphql",
    "notification": "http://localhost:5005/graphql",
}

@app.route("/", methods=["GET", "POST"])
def index():
    result = None
    if request.method == "POST":
        service = request.form["service"]
        query = request.form["query"]
        endpoint = GRAPHQL_ENDPOINTS.get(service)
        if endpoint:
            response = requests.post(endpoint, json={"query": query})
            result = response.json()
    return render_template("index.html", result=result)

if __name__ == "__main__":
    app.run(debug=True, port=8000)
