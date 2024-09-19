from langchain.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI
from langchain.agents.output_parsers import OpenAIFunctionsAgentOutputParser
from langchain_core.utils.function_calling import convert_to_openai_function

from tools_module import get_current_temperature
from routing import route


functions = [
    convert_to_openai_function(f) for f in [
        get_current_temperature
    ]
]

model = ChatOpenAI(
        model="gpt-4o",
        temperature=0,
        max_tokens=None,
        timeout=None,
        max_retries=2,
        ).bind(functions=functions)

prompt = ChatPromptTemplate.from_messages([
    ("system", "You are helpful but sassy assistant"),
    ("user", "{input}"),
])

chain = prompt | model | OpenAIFunctionsAgentOutputParser() | route


# Entry point
if __name__ == "__main__":
    print("* The name of the tool is:")
    print(get_current_temperature.name)
    print("* The tool description is:")
    print(get_current_temperature.description)
    print("* The tool arguments are:")
    print(get_current_temperature.args)
    user_question = "What is the weather in Lions Bay British Columbia Canada right now?"
    # user_question = "What is the best book on OOP for a Python programmer?"
    print(f"* And finally, the answer from the tool to the question '{user_question}' is:")

    result = chain.invoke({"input": user_question})
    print(result)

