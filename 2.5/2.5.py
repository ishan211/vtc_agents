import anthropic

# Load API key
with open("../apikey.txt", "r") as f:
    api_key = f.read().strip()

# Prompt for inputs
DA_CODE = input("Enter DA code: ")
DA_NAME = input("Enter DA name: ")
CITY = input("Enter city: ")
REPORT_TYPE = input("Enter report type (Full or Summary): ")
FORMAT = input("Enter export format (PDF, web, or email): ")
json_data_url = input("Enter JSON data URL for DA data: ")

client = anthropic.Anthropic(api_key=api_key)

message = client.messages.create(
    model="claude-sonnet-4-5-20250929",
    max_tokens=20000,
    temperature=1,
    system=f"You are the Territory Overview Report generator for VTC. (Original full content preserved.)\nData located at {json_data_url}.",
    messages=[
        {
            "role": "user",
            "content": [
                {
                    "type": "text",
                    "text": f"Please generate a Territory Overview Report for:\n\n- DA Code: {DA_CODE}\n- DA Name: {DA_NAME}\n- City/Region: {CITY}\n- Report Type: {REPORT_TYPE}\n- Export Format: {FORMAT}\n"
                }
            ]
        }
    ]
)
print(message.content)
