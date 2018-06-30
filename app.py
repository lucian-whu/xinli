# coding:utf-8

from flask import Flask,render_template,request,redirect,url_for
from werkzeug.utils import secure_filename
import os

app = Flask(__name__)

resume_pdf_link = 'http://127.0.0.1:5000/static/uploads/cvxinli.pdf'

@app.route('/')
def index():
    return render_template('home.html')

@app.route('/timeline')
def aboutme():
	return render_template('timeline.html', resume_pdf_link=resume_pdf_link)

@app.route('/publications')
def articles():
    return render_template('pub.html', resume_pdf_link=resume_pdf_link)

@app.route('/upload', methods=['POST', 'GET'])
def upload():
    if request.method == 'POST':
        f = request.files['file']
        basepath = os.path.dirname(__file__)  # 当前文件所在路径
        upload_path = os.path.join(basepath, 'static\uploads',secure_filename(f.filename))  #注意：没有的文件夹一定要先创建，不然会提示没有该路径
        f.save(upload_path)
        return redirect(url_for('upload'))
    return render_template('upload.html')

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404




if __name__ == "__main__":
    print("running py app")
    app.run(host="127.0.0.1", port=5000, debug=True)
