import os
from dotenv import load_dotenv, find_dotenv
_ = load_dotenv(find_dotenv())

from langchain.prompts import ChatPromptTemplate
from langchain.chat_models import ChatOpenAI
from langchain_core.runnables import RunnableLambda

def get_latex_math_expressions_chain():
    latex_math_template_string = """
    Please convert mathematical expressions in the following text into proper LaTeX format. 

    The following rules apply:
    1. Convert any fractions written as "1/2" or "1 over 2" into LaTeX fraction format. Example: "1/2" or "1 over 2" → `$\\frac{{1}}{{2}}$`.
    2. Convert phrases like "square root of 5" into LaTeX square root format. Example: "square root of 5" → `$\\sqrt{{5}}$`.
    3. Convert phrases like "2 squared" or "two to the power of 3" into LaTeX exponent format. Examples:
       - "2 squared" → `$2^2$`
       - "two to the power of 3" → `$2^3$`
    4. Do not modify text that does not clearly describe a mathematical expression.
    5. Preserve the meaning of the original text as much as possible while ensuring correct LaTeX syntax.

    The converted LaTeX-formatted text will be provided in backticks as shown below:
    ```{text}```
    """

    latex_math_prompt_template = ChatPromptTemplate.from_template(
        template=latex_math_template_string
    )

    chat_model = ChatOpenAI(temperature=0.0)

    latex_math_runnable = latex_math_prompt_template | chat_model
    latex_math_runnable = latex_math_runnable | RunnableLambda(lambda x: {"text": x.content.strip()})

    return latex_math_runnable