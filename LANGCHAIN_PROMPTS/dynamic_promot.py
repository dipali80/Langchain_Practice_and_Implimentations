
from langchain_openai import ChatOpenAI , PromptTemplate
from dotenv import load_dotenv
import streamlit as st
model = ChatOpenAI()
load_dotenv()

st.header('research tool')

paper_input = st.selectbox("select research paper name" , ["select..", "Attension  is all you need", "BERT: Pre-training of deep bidirectional transformers",
"GPT-3 Language Models are few-shot learners", "defusion models beat GANs on image synthesis"])

style_input = st.selectbox("select explanation style",["beginner-friendly", "technical",
"code-orianted", "Mathematical"])

length_input = st.selectbox("select explanation length", ["short(1-2 paragraphs)", "Medium(3-5 paragraph)",
"long(detail explanation)"])

# template 

template = PromptTemplate(
    template ="""
plese summarise the research paper titled "{paper_input}" with the folowing specification:
explaination style :{style_input}
explaination lenght: {lenght_input}
1. Mathematical Details:
-Including relevant mathematical equations if present in the paper.
-Explain the mathematical concept using simple, intutive code snippest where applicable

2. Analogies:
-Using relatable analogies to specify complex ideas.
If certain information is not available insted of guessing.
Ensure the summary is clere, accurate and aligned with the provided style and lenghth .
""",
input_variables = ['paper_input', 'style_input', 'lenghth_input']
)

# fill the placeholders

prompt = template.invoke({
    'paper_input':paper_input,
    'style_input':style_input,
    'lenghth_input': length_input

})


if st.button("Summarzei"):
    st.write("Hello")
    result = model.invoke(prompt)
    st.write(result.content)

    
# we provide the options to users , insted of direct given full acces to ask the system 
# like 1 . select wich resesrch papers summary you want 
# 2. select the style in wich you wnat ex = in detail, or overview
# 3. select the lenght of the summmrizaton in 2-3 lines or 5-10 line 
# this is called the Dynamic prompts and its very usefull     