
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

prompt = PromptTemplate(
    template='Genarate 5 intersting facts about {tooic}',
    input_variables=['topic']
)

model = ChatOpenAI()

parser = StrOutputParser()

chain = prompt | model | parser  # this is my pipline

result = chain.invoke({'topic':'cricket'})

print(result) # this is the simple chain example 

chain.get_graph().print_ascii() # used for the visualizing how chains are work
