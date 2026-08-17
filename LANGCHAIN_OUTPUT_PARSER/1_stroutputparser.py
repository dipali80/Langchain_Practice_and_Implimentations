
from langchain_huggingface import ChatHuggingFace , HuggingFaceEndpoint
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate

load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id = "TinyLlama/TinyLlama-1.1B-Chat-v1.0",
    tesk = "text-genaration"
)

model = ChatHuggingFace(llm=llm)

# 1st prompy >> deatiled repor
template1 = PromptTemplate(
    template = 'write a detail report on {topic}',
    input_variables='[topic]'
)

# 2nd prompt >> summary

template2 = PromptTemplate(
    template = 'write a 5 lines summary on the foolowing text. /n {topic}',
    input_variables='[text]'
)

prompt1 = template1.invoke({'topic':'black hole'})

result = model.invoke(prompt1)

prompt2 = template2.invoke({'text':result.content})

result1 = model.invoke(prompt2)

print(result1.content)
