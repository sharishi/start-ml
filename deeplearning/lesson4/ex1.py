import torch


def get_normalize(features: torch.Tensor):
    means = features.data.mean(axis=(0, 2, 3))
    stds = features.data.std(axis=(0, 2, 3))

    return means, stds
