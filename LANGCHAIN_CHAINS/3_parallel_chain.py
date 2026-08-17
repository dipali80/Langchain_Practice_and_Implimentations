

from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_anthropic import ChatAnthropic

load_dotenv()


model1 = ChatOpenAI()
model2 = ChatAnthropic(model_name='claued-3')

# designing the prompts 

prompt1 = PromptTemplate(
    template = 'Ganarate short and simple notes from the topic \n{text}',
    input_variables=['text']
)

prompt2 = PromptTemplate(
    template= 'Ganarate 5 short question answers from the following text\n {text}',
    input_variables=['text']

)


# now we are going to merge the two template to get the desired output


prompt3 = PromptTemplate(
    template= 'Merge the provided notes and quiz into a single document \n {notes} and {quiz}',
    input_variables=['notes', 'quiz']   
)

parser = StrOutputParser()

# to creatt parallel langchain we need 1 thing that is ===(runableparellel) using this we can run multiple chains parlely 
from langchain_core.runnables import RunnableParallel

parellel_chain = RunnableParallel({
    'notes': prompt1 |model1 | parser ,  # this is the chain we gived name as a notes 
    'quiz': prompt2 |model2 |parser  #  this is the chain 2 we merging both of them 
})

# logic of murge 

merge_chain = prompt3 | model1 | parser

# now including final chain + merge chain we going to creat final chain

chain = parellel_chain |merge_chain 

text = 'Support Vector Machine (SVM) is a supervised machine learning algorithm mainly used for classification tasks, though it can also be applied to regression problems. The core idea of SVM is to find the best' 
' possible boundary, called a hyperplane, that separates data points of different classes. What makes SVM unique is that it does not just separate the classes but does so by maximizing the margin, which is the dis'
'tance between the closest data points of each class and the decision boundary. These closest points are known as support vectors, and they play a crucial role in defining the position of the hyperplane. SVM can ha'
'ndle both linearly separable data and non-linear data by using a technique called the kernel trick, which transforms the data into a higher-dimensional space where it becomes easier to separate. It is especially ef'
'fective in high-dimensional spaces, such as text classification problems, where data is converted into numerical form using techniques like TF-IDF. Despite its strong performance, SVM can be computationally expensive'
' for very large datasets and requires careful tuning of parameters like the kernel type and regularization factor.'

result = chain.invoke({'text':text})

print(result)

# now visulixe chain to just see

chain.get_graph().print_ascii()







