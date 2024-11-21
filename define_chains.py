import os
from dotenv import load_dotenv, find_dotenv
_ = load_dotenv(find_dotenv())

from langchain.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser

# Import your updated custom chain functions
from processes.fix_grammar import get_fix_grammar_chain
from processes.latex_equations import get_latex_word_equations_chain
from processes.percentage_and_dollars import get_percentage_and_dollars_chain
from processes.latex_math_expressions import get_latex_math_expressions_chain
from processes.remove_latex_integers import get_remove_latex_integer_chain

def create_sequential_chain():
    # Initialize each individual chain (Runnables)
    fix_grammar_chain = get_fix_grammar_chain()  # Expects 'text', outputs 'output'
    latex_word_equations_chain = get_latex_word_equations_chain()  # Expects 'output', outputs 'output'
    percentage_and_dollars_chain = get_percentage_and_dollars_chain()  # Expects 'output', outputs 'output'
    latex_math_expressions_chain = get_latex_math_expressions_chain()  # Expects 'output', outputs 'output'
    remove_latex_integers_chain = get_remove_latex_integer_chain()  # Expects 'output', outputs 'output'

    # Chain them using the pipe operator
    sequential_chain = (
        fix_grammar_chain
        | latex_word_equations_chain
        | percentage_and_dollars_chain
        | latex_math_expressions_chain
        | remove_latex_integers_chain
    )

    return sequential_chain

if __name__ == "__main__":
    sequential_chain = create_sequential_chain()
    # Example usage:
    input_text = "Your input text here."
    result = sequential_chain.invoke({"text": input_text})
    print(result["output"])
