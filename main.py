#pip install python-dotenv
#pip install openai-agents
from dotenv import load_dotenv
import os

load_dotenv()

from agents import Agent,Runner, AsyncOpenAI, OpenAIChatCompletionsModel, RunConfig
gemini_api_key = os.getenv("GEMINI-API-KEY")

print(gemini_api_key)
# Check if the API key is present; if not, raise an error
if not gemini_api_key:
    raise ValueError("GEMINI_API_KEY is not set. Please ensure it is defined in your .env file.")

#Reference: https://ai.google.dev/gemini-api/docs/openai
external_client = AsyncOpenAI(
    api_key=gemini_api_key,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/",
)

model = OpenAIChatCompletionsModel(
    model="gemini-2.0-flash",
    openai_client=external_client
)

config = RunConfig(
    model=model,
    model_provider=external_client,
    tracing_disabled=True
)
#translation-agent 
#urdu to english
translator = Agent(
    name = 'Translator Agent',
    instructions = """you are translator agent. Translate urdu to english""",
)
response = Runner.run_sync(
    translator,
    input = "میں نے آج ایک کتاب پڑھی۔ اس میں بہت دلچسپ کہانیاں تھیں۔"
    ,run_config =config
)

print(response.final_output)
# writer  = Agent(
#     name = 'Writer Agent',
#     instructions = """you are writer agent. Generate poem,easy ,stories etc'""",
# )
# response = Runner.run_sync(
#     writer,
#     input = "write a 2 paragraph eassy on Generative AI..."
#     ,run_config =config
#     )
# print(response.final_output)
