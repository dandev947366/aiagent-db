import os

from dotenv import load_dotenv
from langchain.schema import HumanMessage, SystemMessage
from langchain_openai import ChatOpenAI

load_dotenv()

openai_key = os.getenv("API_KEY_OPENAI")
llm_name = "gpt-3.5-turbo"
model = ChatOpenAI(api_key=openai_key, model=llm_name)

messages = [
    SystemMessage(
        content="You are a helpful assistant who is extremely competent as a Computer Scientist. Your name is Rob."
    ),
    HumanMessage(content="What is a bit, and tell me your name?"),
]
# res = model.invoke(messages)
# print(res)


def first_agent(messages):
    res = model.invoke(messages)
    return res


def run_agent():
    print("Simple AI Agent: Type 'exit' to quit")
    while True:
        user_input = input("You: ")
        if user_input.lower() == "exit":
            print("Goodbye!")
            break
        print("AI agent is thinking...")
        messages = [HumanMessage(content=user_input)]
        response = first_agent(messages)
        print("Ai Agent: getting the response...")
        print(f"AI Agent: {response.content}")


if __name__ == "__main__":
    run_agent()
