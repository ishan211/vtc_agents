import anthropic

# Load API key
with open("../apikey.txt", "r") as f:
    api_key = f.read().strip()

# Prompt for inputs
DA_CODE = input("Enter DA code: ")
DA_NAME = input("Enter DA name: ")
CITY = input("Enter city: ")
VTC_ID = input("Enter VTC_ID for the realtor: ")
json_data_url = input("Enter JSON data URL for DA data: ")

client = anthropic.Anthropic(api_key=api_key)

message = client.messages.create(
    model="claude-sonnet-4-5-20250929",
    max_tokens=20000,
    temperature=1,
    system=f"You are the territory allocation assistant for VTC. (Original full instructions preserved.)\nData is located here {json_data_url}.",
    messages=[
        {
            "role": "user",
            "content": [
                {
                    "type": "text",
                    "text": f"I’d like to claim a Designated Area. Here are the details:\n\n- DA Code: {DA_CODE}\n- DA Name: {DA_NAME}\n- City/Region: {CITY}\n- My Information: {VTC_ID}\n\nPlease confirm:\n- If it’s currently available\n- My position on the waitlist (if applicable)\n- Monthly and annual pricing\n- How I can reserve it today\n- Whether multi-DA packages are available\n- If there's a transfer option if I later switch areas\n"
                }
            ]
        }
    ]
)
print(message.content)
