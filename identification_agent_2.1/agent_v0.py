import anthropic
import sys
import os

# --- Handle command line arguments ---
if len(sys.argv) != 3:
    print("Usage: python3 agent.py <NEIGHBORHOOD> <CITY>")
    sys.exit(1)

neighborhood = sys.argv[1]
city = sys.argv[2]

# --- Load API key from file ---
api_key_path = os.path.join(os.path.dirname(__file__), "../api_key.txt")
with open(api_key_path, "r") as f:
    api_key = f.read().strip()

# --- Initialize Claude client ---
client = anthropic.Anthropic(api_key=api_key)

# --- Prompts ---
system_prompt = (
    "You are a real estate data assistant with access to the internet. "
    "Your task is to find real estate agents who have been active in a specific neighborhood and city. "
    "Use public sources such as Realtor.com, Zillow, Redfin, or Google Search to gather accurate, up-to-date data. "
    "Output your results in a clean, easy-to-read markdown table.\n\n"
    "Focus on:\n"
    "- Name of the real estate agent or team\n"
    "- Their official website URL\n"
    "- Number of listings they’ve had in the past 12 months\n"
    "- Number of listings they’ve had specifically in the target neighborhood in the past 12 months\n\n"
    "Only return results that are relevant and accurate. If data isn't available, note that transparently in the output."
)

user_prompt = (
    f"Search for top real estate agents in the {neighborhood} neighborhood of {city}, British Columbia, Canada.\n\n"
    "Return a markdown table that includes:\n"
    "- Agent Name\n"
    "- Website URL\n"
    "- Listings in the past 12 months\n"
    f"- Listings in {neighborhood} in the past 12 months\n\n"
    "If listing data is not directly available, estimate based on available data and mention sources."
)

# --- Send message to Claude ---
message = client.messages.create(
    model="claude-sonnet-4-20250514",
    max_tokens=20000,
    temperature=1,
    system=system_prompt,
    messages=[
        {
            "role": "user",
            "content": [
                {
                    "type": "text",
                    "text": user_prompt
                }
            ]
        }
    ]
)

# --- Print Claude's response ---
print("\nIdentification Agent Output:\n")
for block in message.content:
	if block.type == "text":
		print(block.text)
