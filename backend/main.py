from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from config import settings
from business_helper import BusinessHelper
import uvicorn

# FastAPI Application with CORS enabled
app = FastAPI(
    title="USC-AI backend API", 
    docs_url="/docs"
)
origins = [
    "http://localhost:8000",
    "http://127.0.0.1:8000",
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Query Model
class Query(BaseModel):
    query: str

# Business Helper
business = BusinessHelper()

@app.get("/")
async def root():
    return {"message": "Server UP and Running!"}

@app.post("/query")
async def query_index(input_query: Query):
    generated_response, relevant_docs = business.get_response(question=input_query.query)
    return {"response": generated_response, "relevant_docs": relevant_docs}

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", reload=True, port=8000)