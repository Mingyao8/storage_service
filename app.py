from flask import Flask, render_template, request, redirect, url_for, send_from_directory
import os

app = Flask(__name__)
UPLOAD_FOLDER = '/app/uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# 確保uploads資料夾存在
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == "POST":
        file = request.files.get('file')
        if file:
            # 處理檔案
            file.save(f"./uploads/{file.filename}")  # 假設存到本地的 uploads 資料夾
            flash('檔案上傳成功！')  # 顯示上傳成功訊息
            return redirect(url_for('upload_file'))  # 上傳成功後，重定向回該頁面

    return render_template("index.html")  # 這會渲染一個 HTML 表單

@app.route('/files')
def file_list():
    # 讀取uploads資料夾中的所有檔案
    files = os.listdir(UPLOAD_FOLDER)
    return render_template('file_list.html', files=files)

@app.route('/files/<filename>')
def download_file(filename):
    # 提供下載檔案的功能
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
