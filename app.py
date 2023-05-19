import re
from datetime import datetime
import os
from flask import Flask, render_template, flash, request, redirect, url_for, send_from_directory
from werkzeug.utils import secure_filename


UPLOAD_FOLDER = '/Users/raginimenon/Desktop/alm'
ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif', 'xml'}

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route("/")
def home():
    return "Hello, Flask!"

@app.route("/hello")
@app.route("/hello/<name>")
def hello_there(name=None):
    return render_template(
        "hello_there.html",
        name=name,
        date=datetime.now()
    )

# @app.route("/api/data")
# def get_data():
#     return app.send_static_file("data.josn")


# def allowed_file(filename):
#     return '.' in filename and \
#            filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

# #@app.route('/', methods=['GET', 'POST'])
# # def upload_file():
# #     if request.method == 'POST':
# #         # check if the post request has the file part
# #         if 'file' not in request.files:
# #             flash('No file part')
# #             return redirect(request.url)
# #         file = request.files['file']
# #         # If the user does not select a file, the browser submits an
# #         # empty file without a filename.
# #         if file.filename == '':
# #             flash('No selected file')
# #             return redirect(request.url)
# #         if file and allowed_file(file.filename):
# #             filename = secure_filename(file.filename)
# #             file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
# #             return redirect(url_for('download_file', name=filename))
# #     return '''
# #     <!doctype html>
# #     <title>Upload new File</title>
# #     <h1>Upload new File</h1>
# #     <form method=post enctype=multipart/form-data>
# #       <input type=file name=file>
# #       <input type=submit value=Upload>
# #     </form>
# #     '''

# # @app.route('/uploads/<name>')
# # def download_file(name):
# #     return send_from_directory(app.config["UPLOAD_FOLDER"], name)

# # app.add_url_rule(
# #     "/uploads/<name>", endpoint="download_file", build_only=True
# # )

# def make_tree(path):
#     tree = dict(name=os.path.basename(path), children=[])
#     try: lst = os.listdir(path)
#     except OSError:
#         pass #ignore errors
#     else:
#         for name in lst:
#             fn = os.path.join(path, name)
#             if os.path.isdir(fn):
#                 tree['children'].append(make_tree(fn))
#             else:
#                 tree['children'].append(dict(name=name))
#     return tree

# @app.route('/')
# def dirtree():
#     path = os.path.expanduser(u'~')
#     return render_template('dirtree.html', tree=make_tree(path))

# if __name__=="__main__":
#     app.run(host='localhost', port=8888, debug=True)