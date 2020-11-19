"""
日報系テキストの定型文を自動出力するPython3プログラム
2020-11-19製作
"""

import os
import datetime

now = datetime.datetime.now()

path='todaysreport.txt'

with open(path,'w') as f:
	f.write('{0:%Y-%m-%d}'.format(now)+' 【氏名】日報\nおつかれさまです。本日の業務報告をお送り致します。ご査収ください。\n')
	f.write('▼{0:%Y-%m-%d}'.format(now)+'【氏名】日報')
	
os.rename('todaysreport.txt', '{0:%Y%m%d}.txt'.format(now))

"""
---------------------------------------------------------
以下解説文です。

▼コード行ごとの意図:
> 001; import os
	os モジュールのうち、open関数 ("with open ... as f" 記法を伴う) と、os.rename関数の2つを使うために導入する。

> 002; import datetime
	datetimeモジュールのうち、datetime.datetime 関数を使うために導入する。
	
> 004; 
	変数now に現在の日時を代入する。
	【参考】https://note.nkmk.me/python-datetime-now-today/
> 006;
	これから作るファイルの名称を決める。
	あとで結局名前を日付に合わせてリネームするので、ここは適当でよい。

> 008-010; open関数の変形文法 with open (object_x, 'mode') as f: と write関数
	【参考】with open 記法 https://note.nkmk.me/python-file-io-open-with/
	【参考】open関数のファイルオブジェクトとして仮に定義したf を使ってwrite関数 f.write を実行

>012; os.rename関数を経由して 日付 now の値を代入
	【参考】datetime関数をファイル名の文字列に代入する方法 https://ja.stackoverflow.com/questions/19552/python-%E3%83%86%E3%82%AD%E3%82%B9%E3%83%88%E3%83%95%E3%82%A1%E3%82%A4%E3%83%AB%E3%81%AE%E5%90%8D%E5%89%8D%E3%81%AB%E6%97%A5%E4%BB%98%E3%82%92%E5%85%A5%E3%82%8C%E3%81%9F%E3%81%84
	
	解説以上
	---------------------------------------------------------
	"""