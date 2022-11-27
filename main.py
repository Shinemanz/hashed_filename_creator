import glob
import os
import hashlib
import time
import sqlite3_scripts

# グローバル変数
file_extension = '.png'
path = os.getcwd() + '/' + '*' + file_extension
flist = glob.glob(path)
 
# ファイル名を一括で変更する
for file in flist:
  
  # データベースをアップデートする
  sqlite3_scripts.insert_item()

  # ハッシュ値に使用するデータを取得する
  data = sqlite3_scripts.fetch_item()

  # ハッシュ値を生成する
  hs = hashlib.md5(data.encode()).hexdigest()

  # ファイル名をハッシュ値に変更する
  os.rename(file, path.rstrip('*.png')  + hs + file_extension)

  # 早く処理しすぎると整合性が合わなくなるため0.1秒待つ
  time.sleep(0.1)