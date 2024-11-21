import os
from dotenv import load_dotenv, find_dotenv
_ = load_dotenv(find_dotenv())

from processes.fix_grammar import get_fix_grammar_chain
from processes.latex_equations import get_latex_word_equations_chain
from processes.percentage_and_dollars import get_percentage_and_dollars_chain
from processes.latex_math_expressions import get_latex_math_expressions_chain
from processes.remove_latex_integers import get_remove_latex_integer_chain

def create_sequential_chain():
    fix_grammar_chain = get_fix_grammar_chain()
    latex_word_equations_chain = get_latex_word_equations_chain()
    percentage_and_dollars_chain = get_percentage_and_dollars_chain()
    latex_math_expressions_chain = get_latex_math_expressions_chain()
    remove_latex_integers_chain = get_remove_latex_integer_chain()

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
    input_text = """
Okay, so we are given two rational functions, $f$ and $g$. Now, what are rational functions? Rational functions are of the form $p(x)$ upon $q(x)$, where $p(x)$ and $q(x)$ are both polynomials, and $q(x)$ is not equal to 0. So, we're given that $f(x) + g(x)$ is equal to 0, so we can rearrange this and we can just get $f(x) = -g(x)$. Now, we also have to show that if $f(x) \times g(x)$ is equal to 1, then $f(x)$ is a unit in $F$, capital $F$. So, a unit in capital $F$ basically means that for a rational function, suppose $u(x)$, there will exist another rational function, $v(x)$, such that $u(x) \times v(x)$ is equal to 1. So, we can just get $f(x)$. So, we have to find the rational function, $f(x)$, and we can just get the $u(x)$. So, what we can do is we can just apply this formula to find the $u(x)$, and that is the $u(x) \times v(x)$ is equal to 1. So, if we do that, we get $f(x) \times g(x)$ is equal to 1. And then we just do the multiplication of $u(x)$ and we can just get $f(x) \times g(x)$. So, we're given that $f(x) \times g(x)$ is equal to 1. This is basically the multiplicative inverse of $u(x)$. So, $v(x)$ is the multiplicative inverse of $u(x)$. So, what are we given with? We're given that $f(x) \times g(x)$ is equal to 1. So, from this we know that $g(x)$ is going to be the multiplicative inverse of $f(x)$. Now, in the question, it's also specified that $f(x)$ has non-zero rational functions. So, every non-zero element is going to have an inverse because if we take that function on the other side, we can divide it as long as it's non-zero because $1$ upon $0$ is non-defined. So that's why $f(x)$ is a unit in capital $F$. Okay.

Okay. Okay. Okay. Okay. Okay. Now we've done the proof part. Now we have to demonstrate that for any non-zero rational function $f(x)$ in capital $F$, there exists a unique rational function $g(x)$. Such that $f(x) \times g(x)$ is equal to 1. So, we know that both of them are, sorry, yeah, $f(x)$ and $g(x)$ are both non-zero rational functions. So, we're going to use the form of rational functions. Rational functions are of the form. So, we have $p(x)$ divided by $q(x)$ where $p(x)$ and $q(x)$ are both polynomials and $q(x)$ is not equal to 0. So, since $f(x) \times g(x)$ is equal to 1, we know that $g(x)$ is going to be the multiplicative inverse of $f(x)$. So, if $f(x)$ is equal to $p(x)$ upon $q(x)$, then we get that $g(x)$ has to be $q(x)$ divided by $p(x)$. If it's the multiplicative inverse. So, then we multiply both, so $f(x) \times g(x)$ is going to be $p(x)$ divided by $q(x)$, times $q(x)$ divided by $p(x)$. So, this just cancels out and gives us 1.

Now we also need to show the uniqueness in this proof. That there exists only one rational function that exists. That is, it's a non-zero rational function. Now, we also need to show the uniqueness in this proof. That there exists only one rational function that exists and only 1 rational function in that process. That gives us 1. It's 1, so we have to also show the uniqueness. Let's assume, so for proving uniqueness, it's very easy to... so I always assume that there are two functions that satisfy the condition and then at the end I show that both those functions are actually equal. So, this just shows the property of uniqueness. So, in this case, I'm going to suppose that there exists two rational functions, $g1(x)$ and $g2(x)$, such that $f(x) \times g1(x)$ is equal to 1 and $f(x) \times g2(x)$ is equal to 1. So, now we can try to manipulate both of these equations to somehow show that $g1(x)$ is actually equal to $g2(x)$. So, let's start with $g1(x)$. $g1(x)$ is equal to $g1(x) \times 1$. Now, why am I writing this times 1? Because I've seen in the other two equations we have a 1 in our right-hand side, so I want to use that. So, I'm going to write $g1(x)$ is equal to $g1(x) \times 1$. Now, I'm going to substitute that 1 by our second equation, that is, $f(x) \times g2(x)$. So, I get that $g1(x)$ is equal to $g1(x) \times f(x) \times g2(x)$. Now, we know that $g1(x) \times f(x)$ = 1, so this is just going to be equal to 1 \times $g2(x)$. 1 \times $g2(x)$ is going to be $g2(x)$, so we have shown that $g1(x)$ and $g2(x)$ are actually the same. So, this shows the property of uniqueness.
    """
    try:
        result = sequential_chain.invoke({"text": input_text})
        print("Final Output:", result["output"])
    except Exception as e:
        print(f"An error occurred: {e}")
