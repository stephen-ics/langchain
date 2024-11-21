# processes/fix_grammar.py

import os
from dotenv import load_dotenv, find_dotenv
_ = load_dotenv(find_dotenv())

from langchain.prompts import ChatPromptTemplate
from langchain.chat_models import ChatOpenAI  # Addressed in Deprecation Warnings
from langchain_core.runnables import RunnableLambda

def get_fix_grammar_chain():
    grammar_template_string = """
    Please correct any grammar or spelling errors in the following text while preserving its meaning and tone. 
    The text to be corrected will be provided in backticks as shown below:

    The following text will be in LaTeX. Do not modify or touch any content enclosed in $...$ or $$...$$, including math symbols, variables, or formatting. 
    **Do not add, remove, or alter any dollar signs ($) or their contents.**
    Only fix blatant cases of incorrect capitalization and spelling in the non-math portions of the text.

    Ensure the corrected text uses Canadian English spelling conventions. 
    Corrected text:
    ```{text}```
    """

    grammar_prompt_template = ChatPromptTemplate.from_template(template=grammar_template_string)

    chat_model = ChatOpenAI(temperature=0.0)

    # Chain the prompt and model
    fix_grammar_runnable = grammar_prompt_template | chat_model
    # Modify the lambda to return a dict with 'output' key
    fix_grammar_runnable = fix_grammar_runnable | RunnableLambda(lambda x: {"text": x.content.strip()})

    return fix_grammar_runnable
