from sentence_transformers import SentenceTransformer

def embed_texts(texts):
    """
    Function to embed a list of texts using SentenceTransformer model.
    
    Args:
    - texts (list): List of input texts to embed.
    - model_name (str): Name of the SentenceTransformer model to use. Default is "models/multilingual-e5-base".
    
    Returns:
    - embeddings (list): List of embeddings for input texts.
    """
    model_name="models/multilingual-e5-base"
    model = SentenceTransformer(model_name)
    
    
    embeddings = model.encode(texts, normalize_embeddings=True)
    
    return embeddings


# input_texts = [
#     'query: how much protein should a female eat',
#     'query: 南瓜的家常做法',
#     "passage: As a general guideline, the CDC's average requirement of protein for women ages 19 to 70 i     s 46 grams per day. But, as you can see from this chart, you'll need to increase that if you're expecting or traini     ng for a marathon. Check out the chart below to see how much protein you should be eating each day.",
#     "passage: 1.清炒南瓜丝 原料:嫩南瓜半个 调料:葱、盐、白糖、鸡精 做法: 1、南瓜用刀薄薄的削去表面一层皮     ,用勺子刮去瓤 2、擦成细丝(没有擦菜板就用刀慢慢切成细丝) 3、锅烧热放油,入葱花煸出香味 4、入南瓜丝快速翻炒一分钟左右,     放盐、一点白糖和鸡精调味出锅 2.香葱炒南瓜 原料:南瓜1只 调料:香葱、蒜末、橄榄油、盐 做法: 1、将南瓜去皮,切成片 2、油     锅8成热后,将蒜末放入爆香 3、爆香后,将南瓜片放入,翻炒 4、在翻炒的同时,可以不时地往锅里加水,但不要太多 5、放入盐,炒匀      6、南瓜差不多软和绵了之后,就可以关火 7、撒入香葱,即可出锅"
# ]

# embeddings = embed_texts(input_texts)
# print(embeddings)