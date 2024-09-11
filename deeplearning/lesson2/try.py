import torch
from torch import nn
from torch.optim import Optimizer
from torch.utils.data import DataLoader


# Напишите функцию create_model, которая должна возвращать полносвязную нейронную сеть из двух слоев.
# На вход должно быть 100 чисел, на выход 1, посередине 10. В качестве нелинейности используйте ReLU.
# Воспользуйтесь nn.Sequential и передайте слои как последовательность.


def create_model():
    net = nn.Sequential(
        nn.Linear(100, 10),
        nn.ReLU(),
        nn.Linear(10, 1),
    )
    return net

# Напишите функцию train. Она должна принимать на вход нейронную сеть, даталоадер, оптимизатор и функцию потерь.
# Внутри функции сделайте следующие шаги:
# 1. Переведите модель в режим обучения.
# 2. Проитерируйтесь по даталоадеру.
# 3. На каждой итерации:
# Занулите градиенты с помощью оптимизатора
# Сделайте проход вперед (forward pass)
# Посчитайте ошибку
# Сделайте проход назад (backward pass)
# Напечатайте ошибку на текущем батче с точностью до 5 символов после запятой (только число)
# Сделайте шаг оптимизации
# Функция должна вернуть среднюю ошибку за время прохода по даталоадеру.


def train(model: nn.Module, data_loader: DataLoader, optimizer: Optimizer, loss_fn):
    model.train()

    final_loss = 0

    for i, (x, y) in enumerate(data_loader):

        optimizer.zero_grad()

        output = model(x)

        loss = loss_fn(output, y)

        loss.backward()

        print(f'{loss.item():.5f}')

        optimizer.step()

        final_loss += loss.item()

    return final_loss/len(data_loader)


# Напишите функцию evaluate. Она должна принимать на вход нейронную сеть, даталоадер и функцию потерь.
# Внутри функции сделайте следующие шаги:
# 1. Переведите модель в режим инференса (применения)
# 2. Проитерируйтесь по даталоадеру
# 3. На каждой итерации:
# Сделайте проход вперед (forward pass)
# Посчитайте ошибку
# Функция должна вернуть среднюю ошибку за время прохода по даталоадеру.


def evaluate(model: nn.Module, data_loader: DataLoader, loss_fn):
    model.eval()
    final_loss = 0
    with torch.no_grad():
        for i, (x, y) in enumerate(data_loader):
            output = model(x)
            loss = loss_fn(output, y)

            final_loss += loss.item()

    return final_loss / len(data_loader)
