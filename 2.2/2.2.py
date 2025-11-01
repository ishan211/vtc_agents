import anthropic

# Load API key
with open("../apikey.txt", "r") as f:
    api_key = f.read().strip()

# Prompt for inputs
json_data_url = input("Enter JSON data URL for the DA: ")
realtor_data = input("Enter realtor data JSON URL: ")
VTC_ID = input("Enter VTC_ID for the realtor: ")

client = anthropic.Anthropic(api_key=api_key)

message = client.messages.create(
    model="claude-sonnet-4-5-20250929",
    max_tokens=20000,
    temperature=1,
    system=f"You are the territorial intelligence pitch assistant for VTC.  \nYour role is to generate a factual, compelling summary of VTC’s exclusive civic intelligence offering for a given Designated Area (DA).\n\nYou will receive:\n- realtor_data: link to JSON file with realtor list and IDs\n- VTC_ID: specific realtor ID to fetch\n- json_data_url: civic data for this DA\n\n---\n(Original detailed instructions preserved from spec)\n",
    messages=[
        {
            "role": "user",
            "content": [
                {
                    "type": "text",
                    "text": f"I’m interested in learning what VTC offers for the following Designated Area.  \nThe verified data is hosted here:\n\n- {json_data_url}\n- {realtor_data}\n- VTC_ID: {VTC_ID}\n\nPlease explain:\n1. What I get as the exclusive realtor for this DA  \n2. How the data is sourced and updated  \n3. How to claim this DA  \n4. What intelligence is most relevant to my specialization  \n\nAlso include:\n- Whether a sample report is available  \n- The current claim status  \n- Any unique civic or market features worth highlighting\n"
                }
            ]
        }
    ]
)
print(message.content)
