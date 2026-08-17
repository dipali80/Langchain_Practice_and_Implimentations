from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
from langchain_core.runnables import RunnableParallel ,RunnableSequence , RunnableBranch ,RunnablePassthrough

load_dotenv()

prompt1 = PromptTemplate(
    template = 'Write a detailed report{topic}',
    input_variables=['topic']
)

prompt2 = PromptTemplate(
    template= 'summarize the following text',
    input_variables=['text']
)

model = ChatOpenAI()

parser = StrOutputParser()

report_gen_chain = RunnableSequence(prompt1 , model, parser)

brach_chain = RunnableBranch(
    (lambda x : len(x.split())> 500 , RunnableSequence(prompt2 , model, parser)),
    RunnablePassthrough
)

final_chain = RunnableSequence(report_gen_chain , brach_chain)

result = final_chain.invoke({'topic':'Russia vs UKraine'})

print(result)

