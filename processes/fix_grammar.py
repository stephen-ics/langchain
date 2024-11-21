import os
from dotenv import load_dotenv, find_dotenv
_ = load_dotenv(find_dotenv())

from langchain.prompts import ChatPromptTemplate
from langchain.chat_models import ChatOpenAI

from langchain.chains import LLMChain

def get_fix_grammar_chain(latex):
    grammar_template_string = """
    Please correct any grammar or spelling errors in the following text while preserving its meaning and tone. 
    The text to be corrected will be provided in backticks as shown below:

    The following text will be in LaTeX. Do not modify or touch any content enclosed in `$...$` or `$$...$$`, including math symbols, variables, or formatting. 
    **Do not add, remove, or alter any dollar signs ($) or their contents.**
    Only fix blatant cases of incorrect capitalization and spelling in the non-math portions of the text.

    Ensure the corrected text uses Canadian English spelling conventions. 
    Corrected text:
    ```{text}```
    """

    grammar_prompt_template = ChatPromptTemplate.from_template(template=grammar_template_string)

    # Define the language model
    chat_model = ChatOpenAI(temperature=0.0)

    # Create and return the chain
    grammar_chain = LLMChain(llm=chat_model, prompt=grammar_prompt_template)
    
    return grammar_chain