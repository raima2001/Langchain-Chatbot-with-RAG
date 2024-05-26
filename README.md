# Raima Islam Application Code Challenge 💻🚀
Hello, I have incorporated the necessary changes.

Just some disclaimers: 

1) Please run the code in a virtual environment

2) in embedding.py (situated in app->routes->easy_rag->setup), Please add your own model path. Basically
add the location where your embedding model is saved locally. 

```py 
from sentence_transformers import SentenceTransformer

model_path= r"path\to\your\saved\model"   

model = SentenceTransformer(model_path)
```
To run the code using FastAPI server:

1) Go to the 'app' directory 

2) Then type, 
```bash
fastapi run main.py
```
3) Using 'http://localhost:8000/docs' you will be able to check the API endpoints.

To just test the chatbot:

1) Go to chatbot_example.py (situated in app->routes->easy_rag) and simply run the code, you will be able to interact and directly ask questions :) 

Example outputs from Chatbot!

![Screenshot 2024-05-26 230350](https://github.com/SylloTips/raima-islam-code-exercise/assets/66533777/ba2fb29d-fc9c-49a7-987b-6cd3fb83a2cf)
