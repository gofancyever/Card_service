from flask import Flask
from flask import make_response,send_file
import os
from urllib.parse import quote
app = Flask(__name__)

FILE_PATH = os.getcwd()

@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/library',methods=['GET','POST'])
def file_download():
    filename = FILE_PATH + '/' + 'test.db'
    response = make_response(send_file(filename))
    basename = os.path.basename(filename)
    response.headers["Content-Disposition"] = \
        "attachment;" \
        "filename*=UTF-8''{utf_filename}".format(
            utf_filename=quote(basename.encode('utf-8'))
        )
    return response
if __name__ == '__main__':
    app.run()
