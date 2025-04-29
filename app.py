import os
from flask import Flask, request, render_template, flash, redirect, url_for

app = Flask(__name__)
app.secret_key = 'supersecretkey'  # 這是為了使用 flash() 訊息，請確保設定 secret_key
UPLOAD_FOLDER = './uploads'  # 上傳檔案存放的資料夾
os.makedirs(UPLOAD_FOLDER, exist_ok=True)  # 確保上傳資料夾存在

@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        file = request.files.get('file')
        if file:
            # 處理檔案
            file.save(os.path.join(UPLOAD_FOLDER, file.filename))  # 儲存檔案到 uploads 資料夾
            flash('檔案上傳成功！')  # 顯示上傳成功訊息
            return redirect(url_for('file_list'))  # 上傳成功後，重定向到檔案列表頁面

    return render_template("index.html")  # 上傳檔案的表單頁面

@app.route('/files')
def file_list():
    # 讀取 uploads 資料夾中的所有檔案
    files = os.listdir(UPLOAD_FOLDER)
    return render_template('file_list.html', files=files)  # 顯示檔案列表頁

@app.route('/files/<filename>')
def download_file(filename):
    # 提供下載檔案的功能
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
