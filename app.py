from flask import Flask, render_template, request
from flask_uploads import UploadSet, configure_uploads, IMAGES, ALL
from pyexcel_xlsx import get_data
import json

app=Flask(__name__)
photos = UploadSet('photos', ALL)

app.config['UPLOADED_PHOTOS_DEST'] = 'static/img'
configure_uploads(app, photos)

@app.route("/")
def index():
    return render_template("index.html")

@app.route('/upload', methods=['GET', 'POST'])
def upload():
    if request.method == 'POST' and 'photo' in request.files:
        filename = photos.save(request.files['photo'])
        return anaylze(filename)
    return render_template('upload.html')

def anaylze(filename):
    filePosition= "static/img/"+filename
    # files= open(filePosition, "r")
    # wb = load_workbook(filename=filePosition, read_only=True)
    # ws = wb['Summary']
    #
    # for row in ws.rows:
    #     print(row)
    # return("opened file")

    data = get_data(filePosition)
    s1=json.dumps(data)
    d2=json.loads(s1)
    d2= d2["Summary"]
    s2=json.dumps(d2)
    return s2 
    # return(jsonDict)

    # return jsonDict['Summary']


if __name__=="__main__":
    app.run(debug=True)
