from torch import Tensor


y_pred = Tensor([
    [1, 1, 2, 2, 2],
    [1, 1, 2, 1, 2],
    [1, 0, 0, 0, 0],
    [2, 2, 2, 0, 0],
    [2, 1, 1, 1, 2]
])

y_true = Tensor([
    [1, 1, 1, 2, 2],
    [1, 1, 1, 2, 2],
    [1, 1, 1, 2, 2],
    [0, 0, 0, 2, 2],
    [0, 0, 0, 2, 2]
])

def jacar_mera(y_true, y_pred, item):
    intersection = ((y_pred == item) & (y_true == item)).sum().item()
    union = ((y_pred == item) | (y_true == item)).sum().item()
    return intersection/union

jaccard_0 = jacar_mera(y_true, y_pred, 0)
jaccard_1 = jacar_mera(y_true, y_pred, 1)
jaccard_2 = jacar_mera(y_true, y_pred, 2)

average_jaccard = (jaccard_0 + jaccard_1 + jaccard_2) / 3
average_jaccard = round(average_jaccard, 4)

print(average_jaccard)