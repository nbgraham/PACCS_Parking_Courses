import pandas as pd
from random import randint
import numpy as np


def spread(n=1000, epochs=1000):
    er = [np.abs(perc_error(3, n=n)*100) for _ in range(epochs)]
    return pd.Series(er).describe()


def perc_error(n_sets, n=1000):
    test = random_sets(n_sets, pop_size=n)
    real, estimated = in_all(test)
    return (estimated - real) / real


randBinList = lambda n: [randint(0, 1) for _ in range(n)]
def random_sets(n_sets, pop_size=1000):
    data = [randBinList(n_sets) for _ in range(pop_size)]
    df = pd.DataFrame(data)
    return df


def in_all(data):
    res = 1
    for i in data.columns:
        res = data[i].multiply(res)

    trueABC = np.sum(res)

    def mult(i):
        res = 1
        for j in data.columns:
            if j != i:
                res *= np.sum(data[i].multiply(data[j]))
        return res

    predictedABC = np.sum([mult(i)/np.sum(data[i])**(len(data.columns)-2) for i in data.columns])/len(data.columns)

    return trueABC, predictedABC


def main():
    print(spread(n=1000))


if __name__ == '__main__':
    main()