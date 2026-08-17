
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_anthropic import ChatAnthropic
from langchain_core.runnables import RunnableParallel , RunnableBranch  , RunnableLambda# using runnable branch  it helps to like if , else

load_dotenv()

model = ChatOpenAI()

parser = StrOutputParser()

class Feedback(BaseModel): # this class we create becose our promp1 s ouput must be saty consistant bcz based on 1st output our all other chain is dependant

    sentiment : Literal['positive','negative'] = Field(descriprion ='give the sentiment of the feedback')

parser2 = PydanticOutputParser(Pydantic_object = Feedback)

prompt1 = PromptTemplate(
    template = 'clasify the sentiment the following  feedback text into possitive or negative \n {feedback} \n {format_instructions}',
    input_variables= ['feedback'],
    partial_variables={'format_instruction':parser2.get_format_instructions()}
)

from langchain_core.output_parsers import PydanticOutputParser
from pydantic import BaseModel , Field
from typing  import Literal

classifier_chain = prompt1 | model | parser2

prompt2 = PromptTemplate(
    template= 'Write an aapropriate response to this positive feedback \n {feedback}',
    input_variables=['Feedback']
)


prompt3 = PromptTemplate(
    template= 'Write an aapropriate response to this negative feedback \n {feedback}',
    input_variables=['Feedback']
)
# result =classifier_chain.invoke({'feedback':'this is a terible smartphone'}).sentiment
# print(result)


# now we crate branching 2nd part

brach_chain = RunnableBranch(
    (lambda x:x['sentiment']=='positive' , prompt2 | model | parser),
    (lambda x:x['sentiment']=='negative', prompt3 | model | parser),
    RunnableLambda(lambda x : 'could not find sentiment')
)

chain = classifier_chain | brach_chain

result = chain.invoke({'feedback':'this is a terrible phone'})

print(result)

chain.get_graph().print_ascii()