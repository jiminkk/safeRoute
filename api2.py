# second try of restful api

from flask import Flask, url_for, json, request

app = Flask(__name__)

@app.route('/addresses', methods = ['GET', 'POST'])
def api_address():
	if request.method == 'POST':
		print "HELLO"
		# print request.mimetype
		# print request.get_json()
		# if request.headers['Content-Type'] == 'application/json':
		return "JSON address: "  + json.dumps(request.json) + '\n'
		# else:
		# 	return "Unsupported Media Type!"

if __name__ == '__main__':
	app.run(debug=True)