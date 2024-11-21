# processes/final_touch.py

import os
from dotenv import load_dotenv, find_dotenv
_ = load_dotenv(find_dotenv())

from langchain.prompts import ChatPromptTemplate
from langchain.chat_models import ChatOpenAI  # Corrected import
from langchain_core.runnables import RunnableLambda

from parsers.result_parser import result_parser

def get_final_touch_chain():
    grammar_template_string = """
    Please perform the following tasks on the provided text:
    1. **LaTeX Conversion:**
       - Identify any mathematical expressions or variables that are not currently enclosed in LaTeX math mode (`$...$` or `$$...$$`) but should be.
       - Convert these expressions or variables by enclosing them within `$...$`.
       - **Ensure** that the conversion does not disrupt existing LaTeX expressions.
       - **Specific Symbols Handling:**
         - **Pi (π) and Theta (θ):** Replace instances of "pi" and "theta" with `\\pi` and `\\theta` respectively within math mode. For example, "pi" should become `$\\pi$` and "theta" should become `$\\theta$`.
         - **Binomial Coefficients:** Use `$\\binom{{n}}{{k}}$` for combinations. For example, "choose k from n" should become `$\\binom{{n}}{{k}}$`.
         - **Degrees Symbol:** Represent degrees using `^\\circ`. For example, "90 degrees" should become `$90^\\circ$`.
       - **Consistency:** Ensure all mathematical symbols and expressions follow standard LaTeX conventions.
    
    2. **Prevent Double Dollar Signs:**
       - **Single Dollar Signs Only:** Ensure that all LaTeX expressions are enclosed within single dollar signs (`$...$`) for inline math.
       - **Do not use double dollar signs (`$$...$$`).**
       - If any double dollar signs are found, convert them to single dollar signs.
    
    **Important:** 
    - **Rules 1 and 2 are of utmost importance.** Ensure that grammar corrections and LaTeX conversions are performed accurately without interfering with existing LaTeX formatting.
    
    **Examples:**
    - **Input:** "f(x) is equal to g2(x)."
      **Output:** "`$f(x) = g2(x)$`."
    
    - **Input:** "Solve for x in the equation 2x + 3 = 7."
      **Output:** "Solve for x in the equation `$2x + 3 = 7$`."
    
    - **Input:** "Calculate the derivative of f(x) = x^2."
      **Output:** "Calculate the derivative of `$f(x) = x^2$`."
    
    - **Input:** "A triangle has angles of 90 degrees, theta, and pi radians."
      **Output:** "A triangle has angles of `$90^\\circ$`, `$\\theta$`, and `$\\pi$` radians."
    
    - **Input:** "The number of ways to choose 3 items from 5 is given by binom{{5}}{{3}}."
      **Output:** "The number of ways to choose 3 items from 5 is given by `$\\binom{{5}}{{3}}$`."
    
    The processed text will be provided as the output without any additional formatting:
    
    {text}
    """
    
    # Create the ChatPromptTemplate with correct placeholder
    final_touch_prompt_template = ChatPromptTemplate.from_template(
        template=grammar_template_string
    )
    
    # Initialize the ChatOpenAI model with GPT-4
    chat_model = ChatOpenAI(temperature=0.0, model_name="gpt-4")
    
    # Chain the prompt and model
    final_touch_runnable = final_touch_prompt_template | chat_model | result_parser()
    # Modify the lambda to return a dict with 'output' key
    final_touch_runnable = final_touch_runnable | RunnableLambda(lambda x: {"output": x.content.strip()})
    
    return final_touch_runnable
