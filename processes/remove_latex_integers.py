import os
from dotenv import load_dotenv, find_dotenv
_ = load_dotenv(find_dotenv())

from langchain.prompts import ChatPromptTemplate
from langchain.chat_models import ChatOpenAI
from langchain_core.runnables import RunnableLambda

def get_remove_latex_integer_chain():
    remove_integer_template_string = """
    Please process the following text to remove specific LaTeX elements according to the rules below. Ensure that all other LaTeX constructs and the overall meaning of the text remain unchanged.

    **Rules:**
    1. **Standalone LaTeX Integers**: 
       - **Definition**: A standalone LaTeX integer is a single number enclosed in LaTeX math mode (e.g., `$10$` or `$1010230123$`) that is not part of a mathematical operation.
       - **Action**: Replace such numbers by removing the `$` signs, leaving only the plain integer (e.g., `$10$` → `10`).
       - **Condition**: If the integer is part of a mathematical operation (e.g., `$1 + 0 = 1$`), leave it unchanged.

    2. **Lists of Integers in LaTeX Math Mode**:
       - **Definition**: A sequence of integers separated by commas enclosed in LaTeX math mode (e.g., `$1, 2, 3, 4, 5$`).
       - **Action**: Remove the enclosing `$` signs while keeping the integers and commas intact (e.g., `$1, 2, 3, 4, 5$` → `1, 2, 3, 4, 5`).
       - **Condition**: Only apply this action if there are no mathematical operators (such as `+`, `-`, `*`, `/`, `=`, etc.) within the math mode.

    3. **Mathematical Expressions**:
       - Do not modify any LaTeX mathematical expressions or constructs, such as:
         - `$1 + 0 = 1$`
         - `$\\sqrt{{10}}$`
         - `$\\frac{{1}}{{2}}$`
         - `$g(x) \\times 1$`
       - These should remain unchanged to preserve their mathematical meaning.

    4. **Non-LaTeX Text**:
       - Do not modify text that is not enclosed in LaTeX math mode (`$...$`).

    5. **Preservation of Structure**:
       - Maintain the original structure, spacing, and meaning of the text outside of the specified modifications.

    **Examples:**
    - **Input:** `$10$`
      **Output:** `10`

    - **Input:** `$1, 2, 3, 4$`
      **Output:** `1, 2, 3, 4`

    - **Input:** `$1 + 0 = 1$`
      **Output:** `$1 + 0 = 1$`

    - **Input:** "The sequence is $1, 2, 3, 4, 5$ and it adds up to $15$."
      **Output:** "The sequence is `1, 2, 3, 4, 5` and it adds up to `15`."

    **Text to Process**:
    ```
    {text}
    ```
    """
    remove_integer_prompt_template = ChatPromptTemplate.from_template(template=remove_integer_template_string)

    chat_model = ChatOpenAI(temperature=0.0, model="gpt-4")

    remove_integer_runnable = remove_integer_prompt_template | chat_model
    remove_integer_runnable = remove_integer_runnable | RunnableLambda(lambda x: {"text": x.content.strip()})

    return remove_integer_runnable