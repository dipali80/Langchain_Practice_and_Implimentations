
from langchain_openai import OpenAiEmbeddings
from dotenv import load_dotenv

load_dotenv()

embeddings = OpenAiEmbeddings(model="text-embedding-3-large", dimensions=32) # how much dimensions you want from the output of the embedding model

result = embeddings.embed_query("Delhi is the capital of india")

print(str(result))



