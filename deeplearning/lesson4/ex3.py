import torch
from torch import nn
from torch.utils.data import DataLoader


#
# Создайте пустой список для хранения предсказаний.
# Проитерируйтесь по даталоадеру.
# На каждой итерации сделайте forward pass для батча, посчитайте классы как аргмакс по выходу нейросети, по логитам,
# добавьте тензор с предсказаниями в список.
# Сделайте конкатенацию всех предсказаний и верните этот тензор длины N, по числу объектов в датасете.
# Ваша функция должна возвращать тензор с классами.


@torch.inference_mode()
def predict(model: nn.Module, loader: DataLoader, device: torch.device):
    model.eval()
    predictions = torch.empty(0)
    with torch.no_grad():
        for x,y in loader:
            x, y = x.to(device), y.to(device)

            output = model(x)
            pred = torch.argmax(output, dim=1)
            predictions = torch.cat((predictions, pred))

    return predictions

