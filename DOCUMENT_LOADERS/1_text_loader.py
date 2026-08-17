
# from langchain_community.document_loaders import TextLoader
# from langchain_openai import ChatOpenAI
# from lanchain_core.prompts import PromptTemplate
# from dotenv import load_dotenv
# load_dotenv()
# loader = TextLoader('dipali.txt', encoding='utf-8')


# model = ChatOpenAI()

# prompt = PromptTemplate(
#     tempalte= 'Write a summary for the following poem \n {poem}',
#     input_variables = ['poem']
# )

# parser = StroutputParser 
# docs = loader.load()

# print(docs)

# print(type(docs))

# print(docs[0].page_content)

# print(docs[0].metadata)

# chain = prompt | model | parser

# print(chain.invoke({'poem':docs[0].page_content}))

