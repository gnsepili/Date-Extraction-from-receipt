from flask import Flask, render_template, request
from app import dateExtractor
from werkzeug.utils import secure_filename
import os

app = Flask(__name__)

	
@app.route('/extract_date', methods = ['POST'])
def upload_file():
   if request.method == 'POST':
      file = request.files['base_64_image_content']
      filename = secure_filename(file.filename) # save file 
      filepath = os.path.join('./data', filename)
      file.save(filepath)
      date=dateExtractor(filepath)
      return date
	
if __name__ == '__main__':
   app.run(debug = True)
