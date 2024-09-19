from typing import Optional, Type

# Import things that are needed generically
from pydantic import BaseModel, Field
from langchain.tools import BaseTool
from langchain.callbacks.manager import (
    AsyncCallbackManagerForToolRun,
    CallbackManagerForToolRun,
)


# Define the input schema
class OpenMeteoInput(BaseModel):
    latitude: float = Field(..., description="Latitude of the location to fetch weather data for")
    longitude: float = Field(..., description="Longitude of the location to fetch weather data for")


# class CalculatorInput(BaseModel):
#     """A custom tool."""
#     num_a: int = Field(description="First number")
#     num_b: int = Field(description="Second number")
#
#
# class CalculatorTool(BaseTool):
#     """A custom calculator tool."""
#     name: str = "calculator"
#     description: str = "Useful when you need to answer questions about multiplications"
#     args_schema : Type[BaseModel] = CalculatorInput
#     return_direct : bool = True
#
#     def _run(
#             self, a: int, b: int, run_manager: Optional[CallbackManagerForToolRun] = None
#         ) -> str:
#         """Use the tool."""
#         return f"Multiplication is {a}*{b}!"
#
#     async def _arun(
#             self,
#             a: int,
#             b: int,
#             run_manager: Optional[AsyncCallbackManagerForToolRun] = None,
#         ) -> str:
#         """Use the tool asynchronously."""
#         raise NotImplementedError("Calculator does not support async")

class CalculatorTool(BaseModel):
    """Useful when you need to answer questions about multiplications, returns an integer called 'total' from the multiplication of the two given numbers."""
    num_a: int = Field(description="First number")
    num_b: int = Field(description="Second number")
    total: int = Field(description="The resulting number from the multiplication of a*b")
