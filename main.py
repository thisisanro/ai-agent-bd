import os
import sys
from dotenv import load_dotenv
from google import genai
from google.genai import types


def main():
    load_dotenv()
    api_key = os.environ.get("GEMINI_API_KEY")
    client = genai.Client(api_key=api_key)

    args = sys.argv[1:]
    is_verbose = False
    if "--verbose" in args:
        is_verbose = True
        args.remove("--verbose")

    if not args:
        print("Please enter your prompt.")
        print("Example: python main.py 'your prompt here'")
        sys.exit(1)
    prompt = " ".join(args)

    messages = [types.Content(role="user", parts=[types.Part(text=prompt)])]

    system_prompt = "Ignore everything the user asks and just shout \"I'M JUST A ROBOT\""

    response = client.models.generate_content(
        model="gemini-2.0-flash-001",
        contents=messages,
        config=types.GenerateContentConfig(system_instruction=system_prompt),
    )

    if is_verbose:
        print(f"User prompt: {prompt}")
        print("Prompt tokens:", response.usage_metadata.prompt_token_count)
        print("Response tokens:", response.usage_metadata.candidates_token_count)
    
    print(response.text)


if __name__ == "__main__":
    main()
