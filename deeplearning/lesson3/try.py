import warnings

import matplotlib.pyplot as plt
import numpy as np
import torch
import torch.nn as nn
import torchvision.transforms as T
from IPython.display import clear_output
from PIL import Image
from matplotlib import cm
from time import perf_counter
from torch.utils.data import DataLoader
from torchvision.datasets import MNIST
from tqdm import tqdm

warnings.filterwarnings('ignore')


def count_parameters_conv(in_channels: int, out_channels: int, kernel_size: int, bias: bool):
    parameters = in_channels * kernel_size ** 2 * out_channels
    if bias:
        parameters += out_channels
    return parameters



