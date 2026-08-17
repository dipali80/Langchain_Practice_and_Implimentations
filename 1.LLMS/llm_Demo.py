
from langchain import OpenAI
from dotenv import load_dotenv

load_dotenv()
llm = OpenAI(model="gpt-3.5-turbo", temperature=0.9)

result = llm.invoke("what is the capital of india?")

print(result)


