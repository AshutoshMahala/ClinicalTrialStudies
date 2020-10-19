from flask import Flask, jsonify, request
from RSSCrawler import RSSCrawler

CLINICAL_GOV_URL = "https://clinicaltrials.gov/ct2/results/rss.xml"

app = Flask(__name__)
crawler = RSSCrawler(CLINICAL_GOV_URL)


@app.route('/')
def home():
    return jsonify(message="Welcome to Was It Active use the example to make a request",
                   example="/wasitactive?name=Alzheimer%20Disease&daysinactive=15")


@app.route('/wasitactive')
def was_it_active():
    if len(request.args) == 0:
        return jsonify(message="Welcome to Was It Active use the example to make a request",
                       example="/wasitactive?name=Alzheimer%20Disease&daysinactive=15")
    name = request.args.get('name')
    print(name)
    days_str = request.args.get('daysinactive')
    print(days_str)
    if not days_str:
        return jsonify(message="Invalid number of days, please provide days with number of days greater than 0"), 400
    days = int(days_str)
    if days <= 0:
        return jsonify(message="Invalid number of days, number of days greater than 0"), 422
    active = crawler.was_active_in_days(name, days)
    return jsonify(message=f"Status for {name}", activity=active), 200


if __name__ == '__main__':
    app.run()
