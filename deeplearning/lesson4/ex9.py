import torch
from torch import nn
from torch.utils.data import DataLoader

@torch.inference_mode()
def predict_tta(model: nn.Module, loader: DataLoader, device: torch.device, iterations: int = 2):
    model.eval()
    preds = []
    for i in range(iterations):
        prediction = []
        with torch.no_grad():
            for x,y in loader:
                x, y = x.to(device), y.to(device)
                pred = model(x)
                prediction.append(pred)
            preds.append(torch.cat(prediction))
    preds = torch.stack(preds).mean(dim=0)
    preds = torch.argmax(preds, dim=1)

    return preds


