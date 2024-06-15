# ①app.py
from flask import Flask, render_template, request
import app.pgm01 as pgm01

app = Flask(__name__)


# form情報を格納するクラス
class UserInfo:
   def __init__(info, user_name, password):
       info.user_name = user_name
       info.password = password

# サインインページ
@app.route('/')
def sign_up():
   return render_template('signup.html')


# サインイン情報を表示するページ
@app.route('/home', methods=['GET', 'POST'])
def home():
    info = UserInfo(
        request.form.get('user_name'),
        request.form.get('password')
    )
    ret_cd = pgm01.login(info.user_name,info.password)

    if ret_cd == 0:
        return render_template('home.html', info=info)
    else:
        if ret_cd == 1:
            msg = "未登録のユーザーＩＤです。"
        else:
            msg = "パスワードが異なります。"
        return render_template('resignup.html', msg=msg)





if __name__ == '__main__':
   app.run(debug=True)