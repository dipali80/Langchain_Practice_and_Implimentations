

from langchain_huggingface import ChatHuggingFace , HuggingFaceEndpoint
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id = "TinyLlama/TinyLlama-1.1B-Chat-v1.0",
    tesk = "text-genaration"
)

model = ChatHuggingFace(llm=llm)

# 1st prompt >> deatiled report
template1 = PromptTemplate(
    template = 'write a detail report on {topic}',
    input_variables='[topic]'
)

# 2nd prompt >> summary

template2 = PromptTemplate(
    template = 'write a 5 lines summary on the foolowing text. /n {topic}',
    input_variables='[text]'
)

parser = StrOutputParser()

chain = template1 | model | template2 | model | parser

result = chain.invoke({'topic': 'black hole'})

print(result)  # it is becomes posible becose of parsers 
