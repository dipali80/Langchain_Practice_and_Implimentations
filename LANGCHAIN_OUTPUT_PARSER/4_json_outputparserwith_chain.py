



from langchain_huggingface import ChatHuggingFace , HuggingFaceEndpoint
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser

load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id = "TinyLlama/TinyLlama-1.1B-Chat-v1.0",
    tesk = "text-genaration"
)

model = ChatHuggingFace(llm=llm)

parser = JsonOutputParser()

tempalte = PromptTemplate(
    template = 'give me the name, age and city of a fictional person \n {foramt_instruction}',
    input_variables= [],
    partial_variables= {'foramt_instruction':parser.get_format_instructions()}
)

chain = tempalte | model | parser

result = chain.invoke({'topic':'black hole'})

print(result)
