
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.messages import SystemMessage , HumanMessage

chat_template = ChatPromptTemplate([
    SystemMessage(content = 'you are helpful {domain} expert'),
    HumanMessage(content = 'Explain in simple termes , what is {topic}')
])

prompt = chat_template.invoke({'domain': 'cricket': 'topic' : 'Dusra'})

print(prompt)
