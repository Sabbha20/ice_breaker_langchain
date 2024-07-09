import os
from dotenv import load_dotenv

from langchain.prompts.prompt import PromptTemplate
from langchain_openai import ChatOpenAI

if __name__ == "__main__":
    load_dotenv()
    print("Hello Langchain")
    # for k, v in os.environ.items():
    #     print(f"{k}:\t {v}")
    # print("\n\n")
    print(os.environ["LS_COLORS"])