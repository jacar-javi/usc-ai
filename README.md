# usc-ai

The purpose of this project is to develop an AI Powered User Support Center that will be able to produce accurate answers to user questions based on ours company custom knowledge database information.

## Introduction
cd
Let's explain it with a practical example:

- An user in our company asks to our USC how to access company's VPN.

- Backend will consist of a Vector Database with all our custom information correcty indexed, so that, when we ask how to access company's VPN we will get up to 4 chunks of information about how to do it. LangChain should do the trick to implement this part.

- We will use those chunks of text to put ChatGPT in context, so that we can ask user's question directly to ChatGPT and we will get an accurate answer in a Natural Language that user can directly understand. 

By using this architecture we can take advantage of the outstanding NLP capabilities of ChatGPT to answer directly to our users questions in a practical and understandable way based in our company's internal knowledge database.

## Technology Stack

- [Docker](https://www.docker.com/)
- [Python](https://www.python.org/)
- [LangChain](https://python.langchain.com/en/latest/)
- [FastAPI](https://fastapi.tiangolo.com/)
- [Qdrant](https://qdrant.tech/)
- [OpenAI](https://openai.com/)

## Quick start

Clone the repo:

`git clone https://github.com/jacar-javi/usc-ai.git`


