import logging
from config import settings
from langchain.chains.question_answering import load_qa_chain
from langchain.llms import OpenAI
from qdrant_client import QdrantClient
from sentence_transformers import SentenceTransformer
from qdrant_client.http.models import Distance, VectorParams

# Logging System
logging.basicConfig(level=logging.INFO, format='=== %(asctime)s :: %(levelname)s :: %(message)s')

# Question Answering Chain based in OpenAI
qa_chain = load_qa_chain(llm=OpenAI(openai_api_key=settings.openai_api_key, streaming=False), chain_type="stuff", verbose=False)

# Embedding Model: It maps sentences & paragraphs to a 768 dimensional dense vector space and can be used for tasks like clustering or semantic search.
embedding_model = SentenceTransformer('sentence-transformers/all-mpnet-base-v2', device='cpu')

# QDrant Collection Name
COLLECTION_NAME = 'usc-ai_collection'

class BusinessHelper():
    def __init__(self):
        self.collection_name = COLLECTION_NAME
        self.embedding_model = embedding_model
        self.embedding_size = self.embedding_model.get_sentence_embedding_dimension()

        self.qdrant_client = QdrantClient(
                url="http://"+settings.qdrant_host+":"+str(settings.qdrant_port),
            )
        self.qdrant_client.recreate_collection(
            collection_name=self.collection_name,
            vectors_config=VectorParams(size=self.embedding_size, distance=Distance.COSINE),
        ) 

        logging.info(f"Collection {COLLECTION_NAME} is successfully created in QDrant.")
    def get_response(self, question: str):
        
        return qa_chain.run(input_documents="", question=question)
