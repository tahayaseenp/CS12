import requests  # imports module requests that helps in getting real time data from online
from tabulate import tabulate  # imports module tabulate thats allows the output to be formatted into proper tables 
import mysql.connector as m 

con = m.connect(host='localhost', user='root', password='root', database='cryptology') 
if con.is_connected: 
    print("connection succesful") 
else: 
    print("connection failed") 
cursor = con.cursor() 


def add(): 
    while True: 
        ch = int(input("To add to buy table records press (1)\nTo add to sold table records press (2)")) 
        if ch == 1: 
            coin = input("enter cryptocurreny symbol") 
            typeo = "buy" 
            exchange = input("enter name of exhange") 
            quantity = float(input("enter quantity")) 
            date = input("enter date of transaction") 
            value = float(input("enter value of crypto at the time of transaction")) 
            a = 0 
            b = "null"  
            idch = input("enter transaction id (example: B001,B002)") 
            sql = "insert into buy values('{}','{}','{}',{},'{}',{},{},'{}','{}')".format(
                typeo, coin, exchange, quantity, date, value, a, b, idch) 
            cursor.execute(sql) 
            con.commit() 
            yn = input("continue y/n?")
            if yn == "y": 
                pass 
            else: 
                break 
        
        elif ch == 2: 
            coin = input("enter cryptocurreny symbol") 
            typeo = "sell" 
            exchange = input("enter name of exhange") 
            quantity = float(input("enter quantity")) 
            date = input("enter date of transaction") 
            value = float(input("enter value of crypto at the time of buying")) 
            vas = float(input("enter value of crypto at the time of sale")) 
            a = "null" 
            idch = input("enter transaction id (example: S001,S002)")
            sql = "insert into sold values('{}','{}','{}',{},'{}',{},{},'{}','{}')".format(
                typeo, coin, exchange, quantity, date, value, vas, a, idch) 
            cursor.execute(sql) 
            con.commit() 
            yn = input("continue y/n?") 
            if yn == "y": 
                pass 
            else: 
                break  
        
 
def delete():
    while True:
        ch = int(input("To delete buy table records press (1)\nTo delete sold table records press (2)"))
        if ch == 1:
            idch = input("enter transaction id to delete")
            sql = "delete from buy where id='{}'".format(idch)
            cursor.execute(sql)
            con.commit()
            yn = input("continue y/n?") 
            if yn == "y":
                pass 
            else: 
                break

        elif ch == 2:
            idch = input("enter transaction id to delete")
            sql = "delete from sold where id='{}'".format(idch)
            cursor.execute(sql)
            con.commit()
            yn = input("continue y/n?") 
            if yn == "y":
                pass
            else: 
                break
        yn = input("continue y/n?") 
        if yn == "y":
            pass 
        else: 
            break


def edit():
    while True:
    ch = int(input("To edit 'buy' quantity and value per unit press (1)\nTo edit 'sold' quantity and value per unit at which it was sold at press (2)"))
    if ch == 1:
        idch = input("enter transaction id to be updated: ")
        price = float(input("enter new price per unit"))
        qty = float(input("enter new quantity: "))
        sql = "update buy set quantity={}, value={} where id='{}'".format(qty, price, idch)
        cursor.execute(sql)
        con.commit()
        yn = input("continue y/n?") 
        if yn == "y":
            pass 
        else: 
            break

    elif ch == 2:
        idch = input("enter transaction id to be updated: ")
        price = float(input("enter new price per unit for which it was sold at"))
        qty = float(input("enter new quantity: "))
        sql = "update sold set quantity={}, value_when_sold={} where id='{}'".format(qty, price, idch)
        cursor.execute(sql)
        con.commit()
        yn = input("continue y/n?") 
        if yn == "y":
            pass 
        else: 
            break
    
    yn = input("continue y/n?") 
    if yn == "y":
        pass 
    else: 
        break
         
 
