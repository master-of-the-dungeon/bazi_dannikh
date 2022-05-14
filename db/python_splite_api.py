import json
# import sqlite3
# cur = sqlite3.connect('peniss.db',check_same_thread=False).cursor()
def getallitems(cur):
    items_list = {'items':[]}
    for row in cur.execute('select * from goods'):
        item = {'id':row[0], 'name':row[1], 'category':row[2],'distributor':row[3], 'quantity':row[4], 'price_USD':row[5]}
        items_list['items'].append(item)
    return json.dumps(items_list,ensure_ascii=False)


def getitems_sortedpricerange(cur):
    items_list= {'items': []}
    for row in cur.execute('select name, price_USD from goods order by price_USD DESC;'):
        item = {'name': row[0], 'price_USD': row[1]}
        items_list['items'].append(item)
    return json.dumps(items_list, ensure_ascii=False)
# def getproductid(cur):
#     items_list = {'items':[]}
#     for row in cur.execute('select id from goods'):
# def allproductincategory(cur):
#     for row in cur.execute('select name, price_USD, category from goods order by category;'):
#         print(row)
#



def mostexpensive(cur):
    items_list = {'items':[]}
    for row in cur.execute('select name, max(price_USD) from goods;'):
        item = {'name': row[0], 'price_USD': row[1]}
        items_list['items'].append(item)
    return json.dumps(items_list, ensure_ascii=False)

def cheapest(cur):
    items_list = {'items':[]}
    for row in cur.execute('select name, min(price_USD) from goods;'):
        item = {'name': row[0], 'price_USD': row[1]}
        items_list['items'].append(item)
    return json.dumps(items_list, ensure_ascii=False)
#
# def getpricerange(cur):
#     for row in cur.execute('select name, price_USD from goods WHERE price_USD BETWEEN '+str(input())+' AND '+str(input())+';'):
#         print(row)
# def delete_goods_id():
#
# def delete_category_id():
#


