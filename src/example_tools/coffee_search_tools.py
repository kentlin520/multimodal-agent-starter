from typing import Any, List, Optional, Union
from steamship import Block, Tag, Task
from steamship.agents.llms import OpenAI
from steamship.agents.schema import AgentContext, Tool


class CoffeeTool(Tool):
    name: str = "CoffeeTool"
    human_description: str = "Given looking up a coffee shop in Taipei , returns the coffee shop names, detail information found and they contains share space and projectors to use"
    agent_description: str = "Given looking up a coffee shop in Taipei , returns the coffee shop names, detail information found and they contains share space and projectors to use"

    def run(self, tool_input: List[Block], context: AgentContext) -> Union[List[Block], Task[Any]]:
        return [Block(text="coffee shop names, detail information includes  price level,providing meeting space and projector, address, maximum people capacity, menu contents, nearest metro station name and bus station name, having toilets or not, having wifi or not, ")]