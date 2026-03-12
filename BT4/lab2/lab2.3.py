import openai
from openai import OpenAI

USER_PROMPT = """
def print_fibonacci_sequence(n: int) -> None:
"""

SYSTEM_PROMPT = """You will be provided with a Python function signature.
Your task is to implement the function. Return code only.
"""

def get_code_with_instructions(code: str) -> str:
    return code + "\n# Complete this code"


if __name__ == "__main__":

    client: OpenAI = OpenAI()

    completion: openai.ChatCompletion = client.chat.completions.create(
        model="gpt-4o-mini",
        temperature=1,
        n=2,
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": get_code_with_instructions(USER_PROMPT)}
        ],
    )

    for i in range(2):

        output = completion.choices[i].message.content

        print(f"Output {i+1}:")

        try:
            suggested_code = output.split("```")[1]
            print(suggested_code)
        except IndexError:
            print(output)