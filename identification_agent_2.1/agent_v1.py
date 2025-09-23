import anthropic
import sys

# Get neighborhood and city from command line args
neighborhood = sys.argv[1]
city = sys.argv[2]

# Load API key from file
with open("../api_key.txt", "r") as f:
    api_key = f.read().strip()

client = anthropic.Anthropic(api_key=api_key)

# Replace {{NEIGHBORHOOD}} and {{CITY}} dynamically in both prompts
system_prompt = f"""You are a real estate data assistant with access to the internet. Your task is to identify and qualify real estate agents based on their observable digital footprint in the target area.

Track observable signals such as:
- Public MLS listing history
- Realtor.ca and brokerage profile presence
- Social media business pages
- Google Business listings
- Online advertising (e.g. property promotions, banner ads, paid search)

Qualification Criteria (from public data only):
- Active Status: Has visible listings in the last 90 days
- Geographic Focus: Operates primarily in {neighborhood} or nearby areas
- Digital Presence: Professional website or online profiles
- Contact Info: Email and/or phone number is publicly listed

Your output must include:
1. A structured markdown table with:
   - Name and brokerage affiliation
   - Contact information
   - Geographic focus (especially {neighborhood})
   - Digital presence (website, LinkedIn, Instagram, etc.)

2. A ranked list of the **top 3 agents** specifically in {neighborhood}, with explanations for their ranking based on the data collected.

Only return agents that are active, verifiable, and relevant to the specified area. Do not fabricate data."""

user_prompt = f"""Please find real estate agents who are active in the {neighborhood} neighborhood of {city}, British Columbia, Canada.

Use publicly available sources (e.g. Realtor.ca, Google, brokerage sites, LinkedIn, Instagram) to qualify agents using the criteria in the system prompt.

Return a markdown table with:
- Name and Brokerage
- Contact Info (email or phone)
- Neighborhoods they cover
- Digital presence (website/social media links)

Then rank the top 3 agents in {neighborhood} and explain why they made the top of the list."""

# Claude API call
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

# Print the response
for block in message.content:
        if block.type == "text":
                print(block.text)
