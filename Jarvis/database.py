import mysql.connector
con = mysql.connector.connect(host='localhost', user='root', passwd='', database='test1')
mycur = con.cursor()
