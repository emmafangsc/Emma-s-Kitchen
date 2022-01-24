class Dish:
    def __init__(self, dishname, meattype, cusinename, price, introduction):
        self.meattype = meattype
        self.cusinename = cusinename
        self.dishname = dishname
        self.price = price
        self.introduction = introduction
    def __repr__(self):
        return self.dishname
        


import enum
from typing import MutableSequence

class MeatType(enum.Enum):
    pork = 1
    chicken = 2
    beef = 3
    seafood = 4
    lamb = 5
    veggie = 6
    

class Cusine(enum.Enum):
    chinese = 1
    southeastAsian = 2
    asian = 3
    western = 4
    middleEastern = 5





all_dishes = [
    Dish('greek chickpea stew', MeatType.veggie, Cusine.middleEastern, 20, 'introduction'), 
    Dish('borek with spinach and feta cheese', MeatType.veggie, Cusine.middleEastern, 15, 'introduction'), 
    Dish('shakshuka', MeatType.veggie, Cusine.middleEastern, 20, 'introduction'), 
    Dish('moussaka', MeatType.beef, Cusine.middleEastern, 25, 'introduction'), 
    Dish('pide', MeatType.beef, Cusine.middleEastern, 20, 'introduction'),
    Dish('lahmacun/turkish pizza', MeatType.beef, Cusine.middleEastern, 20, 'introduction'), 
    Dish('risotto', MeatType.veggie, Cusine.western, 20, 'introduction'), 
    Dish('spicy and garlic pasta', MeatType.veggie, Cusine.western, 20, 'introduction'), 
    Dish('creamy pasta', MeatType.veggie, Cusine.western, 20, 'introduction'), 
    Dish('spanish omelette', MeatType.veggie, Cusine.western, 10, 'introduction'), 
    Dish('shepherds pie', MeatType.lamb, Cusine.western, 30, 'introduction'), 
    Dish('chili con carne', MeatType.beef, Cusine.western, 20, 'introduction'), 
    Dish('shrimp taco', MeatType.seafood, Cusine.western, 15, 'introduction'), 
    Dish('paella', MeatType.seafood, Cusine.western, 30, 'introduction'), 
    Dish('pesto salmon', MeatType.seafood, Cusine.western, 30, 'introduction'), 
    Dish('Chorizo pizza', MeatType.pork, Cusine.western, 20, 'introduction'), 
    Dish('chicken quesadilla', MeatType.chicken, Cusine.western, 15, 'introduction'), 
    Dish('enchilada', MeatType.chicken, Cusine.western, 20, 'introduction'), 
    Dish('chicken parm', MeatType.chicken, Cusine.western, 20, 'introduction'), 
    Dish('cottage pie', MeatType.beef, Cusine.western, 30, 'introduction'), 
    Dish('lasagna', MeatType.beef, Cusine.western, 30, 'introduction'), 
    Dish('swedish meatballs', MeatType.beef, Cusine.western, 25, 'introduction'), 
    Dish('okonomiyaki/japanese cabbage pancake', MeatType.veggie, Cusine.asian, 15, 'introduction'), 
    Dish('potato salad', MeatType.veggie, Cusine.asian, 10, 'introduction'), 
    Dish('kimichi pancake', MeatType.veggie, Cusine.asian, 15, 'introduction'), 
    Dish('seafood pancake', MeatType.seafood, Cusine.asian, 20, 'introduction'), 
    Dish('miso mackerel', MeatType.seafood, Cusine.asian, 20, 'introduction'), 
    Dish('kimichi mackerel stew', MeatType.seafood, Cusine.asian, 25, 'introduction'), 
    Dish('japanese beef curry', MeatType.beef, Cusine.asian, 35, 'introduction'), 
    Dish('beef bulgogi', MeatType.beef, Cusine.asian, 30, 'introduction'), 
    Dish('beef croquette', MeatType.beef, Cusine.asian, 15, 'introduction'), 
    Dish('korean fried chicken', MeatType.chicken, Cusine.asian, 20, 'introduction'), 
    Dish('jajangmyeon', MeatType.pork, Cusine.asian, 20, 'introduction'), 
    Dish('army stew', MeatType.pork, Cusine.asian, 30, 'introduction'), 
    Dish('kimchis stew with pork belly and tofu', MeatType.pork, Cusine.asian, 20, 'introduction'), 
    Dish('tonkotsu ramen', MeatType.pork, Cusine.asian, 15, 'introduction'), 
    Dish('curry puff', MeatType.veggie, Cusine.southeastAsian, 15, 'introduction'), 
    Dish('palak paneer', MeatType.veggie, Cusine.southeastAsian, 10, 'introduction'), 
    Dish('tofu omelette', MeatType.veggie, Cusine.southeastAsian, 10, 'introduction'), 
    Dish('mutton curry', MeatType.lamb, Cusine.southeastAsian, 40, 'introduction'), 
    Dish('Laab salmon', MeatType.seafood, Cusine.southeastAsian, 20, 'introduction'), 
    Dish('laksa', MeatType.seafood, Cusine.southeastAsian, 15, 'introduction'), 
    Dish('lime fish', MeatType.seafood, Cusine.southeastAsian, 25, 'introduction'), 
    Dish('stir fried minced pork with thai basil', MeatType.pork, Cusine.southeastAsian, 15, 'introduction'), 
    Dish('thai beef salad', MeatType.beef, Cusine.southeastAsian, 20, 'introduction'), 
    Dish('beef curry', MeatType.beef, Cusine.southeastAsian, 35, 'introduction'), 
    Dish('beef rendang', MeatType.beef, Cusine.southeastAsian, 40, 'introduction'), 
    Dish('chicken korma', MeatType.chicken, Cusine.southeastAsian, 25, 'introduction'), 
    Dish('butter chicken', MeatType.chicken, Cusine.southeastAsian, 25, 'introduction'), 
    Dish('chicken curry', MeatType.chicken, Cusine.southeastAsian, 25, 'introduction'), 
    Dish('pork belly summer rolls', MeatType.pork, Cusine.southeastAsian, 20, 'introduction'), 
    Dish('broccoli salad', MeatType.veggie, Cusine.chinese, 15, 'introduction'), 
    Dish('stir fried egg with tomato', MeatType.veggie, Cusine.chinese, 15, 'introduction'), 
    Dish('stir fried eggplant with cowbeans', MeatType.veggie, Cusine.chinese, 15, 'introduction'), 
    Dish('braised lamb', MeatType.lamb, Cusine.chinese, 40, 'introduction'), 
    Dish('stir fried lamb with leek', MeatType.lamb, Cusine.chinese, 25, 'introduction'), 
    Dish('salt and pepper shrimp', MeatType.seafood, Cusine.chinese, 25, 'introduction'), 
    Dish('sauerkraut fish', MeatType.seafood, Cusine.chinese, 30, 'introduction'), 
    Dish('braised fish with sichuan chili paste', MeatType.seafood, Cusine.chinese, 30, 'introduction'), 
    Dish('chicken salad/凉拌鸡', MeatType.chicken, Cusine.chinese, 20, 'introduction'), 
    Dish('braised chicken with taro', MeatType.chicken, Cusine.chinese, 25, 'introduction'), 
    Dish('chili chicken', MeatType.chicken, Cusine.chinese, 25, 'introduction'), 
    Dish('steamed pork belly with rice flour', MeatType.pork, Cusine.chinese, 25, 'introduction'), 
    Dish('sweet and sour ribs', MeatType.pork, Cusine.chinese, 30, 'introduction'), 
    Dish('double fried pork belly', MeatType.pork, Cusine.chinese, 20, 'introduction'),
    Dish('stir_fried beef', MeatType.beef, Cusine.chinese, 20, 'introduction'), 
    Dish('beef stew', MeatType.beef, Cusine.chinese, 35, 'introduction'), 
    Dish('cumin lamb', MeatType.lamb, Cusine.chinese, 30, 'introduction'), 
    Dish('sour and spicy fatty beef', MeatType.beef, Cusine.chinese, 25, 'introduction'), 
    ]

