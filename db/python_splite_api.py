import sqlite3
import json

con = sqlite3.connect('peniss.db')
cur = con.cursor()

def getallitems():
    for row in cur.execute('select * from goods'):
        print(row)

def getproductid():
    for row in cur.execute('select good_id from goods where name = '+str(input())+';'):
        print(row)
def allproductincategory():
    for row in cur.execute('select name, price_USD, category from goods order by category;'):
        print(row)

def getitems_sortedpricerange():
    for row in cur.execute('select name, price_USD from goods order by price_USD DESC;'):
        print(row)
def mostexpensive():
    for row in cur.execute('select name, max(price_USD) from goods;'):
        print(row)

def cheapest():
  for row in cur.execute('select name, min(price_USD) from goods;'):
    print(row)

def getpricerange():
    for row in cur.execute('select name, price_USD from goods WHERE price_USD BETWEEN '+str(input())+' AND '+str(input())+';'):
        print(row)
# def delete_goods_id():
#
# def delete_category_id():
#


mostexpensive()