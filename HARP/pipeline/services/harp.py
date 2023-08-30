
from flask import Flask, render_template, request
from werkzeug.utils import secure_filename
from Pipeline.Utils import DButils, GeneralUtils

harp = Flask(__name__)

harp.config["UPLOAD_FOLDER"] = "static/"

@harp.route('/')
def upload_file():
    return render_template('index.html')



@harp.route('/display', methods = ['GET', 'POST'])
def save_file():
    if request.method == 'POST':
        f = request.files['file']
        filename = secure_filename(f.filename)

        f.save(harp.config['UPLOAD_FOLDER'] + filename)

        
    return "successfully uploaded the file"

@harp.route('/posted', methods = ['POST'])
def save_file_API():
    if request.method == 'POST':
        f = request.files['file']
        filename = secure_filename(f.filename)

        f.save(harp.config['UPLOAD_FOLDER'] + filename)
 
        
    return "successfully uploaded the file"


@harp.route('/postgenerate', methods = ['POST'])
def save_file():
    if request.method == 'POST':
        f = request.files['file']
        filename = secure_filename(f.filename)

        f.save(harp.config['UPLOAD_FOLDER'] + filename)
    return "successfully uploaded the file"



@harp.route('/createDB', methods = ['GET', 'POST'])
def save_file():
    print("Testing creating HARP DB structre")
    status = DButils.setup_HARP_DB()
    if status:
        ret_string =  "successfully uploaded the file"
    else:
        ret_string =  "Failed to create DB."+status





if __name__ == '__main__':
    harp.run(host="0.0.0.0", port=5001, debug = True)

