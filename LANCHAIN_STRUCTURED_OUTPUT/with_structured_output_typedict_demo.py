
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from typing import TypedDict

load_dotenv()

model = ChatOpenAI()

#Schema 
class Review(TypedDict):

    summary : str
    sentiment :str

structured_output = model.with_structured_output(Review)

result = structured_output(""" The hardware is grat, but the software feels bloated there are too many pre- installed apps that i cant remove also the ui outdated
campared to other brands . hoping for a software update to fix this.""")

print(result)
print(result['summary']) # this is the main use of structured output we can extract specific that we want 
print(['sentiment'])

# so if i want summary only i can exact only summary that is the flexibility we have 
