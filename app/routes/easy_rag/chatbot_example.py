import os
from langchain_pinecone import PineconeVectorStore
from setup.pinecone_store import index_name
from setup.embedding import model, MyOpenAIEmbeddings
from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain.chains import RetrievalQA
from langchain.memory import ConversationBufferMemory
from dotenv import load_dotenv  


load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")

llm = ChatOpenAI(
    api_key= api_key,  
    model_name='gpt-4o'    
)

template = """
You are now acting as a helpful chatbot agent for Syllotips.
Use the following context provided of Syllotips (delimited by <ctx></ctx>),
even if the context does not have the answer, try to look through other chunks 
and find proper similar chunks where the answer is situated, 
answer the questions properly, relating to the proper information of Syllotips and the chat history (delimited by <hs></hs>) to answer the questions from the user.
Don't add unnecesssary info and stick to the point but try to add all the relevant and necessary info.
If you properly give outputs from the Syllotips provided context, I will give you
20 dollars. So dont miss any information. 
If they are asking questions not related to the context of Syllotips, just say "I cannot answer this question":
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

embed_model = MyOpenAIEmbeddings(model)

vectorstore = PineconeVectorStore.from_existing_index(
    index_name=index_name,
    embedding=embed_model     
)

qa = RetrievalQA.from_chain_type(
    llm=llm,
    chain_type='stuff',
    retriever=vectorstore.as_retriever(search_type="similarity", search_kwargs={'k': 20}),
    verbose=False,
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
                "verbose": True,
                "prompt": prompt,
                "memory": memory,
            }
        )

def ask_question(query):
    initialize_qa_system()
    response = qa.invoke(query)
    return response

#Try the User Input Chatbot

def main():
    print("You can start asking questions. Type 'quit' to end the conversation.")
    while True:
        user_input = input("User: ")
        if user_input.lower() == "quit":
            print("Ending the conversation. Goodbye!")
            break
        
        response = ask_question(user_input)
        print(f"Assistant: {response.get('result')}")

if __name__ == "__main__":
    main()