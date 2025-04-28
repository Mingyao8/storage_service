# 使用官方 Python 映像
FROM python:3.10-slim

# 設定工作目錄
WORKDIR /app

# 複製檔案
COPY . .

# 安裝依賴
RUN pip install flask

# 開放 Port
EXPOSE 5000

# 啟動指令
CMD ["python", "app.py"]
