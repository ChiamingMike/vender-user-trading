# vender-user-trading
# simple trading code for practice

import sys

class Items:
    def __init__(self,item,price,quantity):
        self.item = item
        self.price = price
        self.quantity = quantity
    def buyer_item_info(self):
        for i in range(len(self.item)):
            print(self.item[i],':',self.quantity[i])
    def seller_item_info(self):
        for i in range(len(self.item)):
            print(self.item[i],':',self.quantity[i],' --- ',self.price[i],'dollars for each one.' )

class People:
    def __init__(self,money):
        self.money = money
    def buyerMoney(self):
        print('Now you have ' + str(self.money) + ' dollars.\n')
    def sellerMoney(self):
        print('Sales: '+ str(self.money) + ' dollars.\n')

def check_item_name():
    while True:
        askItem = str(input('Which one do want to buy ? ')).upper()
        if askItem not in items:
            print('Sorry, we don\'t sell {}.'.format(askItem))
        else:
            index = items.index(askItem)
            if quantities[index] == 0:
                print('That one is out of stock.')
            else:
                return askItem,index

def check_item_quantity(item_name,index):
    while True:
        askAmount = int(input('How many {} do you want ?'.format(item_name)))
        if askAmount > quantities[index]:
            print('Sorry, we only have {}.'.format(quantities[index]))
        elif askAmount * prices[index] > set_money - sum(record_trades):
            print('You cannot afford it.')
        else:
            quantities[index] = quantities[index] - askAmount #update item's stock
            return askAmount

def update_buyer_item_info(item_name,item_quantity):
    if item_name not in soldLst:
        soldLst.append(item_name)
        soldquantities.append(item_quantity)
    elif item_name in soldLst:
        soldLstIndex = soldLst.index(item_name)
        soldquantities[soldLstIndex] = soldquantities[soldLstIndex] + item_quantity

def gameover():
        if set_money - sum(record_trades) == 0:
            print('You don\'t have money.')
            sys.exit()
        elif set_money - sum(record_trades) < prices[0]:
            print('You don\'t have enough money to buy other appliances.')
            sys.exit()
#generated sellerLst object
items = ['PRINTER','PC','IPHONE','TV']
prices = [40,100,150,200]
quantities = [5,12,10,2]
sellerLst = Items(items,prices,quantities)
#generated buyLst object
soldLst = []
soldquantities = []
buyerLst = Items(soldLst,prices,soldquantities)

set_money = int(input('How much do you earn each month? '))
record_trades = []
#show sellerLst
print('\nWelcome! This shop is selling appliances as below :')
print('----------We\'re selling----------')
sellerLst.seller_item_info()
print('----------------------------------')
while True:
    #ask for the item name then check if that item is on the seller's list or out of stock
    #if it's on the list then find the index
    item_name,index = check_item_name()
    #ask for the amount then check if seller have enough items can sell
    #if seller has enough items, updating the item's stock
    #but if buyer cannot afford the payment then ask amount again
    item_quantity = check_item_quantity(item_name,index)
    #update buyerLst and show what buyer have
    update_buyer_item_info(item_name,item_quantity)
    print('----------You have----------')
    buyerLst.buyer_item_info()
    print('----------------------------')
    #update money and record trades for caculating sales
    need2pay = int(item_quantity * prices[index])
    record_trades.append(need2pay)
    #tell buyer the payment
    print('It cost '+ str(need2pay)+' dollars.')
    buyer = People(set_money - sum(record_trades))
    buyer.buyerMoney()
    #check if buyer's money = 0 or cannot buy the cheapest one
    gameover()
    #show sellerLst
    print('----------We\'re selling----------')
    sellerLst.seller_item_info()
    print('----------------------------------')
    seller = People(sum(record_trades))
    seller.sellerMoney()

