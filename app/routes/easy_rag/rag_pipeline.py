import os
from langchain_pinecone import PineconeVectorStore
from app.routes.easy_rag.setup.pinecone_store import index_name
from app.routes.easy_rag.setup.embedding import model, MyOpenAIEmbeddings
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
answer the questions properly, try to extract all relevant info and use the chat history (delimited by <hs></hs>) to answer the questions from the user.
Don't add unnecesssary info and stick to the point but try to add relevant and necessary info.
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

