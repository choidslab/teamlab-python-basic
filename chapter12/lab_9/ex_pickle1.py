import pickle

with open('list.pickle', 'wb') as pf:
    test = [1, 2, 3, 4, 5]
    pickle.dump(test, pf)

with open('list.pickle', 'rb') as pf:
    test_pickle = pickle.load(pf)
    print(test_pickle)

