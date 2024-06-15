# MySQLdbのインポート
import mysql.connector

def login(user_name,password):
    # データベースへの接続とカーソルの生成
    # MySQLに接続
    conn = mysql.connector.connect(
        host="localhost",
        user="Yuichi",
        password="Ja245422kz",
        db="huac"
    )
    cursor = conn.cursor()

    # ここに実行したいコードを入力します

    sql = "SELECT * FROM user WHERE user_name = %s"
    cursor.execute(sql, (user_name,))
    result = cursor.fetchall()

    # 保存を実行
    conn.commit()

    # 接続を閉じる
    conn.close()

    if len(result) == 0:
        return 1
    elif result[0][1] == password:
        return 0
    else:
        return 2
