import os
from flask import Flask, request, render_template, send_from_directory
import shutil

app = Flask(__name__)

UPLOAD_FOLDER = '/home/mingyao/flask_uploads'  # 檔案存放的資料夾
ALLOWED_EXTENSIONS = {'pdf', 'doc', 'docx', 'txt', 'jpg', 'png'}

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# 檢查副檔名是否允許
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

# 上傳檔案
@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        file = request.files['file']
        if file and allowed_file(file.filename):
            filename = file.filename
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            return '檔案上傳成功'
    return '''
    <!doctype html>
    <title>上傳檔案</title>
    <h1>上傳檔案</h1>
    <form method="POST" enctype="multipart/form-data">
      <input type="file" name="file">
      <input type="submit" value="上傳">
    </form>
    '''

# 顯示目前所有檔案
@app.route('/files', methods=['GET'])
def list_files():
    files = os.listdir(app.config['UPLOAD_FOLDER'])
    return render_template('file_list.html', files=files)

# 下載檔案
@app.route('/uploads/<filename>')
def download_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