import random


print('\nHello, welcome to Emma\'s Kitchen!\n')

meatInput = input('What would you like to have for dinner, pork/chicken/beef/seafood/lamb/veggie/all?\n')

if meatInput == 'pork':
    meatInputEnum = MeatType.pork
elif meatInput == 'chicken':
    meatInputEnum = MeatType.chicken
elif meatInput == 'beef':
    meatInputEnum = MeatType.beef
elif meatInput == 'seafood':
    meatInputEnum = MeatType.seafood
elif meatInput == 'lamb':
    meatInputEnum = MeatType.lamb
elif meatInput == 'veggie':
    meatInputEnum = MeatType.veggie
else:
    meatInputEnum = ''

def dishes():
    dishes = [i for i in all_dishes if i.meattype == meatInputEnum]
    if meatInput == 'all':
        dishes = all_dishes
    return dishes
print('\n' + str(dishes()) + '\n')

cusineInput = input('Which cusine would you like to choose from, chinese/southeastAsian/asian/western/middleEast?\n')
if cusineInput == "chinese":
    cusineInputEnum = Cusine.chinese
elif cusineInput == 'southeastAsian':
    cusineInputEnum = Cusine.southeastAsian
elif cusineInput == 'asian':
    cusineInputEnum = Cusine.asian
elif cusineInput == 'western':
    cusineInputEnum = Cusine.western
elif cusineInput == 'middleEast':
    cusineInputEnum = Cusine.middleEastern
else:
    cusineInputEnum = ''

dishes = [i for i in dishes() if i.cusinename == cusineInputEnum]
print('\n' + str(dishes))
print('\n')

#dish_introduction

introInput = input('would you like to see the introduction of the dishes?\n')
def introduction():
    intro = ''
    for i in dishes:
        if introInput == 'yes':
            intro += '\n' + i.dishname + ': '+ i.introduction + '\n'
    return intro
print(introduction())

#bill

orderInput = input('Please place your order.\n')
order = orderInput.split(', ')

def bill(dishes, order):
    bill = 0
    for i in dishes:
        if i.dishname in order:
            bill += i.price
            message = '\nHere is your bill: ' + str(bill) + '\nThanks for visiting Emma\'s Kitchen!\n'
    return message

print(bill(dishes, order))

    


#weekly_menu 
    
weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
question = input('Hi Emma!\n Would you like to get your weekly menu for the week?')

def weeklyMenu():
    message = ""
    for i in weekdays:
        menu = str(random.sample(all_dishes, 3))
        print(i +': '+ str(random.sample(dishes, 3)) + '\n')
        message += '\n' + i + ': ' + menu + '\n'
    print(message)
    return message

if question == 'yes':
    print('\n Here is the menu for the week:')
    menuOfTheWeek = weeklyMenu()
else:
    print('\nAlright.')

