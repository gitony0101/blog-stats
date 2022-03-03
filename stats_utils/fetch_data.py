from sklearn.datasets import fetch_openml


def digits(save=None):

    X, y = fetch_openml('mnist_784',
                        version=1,
                        as_frame=True,
                        return_X_y=True,
                        data_home='data')
    y = y.astype(np.int8)

    if save:
        X.to_feather('../../data-handson/mnist_784_X.feather')
        y.to_frame().to_feather('../../data-handson/mnist_784_y.feather')

    return X, y
