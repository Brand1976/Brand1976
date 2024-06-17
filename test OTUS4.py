import numpy as np
def get_unique_rows(X):
    # Your code here
    X_unique = X[[0,]]
    for a in X:
        print ('a = ',type(a), a)
        print ('X_unique = ', type(X_unique), X_unique)
        input('нажми')
        if a not in X_unique:
            print('сработал if')
            X_unique = np.concatenate((X_unique, a), axis = 0)
    return X_unique

X = np.random.randint(4, 6, size=(10,3))
print(X)

get_unique_rows(X)

