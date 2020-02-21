import pickle


class Multiply(object):

    def __init__(self, multiplier):
        self.multiplier = multiplier

    def multiply(self, number):
        return number * self.multiplier


multiply = Multiply(5)
multiply.multiply(10)

with open('multiply_obj.pickle', 'wb') as f:
    pickle.dump(multiply, f)  # pickle 파일에 multiply 객체(object) 저장

with open('multiply_obj.pickle', 'rb') as f:
    multiply_pickle = pickle.load(f)
    print(multiply_pickle.multiply(5))
