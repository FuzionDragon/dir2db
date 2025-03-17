from pdb import main
import pandas as pd
import sqlite3
import sys
import os

def pushing(directory, db):
  conn = sqlite3.connect(db)
  table_schema = list(conn.execute("SELECT * FROM sqlite_schema;"))
  print(table_schema)
  for root, dirs, files in os.walk(directory):
    for i in files:
      if i.endswith(".csv"):
        print(i)


if __name__ == "__main__":
  n = len(sys.argv)
  result = [f for f in os.listdir('.') if f.endswith('.db')]
  if len(result) < 1:
    open('data.db', 'x')
    db = "data.db"
  else:
    db = result[0]

  if n == 2:
    print("Searching: " + sys.argv[1])
    pushing(sys.argv[1], db)
  else:
    print("Searching current directory")
    pushing('.', db)
