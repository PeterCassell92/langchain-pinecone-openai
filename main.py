# Load environment variables
from dotenv import load_dotenv,find_dotenv
load_dotenv(find_dotenv())

from langchain.llms import OpenAI
llm = OpenAI(model_name="text-davinci-003")
llm("explain large language models in one sentence")