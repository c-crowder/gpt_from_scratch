import torch
from train import BigramLanguageModel, decode

device = "cuda" if torch.cuda.is_available() else "cpu"

model = BigramLanguageModel()
model.load_state_dict(torch.load("gpt_shakespeare.pth"))
model = model.to(device)

context = torch.zeros((1, 1), dtype=torch.long, device=device)

text = decode(model.generate(context, max_new_tokens=2000)[0].tolist())

with open("fake_shakespeare.txt", "w") as f:
    f.write(text)
