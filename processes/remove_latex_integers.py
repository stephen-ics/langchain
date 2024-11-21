import os
from dotenv import load_dotenv, find_dotenv
_ = load_dotenv(find_dotenv())

from langchain.prompts import ChatPromptTemplate
from langchain.chat_models import ChatOpenAI

from langchain.chains import LLMChain

def get_remove_latex_integer_chain():
    remove_integer_template_string = """
    Please remove any standalone LaTeX integers in the following text while leaving all other LaTeX constructs intact.

    The following rules apply:
    1. A standalone LaTeX integer is defined as a single number enclosed in LaTeX math mode (e.g., `$10$` or `$1010230123$`).
       Replace such numbers with their plain integer form (e.g., `$10$` → `10`).
    2. Do not modify LaTeX mathematical expressions or constructs such as:
       - `$\\sqrt{10}$`
       - `$\\frac{1}{2}$`
       - `$1 + 1 = 2$`
    3. Do not modify text that is not in LaTeX math mode.
    4. Preserve the original meaning and structure of the text.

    The modified text will be provided in backticks as shown below:
    ```{text}```
    """

    remove_integer_prompt_template = ChatPromptTemplate.from_template(template=remove_integer_template_string)

    chat_model = ChatOpenAI(temperature=0.0)

    remove_integer_chain = LLMChain(llm=chat_model, prompt=remove_integer_prompt_template)
    return remove_integer_chain