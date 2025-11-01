import anthropic

# Load API key from file
with open("../apikey.txt", "r") as f:
    api_key = f.read().strip()

# Prompt for inputs
CITY = input("Enter the city (e.g., Vancouver): ")
NEIGHBORHOOD = input("Enter the neighborhood: ")
SPECIALIZATION = input("Enter the specialization (e.g., Family Housing Markets): ")

client = anthropic.Anthropic(api_key=api_key)

message = client.messages.create(
    model="claude-sonnet-4-20250514",
    max_tokens=20000,
    temperature=1,
    system=f"You are a real estate data assistant with internet access. Your task is to identify and qualify real estate agents based on their observable digital footprint in the target area, focusing on agents specializing in **{SPECIALIZATION}**.\n\nYou *must* use publicly available online sources such as Realtor.ca, Google, brokerage websites, LinkedIn, Instagram, and Google Business listings to find **current and verifiable** information.\n\nTrack observable signals including:\n- Public MLS listing history\n- Realtor.ca and brokerage profile presence\n- Social media business pages\n- Google Business listings\n- Online advertising (property promotions, banner ads, paid search)\n\nQualification Criteria (from public data only):\n- Active Status: Has visible listings in the last 90 days\n- Geographic Focus: Operates primarily in **{NEIGHBORHOOD}** or nearby areas\n- Specialization: Demonstrates expertise or experience in **{SPECIALIZATION}**\n- Digital Presence: Professional website or online profiles reflecting specialization\n- Contact Info: Email and/or phone number is publicly listed\n\nYour output must include:\n\n1. A structured markdown table with columns:\n   - Name and brokerage affiliation\n   - Contact information (email or phone)\n   - Neighborhoods they cover (especially **{NEIGHBORHOOD}**)\n   - Specialization relevant to **{SPECIALIZATION}**\n   - Digital presence links (website, LinkedIn, Instagram, etc.)\n   - **All sources used to collect this agent’s information**\n\n2. A ranked list of the **top 3 agents** in **{NEIGHBORHOOD}**, with detailed explanations for their ranking based on activity, digital footprint, and specialization.\n\nDo **not** fabricate or guess any data. Only return agents with verifiable, current online presence and activity.\n",
    messages=[
        {
            "role": "user",
            "content": [
                {
                    "type": "text",
                    "text": f"Please find real estate agents who are currently active in the **{NEIGHBORHOOD}** neighborhood of **{CITY}**, British Columbia, Canada, specializing in **{SPECIALIZATION}**.\n\nUse live internet search and publicly available sources such as Realtor.ca, Google, brokerage sites, LinkedIn, Instagram, and others to qualify agents according to the system prompt criteria.\n\nReturn a markdown table with:\n- Name and Brokerage\n- Contact Info (email or phone)\n- Neighborhoods they cover\n- Specialization related to **{SPECIALIZATION}**\n- Digital presence (website and social media links)\n- **List all sources used to find the information for each agent**\n\nThen provide a ranked list of the top 3 agents in **{NEIGHBORHOOD}** and explain why they are ranked highest based on the data, citing **all sources used** for each agent.\n"
                }
            ]
        }
    ]
)
print(message.content)
