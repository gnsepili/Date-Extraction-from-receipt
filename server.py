from flask import Flask, render_template, request
from app import dateExtractor
app = Flask(__name__)

# @app.route('/upload')
# def upload_file():
#    return render_template('upload.html')
	
@app.route('/extract_date', methods = ['POST'])
def upload_file():
   if request.method == 'POST':
      file = request.files['base_64_image_content']
      date=dateExtractor(file)
      return date
	
if __name__ == '__main__':
   app.run(debug = True)