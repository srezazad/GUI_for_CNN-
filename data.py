from sklearn.datasets import make_classification
import pandas as pd
from imblearn.under_sampling import CondensedNearestNeighbour
import seaborn as sns
import matplotlib.pyplot as plt

cnn = CondensedNearestNeighbour(
    sampling_strategy='auto',  # undersamples only the majority class
    random_state=0,
    n_neighbors=1,
    n_jobs=-1)  # all cores

class Data():

    def __init__(self, sep=2, n_samples=100, weights=.99):
        X,y = make_classification(n_samples= n_samples,
                                   n_features=2,
                                   n_redundant=0,
                                   n_clusters_per_class=1,
                                   weights=[weights],
                                   class_sep = sep,  # how separate the classes are
                                   random_state =1)

        self.X = pd.DataFrame(X, columns=['x', 'y'])
        self.y = pd.Series(y)
        X_resampled, y_resampled = cnn.fit_resample(X, y)
        self.X_resampled = pd.DataFrame(X_resampled, columns=['x', 'y'])
        self.y_resampled = pd.Series(y_resampled)

        plt.clf()

        sns.scatterplot(
            data=self.X_resampled, x="x", y="y", hue=self.y_resampled)
        plt.title('Undersampled data')
        plt.savefig('Undersampled.png')

        plt.clf()

        sns.scatterplot(
            data=self.X, x="x", y="y", hue=self.y
        )
        plt.title('Original data')
        plt.savefig('Original.png')





