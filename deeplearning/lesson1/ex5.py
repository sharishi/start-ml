import torch
from torch import nn
import numpy as np


# Если count_over равен 'columns', верните среднее тензора по колонкам.
# Если равен 'rows', то верните среднее по рядам.
# Гарантируется, что тензор будет матрицей (то есть будет иметь размерность 2).


def function01(tensor: torch.Tensor, count_over: str) -> torch.Tensor:
    if count_over == 'columns':
        return torch.mean(tensor, dim=0)
    elif count_over == 'rows':
        return torch.mean(tensor, dim=1)

# Напишите функцию function02.
# Функции на вход должен приходить датасет — тензор-матрица признаков объектов.
# Ваша функция должна создать тензор-вектор с весами
# (пусть они будут из равномерного распределения на отрезке от 0 до 1) и вернуть их для
# дальнейшего обучения линейной регрессии без свободного коэффициента.
# Сделайте эти веса типа float32, для них нужно будет в процессе обучения вычислять градиенты
# (воспользуйтесь requires_grad).


def function02(dataset: torch.Tensor) -> torch.Tensor:
    num_features = dataset.shape[1]
    weights = torch.rand(num_features, dtype=torch.float32)

    weights.requires_grad = True

    return weights

# Напишите функцию function03.
# Она должна принимать тензор-матрицу с объектами и тензор-вектор с правильными ответами,
# будем решать задачу регрессии: def function03(x: torch.Tensor, y: torch.Tensor):
# Создайте внутри функции веса для линейной регрессии (без свободного коэффициента),
# можете воспользоваться функцией из предыдущего степа.
# С помощью градиентного спуска подберите оптимальные веса для входных данных (используйте длину шага около 1e-2).
# Верните тензор-вектор с оптимальными весами из функции.
# Ваши обученные веса должны давать MSE на обучающей выборке меньше единицы.


n_features = 2
n_objects = 300

w_true = torch.randn(n_features)
X = (torch.rand(n_objects, n_features) - 0.5) * 5
Y = X @ w_true + torch.randn(n_objects) / 2


def function03(x: torch.Tensor, y: torch.Tensor) -> torch.Tensor:

    w = function02(x)

    learning_rate = 1e-2
    tolerance = 1e-1
    max_iter = 1000

    for i in range(max_iter):
        # Вычисляем ошибку
        y_pred = x @ w
        loss = torch.mean((y - y_pred) ** 2)

        if loss.item() < tolerance:
            break

        # Вычисляем градиенты
        loss.backward()

        # Отключаем подсчет градиентов для обновления весов
        with torch.no_grad():
            w -= learning_rate * w.grad

        # Включаем подсчет градиентов и обнуляем градиенты
        w.grad.zero_()

    return w

# Напишите функцию function04. Она должна принимать тензор-матрицу с объектами и тензор с правильными ответами,
# будем решать задачу регрессии: def function04(x: torch.Tensor, y: torch.Tensor):
# Создайте внутри функции полносвязный слой,обучите этот полносвязный слой на входных данных
# с помощью градиентного спуска (используйте длину шага около 1e-2). Верните его из функции.
# Ваш полносвязный слой должен давать MSE на обучающей выборке меньше 0.3.
# Отправляемый файл должен иметь расширение .py


def function04(x: torch.Tensor, y: torch.Tensor):
    layer = nn.Linear(x.shape[1], 1, bias=True)
    mse = torch.tensor([1])

    while mse >= 0.3:
        mse = torch.mean((layer(x).ravel() - y) ** 2)
        mse.backward()

        with torch.no_grad():
            layer.weight -= layer.weight.grad * 1e-2
            layer.bias -= layer.bias.grad * 1e-2

        layer.zero_grad()

    return layer



