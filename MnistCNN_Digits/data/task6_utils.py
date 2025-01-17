import numpy as np

import torch
import torchvision
from torchvision.transforms import Compose, ToTensor, Normalize

from matplotlib import pyplot as plt

def load_MNIST(batch_size: int, normalize_vals: tuple[float, float]) -> tuple:

    # for correctly download the dataset using torchvision, do not change!
    from six.moves import urllib
    opener = urllib.request.build_opener()
    opener.addheaders = [('User-agent', 'Mozilla/5.0')]
    urllib.request.install_opener(opener)

    norm1_val, norm2_val = normalize_vals

    transforms = Compose([ToTensor(), Normalize((norm1_val,), (norm2_val,))])


    train_dataset = torchvision.datasets.MNIST(root='MNIST-data',
                                               train=True,
                                               download=True,
                                               transform=transforms)

    test_dataset = torchvision.datasets.MNIST(root='MNIST-data', 
                                              train=False,
                                              transform=transforms)


    train_loader = torch.utils.data.DataLoader(dataset=train_dataset,
                                               batch_size=batch_size,
                                               shuffle=False)


    test_loader = torch.utils.data.DataLoader(dataset=test_dataset,
                                              batch_size=batch_size,
                                              shuffle=False)

    return train_dataset, test_dataset, train_loader, test_loader


def convert_data_to_numpy(dataset) -> tuple[np.ndarray, np.ndarray]:
    X = []
    y = []
    for i in range(len(dataset)):
        X.append(dataset[i][0][0].flatten().numpy())# flatten it to 1d vector
        y.append(dataset[i][1])

    X = np.array(X)
    y = np.array(y)

    return X, y

# for plotting the low-dimensional points from PCA in Question 2
def plot_points(points_x: list[float], points_y: list[float], labels: list[int], filename: str) -> None:

    points_x = np.array(points_x)
    points_y = np.array(points_y)
    group = np.array(labels)
    cdict = {0: 'tab:blue',
             1: 'tab:orange',
             2: 'tab:green',
             3: 'tab:red',
             4: 'tab:purple',
             5: 'tab:brown',
             6: 'tab:pink',
             7: 'tab:gray',
             8: 'tab:olive',
             9: 'tab:cyan'}
    
    fig, ax = plt.subplots()
    for g in np.unique(group):
        ix = np.where(group == g)
        ax.scatter(points_x[ix], points_y[ix], c = cdict[g], label = g, s = 10)
    ax.legend()
    
    plt.savefig(filename)
    
