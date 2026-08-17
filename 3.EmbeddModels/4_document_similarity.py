
from langchain_openai import OpenAIEmbeddings

from dotenv import load_dotenv

from sklearn.metrics.pairwise import cosine_similarity
import numpy as np 

load_dotenv()

embedding = OpenAIEmbeddings(model = "text-embedding-3-large", dimensions=300)

documents =[

    "virat kolhi is an indian criketer known for his aggressive batting and leadership."
    "MS Dhoni is a former indian captain famous for his calm demenor and finishing skills.",
    "sachin sharma is known for his elegent batting and record-breaking double centuries.",
    "Rohit sharma is known for his elegant batting and record-breaking double centuries.",
    "Jasprit bumrah is known for his unique bowling action and ability to take wickets in crucial moments."

]

query = 'tell me about virat kohali'

doc_embeddings = embedding.embed_documents(documents)
query_embedding = embedding.embed_query(query)

scores = cosine_similarity([query_embedding], doc_embeddings)[0]

print(list(enumerate(scores)))


