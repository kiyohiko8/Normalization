"""
このプログラムはTwitterデータを正規化するための'修正版'プログラムです.

[改良点]
	- アルファベット表記に対応できるようにした.
	- 引用URLを取り除いた.
	- 顔文字を取り除いた

"""

import subprocess
import codecs
import re, os
import pandas as pd

print("移動前：",os.getcwd())
os.chdir('"作業ディレクトリ名"')
print("移動後：",os.getcwd())


datas = pd.read_csv("'読み込むデータ名'", header = None)
fout = codecs.open("'保存するテキストデータ名'", "w", "utf-8")
for key, row in datas.iterrows():
	tweet = str(row[5])
	tweet = re.sub("@.* ", "", tweet)
	tweet = re.sub("https.*", "", tweet)
	tweet = re.sub("RT.*　", "", tweet)
	tweet = re.sub("（.*）", "", tweet)
	tweet = re.sub("\(.*\)", "", tweet)
	
	#リストの書き込みはwritelines
	fout.writelines(tweet)

fout.close()
	
