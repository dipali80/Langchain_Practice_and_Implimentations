from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
from langchain_core.runnables import RunnableParallel ,RunnableSequence , RunnableLambda , RunnablePassthrough

load_dotenv()

def word_counter(text):
    return len(text.split())

prompt = PromptTemplate(
    template='write a joke about {topic}',
    input_variables=['topic']
)

model = ChatOpenAI()

parser = StrOutputParser()

joke_gen_chain = RunnableSequence(prompt, model , parser)

parallel_chain = RunnablePassthrough(),


parallel_chain = RunnableParallel({
    'joke' :RunnablePassthrough(),
    'Word_count': RunnableLambda(lambda x: len(x.split()))
})

final_chain = RunnableSequence(joke_gen_chain, parallel_chain)

print(final_chain.invoke({'topic':'AI'}))