def view(): 
    # enter the coins transaction that you want to view  
    while True: 
        ch = int(input("Buy table records press (1)\nSold table records press (2)")) 
        idch = input("enter id of transaction") 
        
        def update(ch, idch):
            if ch == 1: 
                a = "select currency from buy where id='{}'".format(idch) 
                cursor.execute(a) 
                rs = cursor.fetchall()
                for o in rs:
                    for l in o:
                        coin = l
                a = "select value from buy where id='{}'".format(idch) 
                cursor.execute(a) 
                rs = cursor.fetchall()
                for k in rs: 
                    for j in k: 
                        key = "https://api.binance.com/api/v3/ticker/price?symbol=" 
                        newkeyb = key+coin.upper()+'USDT' 
                        data = requests.get(newkey)   
                        data = data.json() 
                        textprice = f"{data['price']}" 
                        price = float(textprice) 
                        a = j - price 
                        if a > 0: 
                            profit = "↓ loss ↓" 
                        else: 
                            profit = '↑ profit ↑' 
                        # updates the value as per diff coins everytime they want to view  
                        sql = "update buy set current_value ={}, profit_loss='{}' where id='{}'".format(price, profit, idch) 
                        cursor.execute(sql) 
                        con.commit() 
                    sql = "select * from buy where id='{}'".format(idch) 
                    cursor.execute(sql) 
                    rs = cursor.fetchall() 
                    print(tabulate(rs, headers=['Type', 'Currency', 'Exchange', ' Quantity', 'Date',
                          'Value Bought At ($)', 'Current Value ($)', 'Profit_Loss', 'Id'], tablefmt='psql'))
            
            elif ch == 2:
                a = "select currency from buy where id='{}'".format(idch) 
                cursor.execute(a) 
                rs = cursor.fetchall()
                for o in rs:
                    for l in o:
                        coin = l

                a = "select value_when_bought from sold where id='{}'".format(idch) 
                cursor.execute(a) 
                rs = cursor.fetchall() 
                for k in rs: 
                    for j in k: 
                        a = float(j)
                g = "select value_when_sold from sold where id='{}'".format(idch) 
                cursor.execute(g) 
                rs = cursor.fetchall() 
                for x in rs: 
                    for y in x:
                        b = float(y)
                d = b - a
                         
                if d < 0: 
                    profit = '↓ loss ↓' 
                    sql = "update sold set profit_loss='{}' where id='{}'".format(profit, idch) 
                    cursor.execute(sql) 
                    con.commit() 
                elif d > 0: 
                    profit = '↑ profit ↑' 
                    sql = "update sold set profit_loss='{}' where id='{}'".format(profit, idch) 
                    cursor.execute(sql) 
                    con.commit() 
                else: 
                    print("error")
                sql = "select * from sold where id='{}'".format(idch) 
                cursor.execute(sql) 
                rs = cursor.fetchall() 
                print(tabulate(rs, headers=['Type', 'Currency', 'Exchange', ' Quantity', 'Date',
                      'Value When Bought ($)', 'Value When Sold ($)', 'Profit_Loss', 'Id'], tablefmt='psql'))
                
        update(ch, idch)
        yn = input("continue y/n?") 
        if yn == "y": 
            pass 
        else: 
            break


def crypto():
    while True:
        coin = input("enter cryptocurrency symbol")
        key = "https://api.binance.com/api/v3/ticker/price?symbol=" 
        newkey = key+coin.upper()+'USDT' 
        data = requests.get(newkey)   
        data = data.json() 
        textprice = f"{data['price']}" 
        price = float(textprice)
        print(coin, "value=", price, "USD")
        yn = input("continue y/n?")
        if yn == "y": 
            pass 
        else: 
            break


def viewall():
    while True:
        ch = int(input("To view buy table records press (1)\nTo view sold table records press (2)"))
        if ch == 1:
            sql = "update buy set current_value = 000, profit_loss='NULL'"
            cursor.execute(sql)
            con.commit()
            sql = "select type, currency, exchange, quantity, date, value, id from buy" 
            cursor.execute(sql) 
            rs = cursor.fetchall() 
            print(tabulate(rs, headers=['Type', 'Currency', 'Exchange', ' Quantity', 'Date', 'Value ($)', 'Id'], tablefmt='psql'))           
        elif ch == 2:
            sql = "update sold set profit_loss='NULL'"
            cursor.execute(sql)
            con.commit()
            sql = "select type, currency, exchange, quantity, date, value_when_bought, value_when_sold, id from sold" 
            cursor.execute(sql) 
            rs = cursor.fetchall() 
            print(tabulate(rs, headers=['Type', 'Currency', 'Exchange', ' Quantity', 'Date',
                  'Value When Bought ($)', 'Value When Sold ($)', 'Id'], tablefmt='psql'))

        yn = input("continue y/n?")
        if yn == "y": 
            pass 
        else: 
            break
                    

while True: 
    ch = int(input(
        """
_________________________________________________________________________________________
WELCOME TO CRYPTOLOGY : your solution to keeping track of all your crypto transactions.
_________________________________________________________________________________________
Press (1) To add records to buy or sell table

Press (2) To edit buy or sell table:

Press (3) To delete records from buy or sell table:

Press (4) To display individual records profit loss statement:

Press (5) To display all records of buy or sell transactions:

Press (6) To display current value of any cryptocurrency:

Press (any number) To exit from the program
_________________________________________________________________________________________
"""))
    
    if ch == 1: 
        add()
    elif ch == 2:
        edit()
    elif ch == 3:
        delete()
    elif ch == 4: 
        view()
    elif ch == 5: 
        viewall()
    elif ch == 6: 
        crypto()
    else:
        print("Thank You!")
        break