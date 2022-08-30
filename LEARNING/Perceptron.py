import numpy as np


class Perceptron:
    """
    Classificator based on perceptron.
    -----------
    eta : float
        Speed of learning
    n_iter : int
        Iterations each dataset
    random_state : int
        Base state for random numbers generator for random weights initialization.
    -----------
    w_ : one-dimensional array
        Weights for learning
    errors_ : list
        The number of wrong qualifications in each epoch.
    """

    def __init__(self, eta=0.01, n_iter=50, random_state=1):
        self.eta = eta
        self.n_iter = n_iter
        self.random_state = random_state

    def fit(self, x, y):
        """
        Learning the model.
        ---------
        x : {equal to array}, shape = {n_examples, n_features}
            Learning vectors.
        y : {equal to array}, shape = {n_examples}
            Target value.
        ---------
        :returns
        object
        """
        rgen = np.random.RandomState(self.random_state)
        self.w_ = rgen.normal(loc=0.0, scale=0.01, size=1+x.shape[1])
        self.errors_ = []

        for _ in range(self.n_iter):
            errors = 0
            for xi, target in zip(x, y):
                update = self.eta * (target - self.predict(xi))
                self.w_[1:] += update * xi
                self.w_[0] += update
                errors += int(update != 0.0)
            self.errors_.append(errors)
        return self

    def net_input(self, x):
        """Calculate all input."""
        return np.dot(x, self.w_[1:]) + self.w_[0]

    def predict(self, x):
        """Returns value of the class after the step."""
        return np.where(self.net_input(x) >= 0.0, 1, -1)
