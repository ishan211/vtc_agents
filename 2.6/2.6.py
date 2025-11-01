import anthropic

# Load API key
with open("../apikey.txt", "r") as f:
    api_key = f.read().strip()

# Prompt for inputs
AGENT_NAME = input("Enter agent name: ")
DA_CODE = input("Enter DA code: ")
DA_NAME = input("Enter DA name: ")
BILLING_FREQUENCY = input("Enter billing frequency (Monthly or Annual): ")
CURRENT_PLAN = input("Enter current plan: ")
json_data_url = input("Enter JSON data URL for DA data: ")

client = anthropic.Anthropic(api_key=api_key)

message = client.messages.create(
    model="claude-sonnet-4-5-20250929",
    max_tokens=20000,
    temperature=1,
    system=f"You are the renewal and retention assistant for VTC. (Original full content preserved.)\nData located at {json_data_url}.",
    messages=[
        {
            "role": "user",
            "content": [
                {
                    "type": "text",
                    "text": f"My subscription for the following DA is expiring:\n\n- DA Code: {DA_CODE}\n- DA Name: {DA_NAME}\n- Billing Frequency: {BILLING_FREQUENCY}\n- Current Plan: {CURRENT_PLAN}\n\nPlease confirm:\n- Renewal pricing and billing date\n- How to switch from monthly to annual (or vice versa)\n- What new data or features were added\n- If I still have access to my report history\n- Whether I qualify for referral or multi-DA discounts\n\nAlso send:\n- Secure renewal/payment link\n- Steps to update payment method if needed\n"
                }
            ]
        }
    ]
)
print(message.content)
