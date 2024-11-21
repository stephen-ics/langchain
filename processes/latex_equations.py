import os
from dotenv import load_dotenv, find_dotenv
_ = load_dotenv(find_dotenv())

from langchain.prompts import ChatPromptTemplate
from langchain.chat_models import ChatOpenAI
from langchain_core.runnables import RunnableLambda

def get_latex_word_equations_chain():
    latex_equation_template_string = """
    Please convert word-based arithmetic operations in the following text into proper LaTeX format. 

    The following rules apply:
    1. Convert any arithmetic operations written in words (e.g., "five times five equals twenty-five") into LaTeX math mode. Examples:
       - "five times five equals twenty-five" → `$5 \\times 5 = 25$`.
       - "three plus four is seven" → `$3 + 4 = 7$`.
       - "ten divided by two is five" → `$10 \\div 2 = 5$`.
    2. Ignore any text that is too conversational or does not clearly indicate a mathematical equation. Example: "Hmm, I wonder what five times five is" should not be converted to LaTeX.
    3. Preserve the meaning of the original text as much as possible while ensuring correct LaTeX syntax.
    4. Do not modify or convert non-math-related text or context.

    The converted LaTeX-formatted text will be provided in backticks as shown below:
    ```{text}```
    """

    latex_equation_prompt_template = ChatPromptTemplate.from_template(template=latex_equation_template_string)

    chat_model = ChatOpenAI(temperature=0.0)

    latex_equations_runnable = latex_equation_prompt_template | chat_model
    latex_equations_runnable = latex_equations_runnable | RunnableLambda(lambda x: {"text": x.content.strip()})

    return latex_equations_runnable