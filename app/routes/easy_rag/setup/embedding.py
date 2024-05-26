from sentence_transformers import SentenceTransformer

model_path= r"D:\raima-islam-code-exercise\models\multilingual-e5-base"  #When you run this from your computer, please specify your model path
model = SentenceTransformer(model_path)

def embed_texts(texts):
    
    embeddings = model.encode(texts, normalize_embeddings=True)
    
    return [embedding.tolist() for embedding in embeddings]

class MyOpenAIEmbeddings:
    def __init__(self, model):
        self.model = model

    def embed_query(self, query):
        embeddings = embed_texts([query])
        return embeddings[0]

