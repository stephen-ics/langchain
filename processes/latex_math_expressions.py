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
    1. **Fraction Conversion**:
    - Convert any written fractions (such as "1/2," "one-half," "1 upon 2," "one over two," "1 divided by 2") into LaTeX fraction format. 
    - **Specific Cases**:
        - "1/2" or "one-half" → `$\\frac{{1}}{{2}}$`
        - "1 upon 2" or "one upon two" → `$\\frac{{1}}{{2}}$`
        - "1 over 2" or "one over two" → `$\\frac{{1}}{{2}}$`
        - "1 divided by 2" or "one divided by two" → `$\\frac{{1}}{{2}}$`
   - **General Cases**:
     - Any fraction involving two integers or expressions should be converted into LaTeX fraction format using the `\\frac{{numerator}}{{denominator}}` syntax.
   - The goal is to ensure all these variations of fractions are converted consistently to LaTeX format as `$\\frac{{numerator}}{{denominator}}$`.
    2. Convert phrases like "square root of 5" into LaTeX square root format. Example: "square root of 5" → `$\\sqrt{{5}}$`.
    3. Convert phrases like "2 squared" or "two to the power of 3" into LaTeX exponent format. Examples:
       - "2 squared" → $2^2$
       - "two to the power of 3" → $2^3$
    4. Do not modify text that does not clearly describe a mathematical expression.
    5. Preserve the meaning of the original text as much as possible while ensuring correct LaTeX syntax.

    The converted LaTeX-formatted text will be provided in backticks as shown below:
    ```{text}```
    """

    latex_math_prompt_template = ChatPromptTemplate.from_template(
        template=latex_math_template_string
    )

    chat_model = ChatOpenAI(temperature=0.0, model="gpt-4")

    latex_math_runnable = latex_math_prompt_template | chat_model
    latex_math_runnable = latex_math_runnable | RunnableLambda(lambda x: {"text": x.content.strip()})

    return latex_math_runnable