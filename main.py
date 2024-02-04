from flask import Flask, render_template, jsonify, request
from werkzeug.utils import secure_filename
import os



# the line below initializes the Flask app
app = Flask(__name__)

# the line below specifies that the tmp folder should be used for file uploads
app.config['UPLOAD_FOLDER'] = 'tmp'




@app.route('/', methods=['GET', 'POST'])
def index():
	"""

	This function will execute every time someone enters the landing page of your application.
	Right now it simply creates some text and inserts it into the page under the name 'info' 
	upon rendering the index.html page.

	"""
	data = 'Hello, this is data that has been inserted from the Flask backend!!!!'
	return render_template("index.html",info = data)





@app.route('/render_form', methods=['GET', 'POST'])
def render_form():
	"""

	This function is responsible for rendering the form.html page and will be triggered
	if the user visits the /render_form url of the application.

	"""
	return render_template("form.html")





@app.route('/submit_form', methods=['POST'])
def submit_form():
	"""

	This function is triggered by a function in form.js, which is
	executed by clicking a button in a form in form.html.  It pulls the data that you 
	entered into the form HTML element in form.html using request.get_json(). This data will be 
	in the form of a python dictionary.  It then appends " was received" to the message
	that was submitted and sends it back as a JSON response.  The form.html page is 
	set up to then display this response on screen.

	"""
	data = request.get_json()
	print("I just recieved " + str(data))
	message = data["message"]
	send_back = {}
	send_back["response"] = message + " was recieved"
	return jsonify(send_back), 200






@app.route('/upload_file', methods=['POST'])
def upload_file():
	"""

	This function is triggered by a function in form.js, which is
	executed by clicking a button in a form HTML element in form.html.  It pulls the file that you
	chose to upload and writes it to the tmp folder in the project and then returns
	as JSON message indicating whether or not is as successfully able to upload the file

	"""
    if 'file' not in request.files:
        return jsonify({"message":"Error no file found"}), 500
    file = request.files['file']
    if file.filename == '':
        return jsonify({"message":"Something went wrong"}), 500
    if file:
        filename = secure_filename(file.filename)
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        return jsonify({"message":"file successfully uploaded"}), 200





if __name__ == '__main__':
	"""

	This executes the Flask app with debug turned on, which means you can alter the code as 
	the app is running and it will restart and upate automatically.  The host is set to 0.0.0.0,
	which implies that you are running it locally.

	""" 
	app.run(debug=True,  host='0.0.0.0', port = 5002)







