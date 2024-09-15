from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.document_loaders import DirectoryLoader
from langchain.document_loaders import PyPDFLoader
from langchain.vectorstores import Qdrant
# from langchain.embeddings import SentenceTransformerEmbeddings
from langchain_huggingface import HuggingFaceEmbeddings

embeddings = HuggingFaceEmbeddings(
    model_name="NeuML/pubmedbert-base-embeddings")

print(embeddings)

loader = DirectoryLoader('Data/', glob="**/*.pdf",
                         show_progress=True, loader_cls=PyPDFLoader)

documents = loader.load()

text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=1000,
    chunk_overlap=100
)

texts = text_splitter.split_documents(documents)

url = "http://localhost:6333/dashboard"
qdrant = Qdrant.from_documents(
    texts,
    embeddings,
    url=url,
    collection_name="vector_database"
)

print("Vector Database is Created!")
