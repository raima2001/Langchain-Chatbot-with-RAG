# Raima Islam Application Code Challenge 💻🚀

Greetings Raima,

We extend a warm welcome to you to embark on our code challenge! Your participation promises to showcase your skills in a compelling manner.

In recent months, SylloTips has been gaining remarkable traction. Our product has piqued the interest of an ever-growing customer base, each eager to delve deeper into its functionalities.

In response to the escalating influx of inquiries regarding the inner workings of SylloTips, our funding team has taken decisive action. They have proposed the development of a straightforward chatbot, designed to address customer queries by leveraging existing content available on the SylloTips website.

Your task in this challenge is to craft a rudimentary RAG system, accessible via a FastAPI application written in Python.

## Challenge Description

The provided code furnishes a fully operational FastAPI application. Your objective is to compose the code for two routes constituting the SylloTips RAG system (`app/routes/easy_rag/easy_rag.py`). The first function, `index_website_controller`, will index the SylloTips website, while the function `rag_controller` will be invoked whenever a user interacts with the SylloTips chatbot.

In the file `app/routes/easy_rag/utils.py`, we offer you the framework of the functions you need to create and subsequently invoke from the FastAPI routes.

This chatbot should respond to user inquiries based on existing information on the SylloTips website. Whenever a retrieval step is unnecessary, the chatbot should bypass it and directly address the user's query. Furthermore, with each new prompt, the chatbot should be capable of reusing the chat history.

Here are some guidelines on how to proceed:

- Employ PineCone vector database to index and retrieve SylloTips website snippets ([www.syllotips.com](www.syllotips.com)). We have already configured a project and index on PineCone for you. Here are the credentials to access it: [credentials]. Remember, the index is configured to utilize the dot product as the method to compute similarity.
  - PINECONE_API_KEY = "049f0927-0d19-4e1b-9142-81b515f08787"
  - PINECONE_INDEX_NAME = "raima-isla-code-exercise"
- Utilize a local instance of the following sentence embedding model to compute the snippet embeddings: [link to model]. To execute the model, use the SentenceTransformer library from HuggingFace. Do not be concerned about pushing the model weights to GitHub; please use a `.gitignore` for that purpose. Remember that the default similarity method for these embeddings is cosine similarity, but the PineCone index uses the dot product. There's a workaround available to make this functional.
- Once you've indexed the website, proceed with setting up the RAG pipeline using langchain. As a large language model, you can select any OpenAI model. Feel free to use the provided API key:
  - OPENAI_API_KEY = "sk-proj-RTecz6DjaUKH5OzOyZGsT3BlbkFJoGLVOWRFUCe4vR2V0s4H"

### Additional Tips
- To simplify the task, you need not worry about streaming the chatbot responses for now. However, we expect you to utilize `async/await` methods to handle API calls efficiently.
- Feel free to consult any resources to aid you in completing the task: Medium posts, GitHub Copilot, ChatGPT, Hugging Face, etc.

## Good Luck! 🚀