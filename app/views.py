from app import app # import "app" folder import "app.py" file
from flask import render_template, request, redirect
from fastai.vision.all import *
import pathlib # To sort out PosixPath issue occuring on Windows


# Explore this thing
# https://blog.miguelgrinberg.com/post/handling-file-uploads-with-flask

app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0

@app.route("/")
def index():
    print("kupa")

    # print(app.config)
    return render_template("public/index.html")

# load_posix_learner is a workaround for error occuring on Windows:
# "NotImplementedError: cannot instantiate 'PosixPath' on your system"
# The reason for this error is, that on Windows, PosixPath is not implemented. 
def load_posix_learner(path):
    save = pathlib.PosixPath
    pathlib.PosixPath = pathlib.WindowsPath
    learn = load_learner(path)
    pathlib.PosixPath = save
    return learn



@app.route("/upload_image", methods=['POST'])
def upload_image():
    # Check if POST method is used
    if request.method == "POST":

        # Intercept file object from the form
        from_upload = request.files['image']

        # Load learned clasifier 
        learn = load_posix_learner('app/static/models/export_resnet14.pkl')

        # Load sample used to make perdiction
        ret = learn.predict(from_upload.read())

        # print(ret)
        d = {'pred-class-name': ret[0],
        'pred-class-index': ret[1].tolist(),
        'output-layer-activations': ret[2].tolist(),
        'class-titles': list(learn.dls.vocab),
        #  'time-saved': time.time(),
        }

        print("Predicted tree: ", d['pred-class-name'])

        # return '''<h1>POST METHOD was passed: {}</h1>'''.format(from_upload.filename)
        return json.dumps(d)
    else:
        return "<h1>IT WAS NOT A POST METHOD<h1>"




