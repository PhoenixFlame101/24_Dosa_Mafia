import pickle

example_dict = {1: "6", 2: "2", 3: "f"}

example_dict = {
    0: 61000,
    1: 86830.11,
    2: 686830.11,
    3: 30 * 15000.12,
    4: 107399.70,
    5: 51078.23,
    6: 55384.89,
    7: 23 * 10 * 2812.12,
    8: 71929.71,
    9: 28 * 20531.23,
}

pickle.dump(example_dict, open("models/price_calc.pkl", "wb"))
