from flask import Flask, request, render_template
import logging

app = Flask(__name__)
log = logging.getLogger('werkzeug')
log.setLevel(logging.ERROR)


@app.route("/")
def main():
	name = request.args.get('name') or "..."
	message = request.args.get('message') or "..."
	print(f"{name}! {message}")
	return render_template('index.html', name=name, message=message)


if __name__ == '__main__':
	app.run(debug=False, host='0.0.0.0')
