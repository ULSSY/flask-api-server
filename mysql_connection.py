import mysql.connector


def get_connection():
        connection= mysql.connector.connect(
        host='yh-db.cahgiqgzpaou.ap-northeast-2.rds.amazonaws.com',
        database='memo_db',
        user='memo_user',
        password='2105'
    )
        return connection
        

    