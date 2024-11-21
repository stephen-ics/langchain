import os
from dotenv import load_dotenv, find_dotenv
_ = load_dotenv(find_dotenv())

from langchain.prompts import ChatPromptTemplate
from langchain.chat_models import ChatOpenAI
from langchain_core.runnables import RunnableLambda

def get_percentage_and_dollars_chain():
    fix_percent_and_dollar_template_string = """
    Please modify the following LaTeX text to properly format dollar amounts and percentages while preserving the rest of the text as-is.

    The following rules apply:
    1. **Dollar Amounts:**
       - Any dollar amounts (e.g., $1000) should be enclosed in LaTeX math mode and prefixed with a backslash. Example:
         - **Input:** "The cost was $1000."
         - **Output:** "The cost was $\$1000$."
    2. **Percentages:**
       - Any percentages (e.g., 50%) should be converted to LaTeX math mode with proper escaping. Example:
         - **Input:** "The discount was 50%."
         - **Output:** "The discount was $50\\%$."
    3. **Consistency in Delimitation:**
       - Ensure that every LaTeX math expression starts and ends with a single dollar sign ($).
       - **Do Not:** Leave any LaTeX expression without a closing dollar sign. Example of incorrect formatting:
         - **Incorrect Output:** "$50\\%"
       - **Correct Formatting:** "$50\\%$"
    4. **Preservation of Non-Mathematical Text:**
       - Do not make any other changes to the text, including grammar, spelling, or non-math portions.
    5. **Avoid Redundancy:**
       - Do not add multiple dollar signs or unnecessary backslashes.
    
    **Additional Examples:**
    - **Input:** "He received a bonus of $200 and a discount of 15%."
      **Output:** "He received a bonus of $\$200$ and a discount of $15\\%$."
    
    - **Input:** "The price dropped to $750 after a 25%."
      **Output:** "The price dropped to $\$750$ after a $25\\%$."
    
    The corrected text will be provided in backticks as shown below:
    ```{text}```
    """

    fixed_percent_dollar_template = ChatPromptTemplate.from_template(template=fix_percent_and_dollar_template_string)

    chat_model = ChatOpenAI(temperature=0.0, model="gpt-4")

    percent_and_dollar_chain_runnable = fixed_percent_dollar_template | chat_model
    percent_and_dollar_chain_runnable = percent_and_dollar_chain_runnable | RunnableLambda(lambda x: {"text": x.content.strip()})
    
    return percent_and_dollar_chain_runnable