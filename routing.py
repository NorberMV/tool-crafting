from langchain.schema.agent import AgentFinish
from langchain_core.messages import AIMessage

from tools import get_current_temperature


def route(result):
    if isinstance(result, AgentFinish):
        print("Not calling the tool...")
        return result.return_values["output"]
    else:
        tools = {
            "get_current_temperature": get_current_temperature,
        }
        print("Routing the call to the weather tool with the parameters:")
        print(f"{result.tool_input!r}")
        return tools[result.tool].run(result.tool_input)

def display_openai_func(message: AIMessage):
    print(f"The full object generated from querying the chain is:\n{message!r}")
    print()
    try:
        message.additional_kwargs["function_call"]
    except KeyError:
        pass
    else:
        print(f"The function call being made was: {message.additional_kwargs["function_call"]!r}")
    return message
