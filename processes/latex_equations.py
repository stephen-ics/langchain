import os
from dotenv import load_dotenv, find_dotenv
from langchain.prompts import ChatPromptTemplate
from langchain.chat_models import ChatOpenAI
from langchain_core.runnables import RunnableLambda

# Load environment variables from .env file
_ = load_dotenv(find_dotenv())

def get_latex_word_equations_chain():
    latex_equation_template_string = """
    Please convert all word-based arithmetic operations and algebraic equations in the following text into proper LaTeX format. 
    
    **The following rules apply:**
    
    **1. Arithmetic Operations:**
       - Convert word-based arithmetic operations like "five times five equals twenty-five" into a single LaTeX math mode expression. 
         **Examples:**
           - "five times five equals twenty-five" → `$5 \\times 5 = 25$`.
           - "three plus four is seven" → `$3 + 4 = 7$`.
           - "ten divided by two is five" → `$10 \\div 2 = 5$`.
    
    **2. Algebraic Equations and Expressions:**
       - Treat all algebraic equations and expressions as single mathematical entities. 
         **Examples:**
           - "g1(x) is equal to g1(x) times 1" → `$g1(x) = g1(x) \\times 1$`.
           - "f(x) times g1(x) is equal to 1 and f(x) times g2(x) is equal to 1" → $f(x) \\times g1(x) = 1 and f(x) \\times g2(x) = 1$.
           - "p(x) divided by q(x)" → `$\\frac{{{{p(x)}}}}{{{{q(x)}}}}$`.
       - **Ensure** that any instance of "is equal to" or similar phrasing results in a single equation connected by `=` in LaTeX.
    
    **3. Preservation of Non-Mathematical Text:**
       - Do not modify or convert any text that does not describe mathematical operations or expressions. Ensure all non-math text remains as-is.
    
    **4. Proper Delimitation:**
       - Ensure that all converted LaTeX expressions are fully enclosed within `$...$` for inline math and do not leave trailing or missing `$` characters. 
       - Combine any related expressions (e.g., involving "and") into a single LaTeX expression where applicable.
    
    **Examples:**
    - **Input:** "Five times five equals twenty-five."
      **Output:** "$5 \\times 5 = 25$."
      
    - **Input:** "g1(x) is equal to g1(x) times 1."
      **Output:** "$g1(x) = g1(x) \\times 1$."
    
    - **Input:** "f(x) times g1(x) is equal to 1 and f(x) times g2(x) is equal to 1."
      **Output:** "$f(x) \\times g1(x)$ and $f(x) \\times g2(x) = 1$."
    
    The converted LaTeX-formatted text will be provided as the output without any additional formatting:
    
    {text}
    """
    
    # Create the prompt template
    latex_equation_prompt_template = ChatPromptTemplate.from_template(template=latex_equation_template_string)

    # Initialize the chat model
    chat_model = ChatOpenAI(model="gpt-4", temperature=0.0)  # Change to "gpt-4-32k" if you have access

    # Create the runnable chain
    latex_equation_runnable = latex_equation_prompt_template | chat_model
    latex_equation_runnable = latex_equation_runnable | RunnableLambda(lambda x: {"text": x.content.strip()})

    return latex_equation_runnable
