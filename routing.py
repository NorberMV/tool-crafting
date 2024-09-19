from langchain.schema.agent import AgentFinish

from tools_module import get_current_temperature


def route(result):
    if isinstance(result, AgentFinish):
        return result.return_values["output"]
    else:
        tools = {
            "get_current_temperature": get_current_temperature,
        }
        print("Actually calling the weather tool...")
        return tools[result.tool].run(result.tool_input)
