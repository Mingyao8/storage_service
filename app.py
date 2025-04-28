import os
from flask import Flask, request, render_template, send_from_directory
import shutil

app = Flask(__name__)
UPLOAD_FOLDER = '/home/mingyao/flask_uploads'  # 檔案存放的資料夾
ALLOWED_EXTENSIONS = {'pdf', 'doc', 'docx', 'txt', 'jpg', 'png'}
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# 確保上傳目錄存在
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# 檢查副檔名是否允許
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

# 上傳檔案
@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        if 'file' not in request.files:
            return '沒有檔案'
        file = request.files['file']
        if file.filename == '':
            return '沒有選擇檔案'
        if file and allowed_file(file.filename):
            filename = file.filename
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            return '檔案上傳成功'
        else:
            return '不允許的檔案類型'
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
    html = '''
    <!doctype html>
    <title>檔案列表</title>
    <h1>檔案列表</h1>
    <ul>
    '''
    for filename in files:
        html += f'<li><a href="/uploads/{filename}">{filename}</a></li>'
    html += '''
    </ul>
    <a href="/">返回上傳頁面</a>
    '''
    return html

# 下載檔案
@app.route('/uploads/<filename>')
def download_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
