# hashed_filename_creator

説明：
一意のファイル名を作成するためにハッシュされた任意のファイル名を作成できます。

使い方
1: create_database.py を実行してデータベースを作成する  
2: 名前を変更したいすべてのファイルを集めて、main.pyと同じフォルダーに配置します (すべてのファイルの拡張子が同じであることを確認してください)。
3: main.pyを実行する

注意事項:
このモジュールは、ワードプレス環境で使用して、一意の .png ファイル名を作成することが期待されています。
.pngファイル以外の名前を変更する場合は、main.py下、filename_extensionのパラメータを変更する必要があります。

Make any filenames hashed to make unique names

Description:
You can make any filenames hashed to make unique filenames.

How to use
1: Create database executing create_database.py
2: Gather all files you want to change names and put them in the same folder as main.py (make sure all of them are the same file extensions)
3: Execute main.py

Precaution:
This module is expected to use in wordpress environment to make unique .png filenames.
If you want to change names other than .png file, you need to change code main.py filename_extension parameter.
