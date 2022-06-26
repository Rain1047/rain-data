import os
import configparser
import pandas as pd
import sqlite3
# config = configparser.ConfigParser()
# config.read(os.path.abspath(os.path.join(".ini")))
# # print(os.path.abspath(os.path.join("app_ini")))
# print(config)

# complete_profile = pd.read_csv('dashboardapp/static/data/starbucks/complete_profile.csv')
database = "./dashboardapp/static/data/crypto/crypto.db"
con = sqlite3.connect(database)
print("connected!")

cur = con.cursor()
cur.execute("select * from bitcoin")