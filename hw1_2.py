import sys

class People:
    def __init__(self,money,products):
        self.money = money
        self.products = products
    def belongings(self):
        for name,value in zip(self.products, self.products.values()):
            print(name,':',value[0],' --- ',value[1],'dollars for each one.' )
        if self.money != 0:
            print('Money: ' + str(self.money) + ' dollars.\n')
    def trading(self,name,quantity,operator):
        self.money = int(self.money) + int(quantity) * int(self.products[name][1]) * int(operator)

products = {
'PRINTER' : [5,40],
'PC'      : [12,100],
'IPHONE'  : [10,150],
'IPOD'    : [8,120],
'TV'      : [2,200] }
vender = People(0,products)

print('\nWelcome! This shop is selling appliances as below :')
print('----------We\'re selling----------')
vender.belongings()
print('----------------------------------')
user = People(input('How much do you earn each month? '),{})

while True:
    name,quantity = str(input('Please enter the name and quantity of the products (e.g. PC,2)......')).split(',')
    name = name.upper()
    if name not in products.keys():
        print('Sorry, we don\'t sell {}.'.format(name))
    elif products[name][0] == 0:
        print('That one is out of stock.')
    elif int(quantity) > int(products[name][0]):
        print('Sorry, we only have {}.'.format(products[name][0]))
    elif int(quantity) * int(products[name][1]) > int(user.money):
        print('You cannot afford it.')
    else:
        if name not in user.products.keys():
            user.products[name] = [quantity,products[name][1]]
        elif name in user.products.keys():
            user.products[name][0] = int(user.products[name][0]) + int(quantity)
        vender.products[name][0] = int(vender.products[name][0]) - int(quantity)
        user.trading(name,quantity,-1)
        vender.trading(name,quantity,1)
        print('----------What you have----------')
        user.belongings()
        if user.money == 0 or user.money < products['PRINTER'][1]:
            print('You don\'t have enough money to buy other appliances.')
            sys.exit()
        print('----------We\'re selling----------')
        vender.belongings()
