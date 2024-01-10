# GPT_From_Scratch

### What
This repository is a recreation of chat gpt's decoder only transformer architecture trained on the tiny Shakespeare dataset. It was made in coordination with Karpathy's video, and it was trained on my local machine.

Chat GPT uses this same style architecture for their model, but they take it quite a bit further. The training data is magnitudes larger than this training data, and the size of the network is also magnitudes larger. Even still, the model only predicts the next word in a sentence. This creates a babble like affect - as can be seen from this model's ability to create babble nonsense that sounds like Shakespeare. Chat GPT goes through an extensive process of alignment which is not present here as that is the proprietary aspect of gpt that makes it so successful.  