import os
from flask import app, request


basedir = os.path.abspath(os.path.dirname(__file__))


@app.route('/post_test', methods=['GET', 'POST'])
def post_test():
    img = request.files.get('upload')
    path = basedir + "/static/img/"
    img_name = img.filename
    file_path = path + img_name
    img.save(file_path)
    url = '/static/img/' + img_name
    # use neural network get string
    # return
    return url


if __name__ == '__main__':
    app.run()
