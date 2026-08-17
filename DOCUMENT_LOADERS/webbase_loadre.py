
# from langchain_cummunity.document_loaders import webBaseLoader
# url = 'path of that content'
# loader = webBaseLoader(url)
# docs = loader.load()

# from langchain_community.document_loaders import TextLoader
# from langchain_openai import ChatOpenAI
# from lanchain_core.prompts import PromptTemplate 
# from dotenv import load_dotenv
# load_dotenv()
# loader = TextLoader('dipali.txt', encoding='utf-8')


# model = ChatOpenAI()

# prompt = PromptTemplate(
#     tempalte= 'Anwer the following questions \n {question} from \n {text}',
#     input_variables =['question','text']
# )

# parser = StroutputParser 

# print(len(docs))
# print(docs[0].page_content)


# #to asking the question from that 

# chain = prompt |model|parser

# chain.invoke({'wuestion': 'what is the pek brightness of this product','text':docs[0].page_content})
