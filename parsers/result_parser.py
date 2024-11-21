from langchain_core.runnables import RunnableLambda

def result_parser():
    return RunnableLambda(lambda x: {"output": x.content.replace('`', '').strip()})
