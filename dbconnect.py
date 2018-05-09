import pymysql
import pymysql.cursors
def connection():
    conn=pymysql.connect(host="endpoint url",
                         user='username',
                         password='password',
                         db='database name')
    c=conn.cursor()

    return c, conn