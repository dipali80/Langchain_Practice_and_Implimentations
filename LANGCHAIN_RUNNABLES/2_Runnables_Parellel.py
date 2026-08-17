

from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
from langchain_core.runnables import RunnableParallel ,RunnableSequence

load_dotenv()

prompt1 = PromptTemplate(
    template='genarate a tweet about {topic}',
    input_variables=['topic']
)

prompt2 = PromptTemplate(
    template='Genarate a Linkdin post about {topic}',
    input_variables= ['topic']
)

model = ChatOpenAI()

parser = StrOutputParser()

parellel_chain = RunnableParallel({
    'tweest' :RunnableSequence(prompt1 , model, parser),
    'linkdin' :RunnableSequence(prompt2, model, parser)

})

result = parellel_chain.invoke({'topic':'AI'})
print(result)

