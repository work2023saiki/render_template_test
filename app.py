from flask import Flask, render_template, redirect, url_for

# ==================================================
# インスタンス生成
# ==================================================
app = Flask(__name__)

# ==================================================
# ルーティング
# ==================================================
# TOPページ
@app.route('/') 
def index():
    f = open('templates/top.html', encoding='utf-8', mode='w')  #'w'はwriteの略で書き込み可にしてる。
    f.write('test \n')
    f.close()
    return render_template('top.html')

@app.route('/a') 
def index2():
    f = open('templates/top.html', encoding='utf-8', mode='w')  #'w'はwriteの略で書き込み可にしてる。
    f.write('tes \n')
    f.close()
    a = 1
    
    return redirect(url_for('openfile'))

#@app.route('/openfile') 
def openfile():
    print('<h1>aa</h1>')
    
# ==================================================
# 実行
# ==================================================
if __name__ == '__main__':
    app.run()