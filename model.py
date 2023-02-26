import pickle
import random
import pandas
from sklearn.tree import DecisionTreeRegressor
import numpy as np


def item_one_hot(item):
    item = item.lower()
    items = [
        'tomato',
        'maize',
        'plaintain',
        'potatoes',
        'rice',
        'mustard',
        'soybeans',
        'sweet potatoes',
        'wheat',
        'onion'
    ]

    index = -1
    for i, ele in enumerate(items):
        if ele in item:
            index = i
    if 'sweet' in item:
        index = items.index("sweet potatoes")

    return [int(i == index) for i in range(len(items))]


def prediction(rainfall, temperature, item):
    crop_yield = pickle.load(open('models/model_pickled_crop_yield.pkl', 'rb'))
    price_calc = pickle.load(open('models/price_calc.pkl', 'rb'))
    temp = [rainfall, temperature]
    temp.extend(item_one_hot(item))
    temp = np.array([temp])
    # temp[0] = rainfall
    # temp[1] = temperature
    # print(temp)
    pred_yield = crop_yield.predict(temp)
    print("Item:", item, '\t\t\t', 'Price Prediction:', pred_yield[0])
    return price_calc[item_one_hot(item).index(1)]*10/(pred_yield)


def calc_for_everything(rainfall, temperature, items):
    for item in items:
        yield prediction(rainfall, temperature, item)[0]

if __name__ == '__main__':
    print(item_one_hot('rice'))
    print(prediction(2342,25,'maize'))
