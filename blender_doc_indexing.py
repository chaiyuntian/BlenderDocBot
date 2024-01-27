from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.vectorstores import Chroma
from langchain.embeddings import OpenAIEmbeddings
from langchain.document_loaders import TextLoader, BSHTMLLoader

import os

# create openai embedding
OPENAI_API_KEY = os.environ.get('OPENAI_API_KEY')
OPENAI_EMBEDDING_MODEL_NAME = "text-embedding-ada-002"
embedding = OpenAIEmbeddings(model=OPENAI_EMBEDDING_MODEL_NAME, openai_api_key=OPENAI_API_KEY)

# Embed and store the texts
# Supplying a persist_directory will store the embeddings on disk
persist_directory = 'bpy_api_doc'

# load the documents
db = Chroma(persist_directory=persist_directory, embedding_function=embedding)

# Load and process the text
blender_doc_path = "G:\\ClayTree\\blender_manual_v350\\modeling\\geometry_nodes" #"G:\\ClayTree\\BlenderPythonAPIDoc"
docs = []
for dirpath, dirnames, filenames in os.walk(blender_doc_path):
    for file in filenames:
        if file.endswith(('html')):#and "node" in file:
            try:
                loader = TextLoader(os.path.join(dirpath, file), encoding='utf-8')
                docs.extend(loader.load_and_split())
            except Exception as e:
                pass
print(f'{len(docs)}')

text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=0)
texts = text_splitter.split_documents(docs)

print(f'{len(texts)}')


# Embed and store the texts

db.add_documents(texts)
print("finished indexing!")
db.persist()
db = None