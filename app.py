import anthropic
import os

client = anthropic.Anthropic(
    # defaults to os.environ.get("ANTHROPIC_API_KEY")
    api_key=os.environ.get("ANTHROPIC_API_KEY"),
)

message = client.messages.create(
    model="claude-3-5-sonnet-20240620",
    max_tokens=1000,
    temperature=0,
    system="You are a translator",
    messages=[
        {
            "role": "user",
            "content": [
                {
                    "type": "text",
                    "text": "Translate this Hello How are you? into Urdu"
                }
            ]
        }
    ]
)
print(message.content)