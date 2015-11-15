# second try of restful api

from flask import Flask, url_for, json, request
import safeMap as sm

app = Flask(__name__)

@app.route('/addresses', methods = ['GET', 'POST'])
def api_address():
	if request.method == 'POST':
		print "HELLO"
		# print request.mimetype

		json_var = json.dumps(request.json)
        data = json.loads(json_var)
        print data['Origin'], data['Destination']

        return sm.return_Best_Route(data['Origin'], data['Destination'])
        # return "lols\n"
        # return ret_json
		# else:
		# 	return "Unsupported Media Type!"

if __name__ == '__main__':
	app.run(debug=True)