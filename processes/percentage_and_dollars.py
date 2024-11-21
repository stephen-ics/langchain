import os
from dotenv import load_dotenv, find_dotenv
_ = load_dotenv(find_dotenv())

from langchain.prompts import ChatPromptTemplate
from langchain.chat_models import ChatOpenAI

from langchain.chains import LLMChain

def get_percentage_and_dollars_chain():
    fix_percent_and_dollar_template_string = """
    Please modify the following LaTeX text to properly format dollar amounts and percentages while preserving the rest of the text as-is. 

    The following rules apply:
    1. Any dollar amounts (e.g., `$1000`) should be enclosed in LaTeX math mode and prefixed with a backslash, as `$\\$1000$`.
    2. Any percentages (e.g., `50%`) should be converted to LaTeX math mode as `$50\\%$`.
    3. Do not make any other changes to the text, including grammar, spelling, or non-math portions.

    The corrected text will be provided in backticks as shown below:
    ```{text}```
    """

    grammar_prompt_template = ChatPromptTemplate.from_template(template=fix_percent_and_dollar_template_string)

    # Define the language model
    chat_model = ChatOpenAI(temperature=0.0)

    # Create and return the chain
    percent_and_dollar_chain = LLMChain(llm=chat_model, prompt=grammar_prompt_template)
    
    return percent_and_dollar_chain