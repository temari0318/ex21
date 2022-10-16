import csv
import sqlite3

dbpath = "csvtest.db"
conn = sqlite3.connect(dbpath)
cur = conn.cursor()

sql = '''CREATE TABLE IF NOT EXISTS titanic
(
    PassengerId INTEGER,
    Survived INTEGER,
    Pclass TEXT,
    Name TEXT,
    Sex TEXT,
    Age TEXT,
    SibSp INTEGER,
    Parch INTEGER,
    Ticket TEXT,
    Fare REAL,
    Cabin TEXT,
    Embarked TEXT
)
'''

cur.execute(sql)
conn.commit()

#CSVファイルを開きリスト変数dataに読み込み

with open("titanic.csv", "r") as f:
  rows = csv.reader(f)
  
  #next関数でデータの1行目に存在するラベルをスキップ
  header = next(rows)
  
  data=[]
  
  for row in rows:
    data.append(row)

#executemany()で複数のINSERTを実行する

sql = '''INSERT INTO titanic
(PassengerID, Survived, Pclass, Name, Sex, Age, SibSp, Parch, Ticket, Fare, Cabin, Embarked)
VALUES
(?,?,?,?,?,?,?,?,?,?,?,?)
'''

cur.executemany(sql, data)
conn.commit()

cur.close()
conn.close()