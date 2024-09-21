from langchain_core.runnables import RunnableLambda

from chains import chain
from routing import route


full_chain = {"topic": chain, "question": lambda x: x["question"]} | RunnableLambda(
    route
)


# Entry point
if __name__ == "__main__":
    # question = "how do I use Anthropic?"
    question = "how do I use LangChain?"
    print(f"Asking the question: {question!r}")
    print(full_chain.invoke({"question": question}))
