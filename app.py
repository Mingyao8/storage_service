from flask import Flask, render_template, request, redirect, url_for
import os

app = Flask(__name__)
UPLOAD_FOLDER = 'home/mingyao/flask_uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# 確保uploads資料夾存在
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        file = request.files['file']
        if file:
            filepath = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
            file.save(filepath)
            return redirect(url_for('file_list'))
    return render_template('upload.html')

@app.route('/files')
def file_list():
    # 讀取uploads資料夾中的所有檔案
    files = os.listdir(UPLOAD_FOLDER)
    return render_template('file_list.html', files=files)

@app.route('/files/<filename>')
def download_file(filename):
    return redirect(url_for('static', filename=os.path.join('uploads', filename)))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
