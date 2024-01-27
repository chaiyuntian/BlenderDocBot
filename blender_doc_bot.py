from langchain.vectorstores import Chroma
from langchain.embeddings import OpenAIEmbeddings
from langchain.chat_models import ChatOpenAI
from langchain.chains import ConversationalRetrievalChain
import gradio as gr
import os

# create openai embedding
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
OPENAI_EMBEDDING_MODEL_NAME = "text-embedding-ada-002"
embedding = OpenAIEmbeddings(model=OPENAI_EMBEDDING_MODEL_NAME, openai_api_key=OPENAI_API_KEY)

# Embed and store the texts
persist_directory = 'bpy_api_doc'

# load the documents
db = Chroma(persist_directory=persist_directory, embedding_function=embedding)

retriever = db.as_retriever()

retriever.search_kwargs['distance_metric'] = 'cos'
retriever.search_kwargs['fetch_k'] = 150
retriever.search_kwargs['maximal_marginal_relevance'] = True
retriever.search_kwargs['k'] = 20

model = ChatOpenAI(model='gpt-3.5-turbo') # TODO: switch to 'gpt-4'
qa = ConversationalRetrievalChain.from_llm(model, retriever=retriever)

chat_history = []

def ask_question(question):
    global chat_history
    result = qa({"question": question, "chat_history": chat_history})
    chat_history.append((question, result['answer']))
    return result['answer']

iface = gr.Interface(fn=ask_question, inputs="text", outputs="text", examples=[["What does GeometryNodeInputMaterialIndex do?"]])
iface.launch()
