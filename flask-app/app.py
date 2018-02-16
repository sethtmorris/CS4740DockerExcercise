from flask import Flask, render_template, request
from werkzeug import secure_filename
import compile

app = Flask(__name__)

@app.route('/upload')
def upload_file2():
	return render_template('upload.html')

@app.route('/uploader', methods = ['GET', 'POST'])
def upload_file():
	if request.method == 'POST':
		f = request.files['file']
		f.save(secure_filename(f.filename))
		compile.compile()
		test.test()

'''
if __name__ == "__main__":
    app.run(debug = True)
'''
