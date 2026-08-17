

from langchain_openai import OpenAiEmbeddings
from dotenv import load_dotenv

load_dotenv()

embeddings = OpenAiEmbeddings(model="text-embedding-3-large", dimensions=32) # how much dimensions you want from the output of the embedding model

documents = [

    "delhi is the capital of india",
    "kolkata is the capital of west bengol",
    "paris is the capital of france"
]

result = embeddings.embed_documents(documents)

print(str(result))

