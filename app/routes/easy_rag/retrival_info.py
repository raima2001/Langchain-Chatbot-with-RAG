import os
from langchain_pinecone import PineconeVectorStore
from app.routes.easy_rag.pinecone_store import index 
from sentence_transformers import SentenceTransformer
from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain.chains import RetrievalQA
from langchain.memory import ConversationBufferMemory

model_name="models/multilingual-e5-base"
model = SentenceTransformer(model_name)


def embed_texts(texts):
    
    
    embeddings = model.encode(texts, normalize_embeddings=True)
    
    return [embedding.tolist() for embedding in embeddings]


os.environ["OPENAI_API_KEY"] = os.getenv("sk-proj-RTecz6DjaUKH5OzOyZGsT3BlbkFJoGLVOWRFUCe4vR2V0s4H") or "sk-proj-RTecz6DjaUKH5OzOyZGsT3BlbkFJoGLVOWRFUCe4vR2V0s4H"



llm = ChatOpenAI(  
    openai_api_key= os.environ["OPENAI_API_KEY"],  
    model_name='gpt-4o' 
    
)
template = """
Use the following context provided about Syllotips (delimited by <ctx></ctx>) and the chat history (delimited by <hs></hs>) to answer the questions from the user. If you dont have any answer just write "I don't know":
------
<ctx>
{context}
</ctx>
------
<hs>
{history}
</hs>
------
{question}
Answer:
"""
prompt = PromptTemplate(
    input_variables=["history", "context", "question"],
    template=template,
)

memory = ConversationBufferMemory(
    memory_key="history",
    input_key="question"
)



class MyOpenAIEmbeddings:
    def __init__(self, model):
        self.model = model

    def embed_query(self, query):
        embeddings = embed_texts([query])
        return embeddings[0]


embed_model = MyOpenAIEmbeddings(model)

print(embed_model)

text_field ='text'


vectorstore = PineconeVectorStore(
    index=index,
    embedding=embed_model,  
    text_key=text_field
)

qa = RetrievalQA.from_chain_type(
    llm=llm,
    chain_type='stuff',
    retriever=vectorstore.as_retriever(),
    verbose=True,
    chain_type_kwargs={
        "verbose": False,
        "prompt": prompt,
        "memory": memory,
    }
)

def initialize_qa_system():
    global qa
    if not qa:
        qa = RetrievalQA.from_chain_type(
            llm=llm,
            chain_type='stuff',
            retriever=vectorstore.as_retriever(),
            verbose=True,
            chain_type_kwargs={
                "verbose": False,
                "prompt": prompt,
                "memory": memory,
            }
        )

def ask_question(query):
    initialize_qa_system()
    response = qa.run(query)
    return response

def main():
    print("You can start asking questions. Type 'quit' to end the conversation.")
    while True:
        user_input = input("User: ")
        if user_input.lower() == "quit":
            print("Ending the conversation. Goodbye!")
            break
        
        # Run the conversation chain with user input
        response = ask_question(user_input)
        print(f"Assistant: {response}")

if __name__ == "__main__":
    main()