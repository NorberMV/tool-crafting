from chains import (
    anthropic_chain,
    langchain_chain,
    general_chain,
)


def route(info):
    if "anthropic" in info["topic"].lower():
        return anthropic_chain
    elif "langchain" in info["topic"].lower():
        return langchain_chain
    else:
        return general_chain
