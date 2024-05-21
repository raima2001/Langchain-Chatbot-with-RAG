from transformers import AutoModel, AutoTokenizer
import torch
from torch import Tensor
import torch.nn.functional as F
from sentence_transformers import SentenceTransformer

model_name = "models/multilingual-e5-base"
model = AutoModel.from_pretrained(model_name)
tokenizer = AutoTokenizer.from_pretrained(model_name)

def average_pool(last_hidden_states: Tensor, attention_mask: Tensor) -> Tensor:
    """
    Function to compute average pooling of hidden states based on attention mask.
    """
    last_hidden = last_hidden_states.masked_fill(~attention_mask[..., None].bool(), 0.0)
    return last_hidden.sum(dim=1) / attention_mask.sum(dim=1)[..., None]

def embed_text(texts: list) -> Tensor:
    """
    Function to embed a list of texts using the provided model and tokenizer.
    """
    
    batch_dict = tokenizer(texts, max_length=512, padding=True, truncation=True, return_tensors='pt')

    
    with torch.no_grad():
        outputs = model(**batch_dict)
    
    
    embeddings = average_pool(outputs.last_hidden_state, batch_dict['attention_mask'])

    
    embeddings = F.normalize(embeddings, p=2, dim=1)

    return embeddings
