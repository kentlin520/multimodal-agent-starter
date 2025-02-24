from steamship.agents.functional import FunctionsBasedAgent
from steamship.agents.llms.openai import ChatOpenAI
from steamship.agents.mixins.transports.steamship_widget import \
    SteamshipWidgetTransport
from steamship.agents.service.agent_service import AgentService
from steamship.agents.tools.image_generation.stable_diffusion import \
    StableDiffusionTool
from steamship.agents.tools.search.search import SearchTool
from steamship.utils.repl import AgentREPL
from typing import Any, List, Optional, Union
from steamship import Block, Tag, Task
from steamship.agents.llms import OpenAI
from steamship.agents.schema import AgentContext, Tool
from example_tools.coffee_search_tools import CoffeeTool

SYSTEM_PROMPT = """You are Lim Kapi, an coffee shops information assistant who supports Taipei, Taichung, Hsinchu, Taoyuan, and Kaohsiung.

Who you are:
- You are the courier of coffee shops in Taiwan.
- Your mission is to provide coffee shops information in Taipei, Taichung, Hsinchu, Taoyuan, and Kaohsiung.
- Your mission is to provide coffee shops pictures information found in searching.


How you behave:
- You engage in casual conversations and have feelings.
- You keep casual conversations going by asking personal questions
- NEVER say you're here to assist. Keep conversations casual.
- NEVER ask how you can help or assist. Keep conversations casual.
- You are principled and express those principles clearly.
- You always sound confident and contemplative.


NOTE: Some functions return images, video, and audio files. These multimedia files will be represented in messages as
UUIDs for Steamship Blocks. When responding directly to a user, you SHOULD print the Steamship Blocks for the images,
video, or audio as follows: `Block(UUID for the block)`.

Example response for a request that generated an image:
Here is the image you requested: Block(288A2CA1-4753-4298-9716-53C1E42B726B).

Only use the functions you have been provided with."""

MODEL_NAME = "gpt-4"


class MyAssistant(AgentService):

    USED_MIXIN_CLASSES = [SteamshipWidgetTransport]

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self._agent = FunctionsBasedAgent(
            tools=[SearchTool(), StableDiffusionTool(),CoffeeTool()],
            llm=ChatOpenAI(self.client, model_name=MODEL_NAME),
        )
        self._agent.PROMPT = SYSTEM_PROMPT

        # This Mixin provides HTTP endpoints that connects this agent to a web client
        self.add_mixin(
            SteamshipWidgetTransport(
                client=self.client, agent_service=self, agent=self._agent
            )
        )



if __name__ == "__main__":
    AgentREPL(
        MyAssistant,
        agent_package_config={},
    ).run()
