# Raima Islam Application Code Challenge 💻🚀
=====================================================

Welcome to the Raima Islam Application Code Challenge! 🎉

## Challenge Description
In this challenge, you are tasked with crafting a rudimentary RAG system, accessible via a FastAPI application written in Python. The goal is to develop a straightforward chatbot that addresses customer queries by leveraging existing content available on the SylloTips website.

## Provided Code
The provided code furnishes a fully operational FastAPI application. Your objective is to compose the code for two routes constituting the SylloTips RAG system (`app/routes/easy_rag/easy_rag.py`).

## Task Objectives
### 1. Index the SylloTips website
Implement the `index_website_controller` function to index the SylloTips website.

### 2. Implement the RAG system
Implement the `rag_controller` function to respond to user inquiries based on existing information on the SylloTips website.

## Guidelines
### Indexing and Retrieval
* Employ PineCone vector database to index and retrieve SylloTips website snippets (www.syllotips.com).
* Use the provided credentials to access the PineCone project and index.

- PINECONE_API_KEY = "049f0927-0d19-4e1b-9142-81b515f08787"
- PINECONE_INDEX_NAME = "raima-isla-code-exercise"

* Utilize the dot product as the method to compute similarity.

### Sentence Embedding Model
* Use a local instance of the provided sentence embedding model to compute the snippet embeddings.
* Execute the model using the SentenceTransformer library from HuggingFace.
* Remember to use a `.gitignore` file to ignore the model weights.

### RAG Pipeline
* Set up the RAG pipeline using langchain.
* Select any OpenAI model as the large language model.
* Use the provided API key.

- OPENAI_API_KEY = "sk-proj-RTecz6DjaUKH5OzOyZGsT3BlbkFJoGLVOWRFUCe4vR2V0s4H"

### Additional Tips
* Use async/await methods to handle API calls efficiently.
* Feel free to consult any resources to aid you in completing the task, such as Medium posts, GitHub Copilot, ChatGPT, Hugging Face, etc.

## Good Luck! 🚀