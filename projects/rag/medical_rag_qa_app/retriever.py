from langchain.vectorstores import Qdrant
# from langchain.embeddings import SentenceTransformerEmbeddings
from langchain_huggingface import HuggingFaceEmbeddings
from qdrant_client import QdrantClient

embeddings = HuggingFaceEmbeddings(
    model_name="NeuML/pubmedbert-base-embeddings")

url = "http://localhost:6333/dashboard"

client = QdrantClient(
    url=url,
    prefer_grpc=False
)

print(client)

db = Qdrant(client=client, embeddings=embeddings,
            collection_name="vector_database")
print(db)
print("##############")

query = "What is Metastatic disease?"

docs = db.similarity_search_with_score(query=query, k=2)

for i in docs:
    doc, score = i
    print("Score:", score, "Content:",
          doc.page_content, "metadata:", doc.metadata)

