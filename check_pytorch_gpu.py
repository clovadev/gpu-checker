import torch

print(torch.cuda.is_available())
print(torch.rand(5, 3, device='cuda'))
