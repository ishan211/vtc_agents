# VTC AI Agent System

This directory contains the AI-driven assistants (2.1–2.6) that power VTC’s territorial and realtor intelligence workflows.  
Each script uses the Anthropic Claude API via the official Python SDK and loads the API key automatically from `apikey.txt`.

---

## Directory Structure

```

vtc_agents/
│
├── apikey.txt
├── readme.md
│
├── 2.1/
│   └── 2.1.py
├── 2.2/
│   └── 2.2.py
├── 2.3/
│   └── 2.3.py
├── 2.5/
│   └── 2.5.py
└── 2.6/
└── 2.6.py

````

---

## Setup Instructions

1. **Install dependencies**
   ```bash
   pip install anthropic
````

2. **Add your API key**

   * Save your Claude API key in `apikey.txt` (the file should contain only the key on a single line).

3. **Run an agent**

   * Navigate to the desired agent folder (for example, `cd 2.1`) and run:

     ```bash
     python 2.1.py
     ```
   * The script will prompt you for variables like city name, DA code, etc.
   * Output is printed in your terminal as formatted text.

---

## Agent Overview

### 2.1 — Real Estate Agent Finder

**Purpose:**
Identifies and qualifies active real estate agents in a target area based on their digital footprint.

**Inputs Prompted:**

* City
* Neighborhood
* Specialization (e.g., Family Housing Markets)

**How it works:**
Uses live internet search through Claude’s connected model to verify public agent data from Realtor.ca, Google, LinkedIn, brokerage sites, and social media.
Filters for active, verifiable agents with recent listings.

**Output:**

* Markdown table of agents with name, contact info, neighborhoods, specialization, and source links
* Ranked top 3 agents with reasoning and citations

**Test Case Example:**

```
City: Vancouver
Neighborhood: Mount Pleasant West
Specialization: Family Housing Markets
```

**Expected Output:**
A Markdown table with 5–10 verified agents and a short ranked list explaining top choices based on listing recency and specialization.

---

### 2.2 — Territorial Intelligence Pitch Assistant

**Purpose:**
Generates a factual, data-driven pitch summary of VTC’s civic intelligence for a given Designated Area (DA).

**Inputs Prompted:**

* json_data_url (link to civic data JSON)
* realtor_data (link to VTC realtor registry JSON)
* VTC_ID (specific realtor ID)

**How it works:**
Fetches the JSON data, reads DA attributes (schools, transit, development, census, features, claim status), and creates a tailored pitch using approved messaging templates.

**Output:**

* Overview of what the realtor receives if they claim the DA
* How data is sourced and updated
* Claim status and sample report availability
* Relevance to realtor specialization

**Test Case Example:**

```
json_data_url: https://vtc.ai/data/117.json
realtor_data: https://vtc.ai/realtors.json
VTC_ID: 4589
```

**Expected Output:**
A paragraph-form pitch highlighting DA 117 (Mount Pleasant West) including school and transit summaries, current claim status (“Available”), and call to action to claim territory.

---

### 2.3 — Territory Allocation Assistant

**Purpose:**
Manages allocation of Designated Areas on a first-come, first-served basis.

**Inputs Prompted:**

* DA_CODE
* DA_NAME
* CITY
* VTC_ID
* json_data_url

**How it works:**
Reads DA data from JSON, confirms whether the DA is available or waitlisted, provides pricing and hold durations, and explains transfer and multi-DA options.

**Output:**

* Availability status and waitlist info
* Pricing breakdown (monthly and annual)
* Reservation and transfer options

**Test Case Example:**

```
DA_CODE: 117
DA_NAME: Mount Pleasant West
CITY: Vancouver
VTC_ID: 4589
json_data_url: https://vtc.ai/data/117.json
```

**Expected Output:**
A structured explanation confirming DA 117 is “Available,” with pricing details and instructions to reserve or join the waitlist.

---

### 2.5 — Territory Overview Report Generator

**Purpose:**
Generates detailed reports using verified civic and infrastructure data.

**Inputs Prompted:**

* DA_CODE
* DA_NAME
* CITY
* REPORT_TYPE (Full or Summary)
* FORMAT (PDF, web, or email)
* json_data_url

**How it works:**
Interprets verified JSON data for a DA and builds a report summarizing education, transit, development, census, and local infrastructure.
Tags all information with evidence levels (L1/L2/L3).

**Output:**

* Narrative or structured report
* Data source citations with timestamps
* Quality of Life and civic metrics

**Test Case Example:**

```
DA_CODE: 117
DA_NAME: Mount Pleasant West
CITY: Vancouver
REPORT_TYPE: Full
FORMAT: PDF
json_data_url: https://vtc.ai/data/117.json
```

**Expected Output:**
Comprehensive territory overview including school capacity (92%), development pipeline, population, median income, and unique features.

---

### 2.6 — Renewal and Retention Assistant

**Purpose:**
Manages subscription renewals and retention for existing DAs.

**Inputs Prompted:**

* AGENT_NAME
* DA_CODE
* DA_NAME
* BILLING_FREQUENCY (Monthly or Annual)
* CURRENT_PLAN
* json_data_url

**How it works:**
Confirms renewal pricing, next billing date, new data features, report access, and available incentives such as referral bonuses or multi-DA discounts.
If not renewed, offers waitlist or downgrade paths.

**Output:**

* Renewal confirmation with pricing and options
* Incentive and referral details
* Instructions for updating billing or transferring a DA

**Test Case Example:**

```
AGENT_NAME: John Lee
DA_CODE: 117
DA_NAME: Mount Pleasant West
BILLING_FREQUENCY: Monthly
CURRENT_PLAN: Basic
json_data_url: https://vtc.ai/data/117.json
```

**Expected Output:**
Response confirming renewal link, updated features, next billing date, and a note about available referral credit.

---

## Common Notes

* All data sources must be verifiable and never fabricated.
* Each agent script prompts for variables at runtime.
* The scripts print the generated message directly to the console.
* For PDF or email exports (in 2.5), integration is handled by external systems, not by these scripts.

---

## Troubleshooting

**Issue:** `anthropic.errors.AuthenticationError`
**Solution:** Verify that `apikey.txt` contains a valid API key and no extra spaces.

**Issue:** Script cannot find `apikey.txt`
**Solution:** Run the script from inside its subfolder (e.g., `cd 2.1`), ensuring the relative path `../apikey.txt` exists.

**Issue:** No output returned
**Solution:** Check that the model name in each script matches your Anthropic account access (e.g., `claude-sonnet-4-5-20250929`).

---

## Example JSON Data (for Web Hosting)

These examples can be saved and hosted as static JSON files on your domain for testing or demonstration purposes.

---

### Example 1: Civic Data for DA (used by 2.2, 2.3, 2.5, 2.6)

**File:** `https://github.com/ishan211/vtc_agents/blob/main/examples/117.json`

```json
{
  "DA_CODE": "117",
  "DA_NAME": "Mount Pleasant West",
  "CITY": "Vancouver",
  "PROVINCE": "BC",
  "POPULATION": 12845,
  "MEDIAN_INCOME": 68400,
  "SCHOOLS": {
    "elementary": 3,
    "secondary": 1,
    "post_secondary": 1,
    "school_quality_index": 0.89
  },
  "TRANSIT": {
    "stations": ["Broadway-City Hall", "Olympic Village"],
    "bus_routes": 6,
    "transit_score": 0.92
  },
  "DEVELOPMENT": {
    "active_projects": 4,
    "notable_projects": [
      {
        "name": "Cambie Corridor Phase 3",
        "developer": "City of Vancouver",
        "completion_year": 2026
      },
      {
        "name": "Westbank – Broadway Towers",
        "developer": "Westbank",
        "completion_year": 2027
      }
    ]
  },
  "REAL_ESTATE": {
    "avg_listing_price": 1275000,
    "avg_days_on_market": 19,
    "recent_sales": 43,
    "property_types": ["Condo", "Townhouse", "Detached"]
  },
  "CLAIM_STATUS": "Available",
  "UPDATED_AT": "2025-10-12T14:00:00Z"
}
```

---

### Example 2: Realtor Registry Data (used by 2.2)

**File:** `https://github.com/ishan211/vtc_agents/blob/main/examples/realtors.json`

```json
{
  "realtors": [
    {
      "VTC_ID": "4589",
      "name": "John Lee",
      "brokerage": "Sutton Group West Coast Realty",
      "email": "john.lee@sutton.com",
      "specialization": "Family Housing Markets",
      "territories_claimed": ["118", "119"]
    },
    {
      "VTC_ID": "4590",
      "name": "Sarah Chen",
      "brokerage": "RE/MAX City Realty",
      "email": "sarah.chen@remax.ca",
      "specialization": "Urban Condos",
      "territories_claimed": ["117"]
    }
  ]
}
```

---

### Example 3: Territory Availability Data (optional for 2.3 testing)

**File:** `https://github.com/ishan211/vtc_agents/blob/main/examples/territories.json`

```json
{
  "territories": [
    {
      "DA_CODE": "117",
      "name": "Mount Pleasant West",
      "city": "Vancouver",
      "status": "Available",
      "monthly_rate": 149.0,
      "annual_rate": 1490.0
    },
    {
      "DA_CODE": "118",
      "name": "Fairview Slopes",
      "city": "Vancouver",
      "status": "Waitlisted",
      "monthly_rate": 139.0,
      "annual_rate": 1390.0
    }
  ]
}
```

---

### Example 4: Renewal and Plan Data (for 2.6 testing)

**File:** `https://github.com/ishan211/vtc_agents/blob/main/examples/renewals.json`

```json
{
  "agents": [
    {
      "AGENT_NAME": "John Lee",
      "DA_CODE": "117",
      "DA_NAME": "Mount Pleasant West",
      "CURRENT_PLAN": "Basic",
      "BILLING_FREQUENCY": "Monthly",
      "RENEWAL_DATE": "2025-11-15",
      "NEXT_BILLING": "2025-12-15",
      "UPGRADE_OPTIONS": ["Pro", "Enterprise"],
      "INCENTIVES": {
        "referral_credit": 50,
        "multi_da_discount": 10
      }
    }
  ]
}
```

---

### Hosting Notes

1. Upload these `.json` files to your hosting environment (e.g., AWS S3, Cloudflare Pages, or GitHub Pages).
2. Ensure the URLs are **publicly accessible** (i.e., anyone can open them in a browser).
3. When prompted by a script (for example, `json_data_url`), paste the hosted URL (e.g. `https://github.com/ishan211/vtc_agents/blob/main/examples/117.json`).
4. Make sure your site sends `Content-Type: application/json` headers for these files.

---

### Example Test Input for 2.2 Using Hosted Data

```
json_data_url: https://github.com/ishan211/vtc_agents/blob/main/examples/117.json
realtor_data: https://github.com/ishan211/vtc_agents/blob/main/examples/realtors.json
VTC_ID: 4589
```

**Expected Output:**
Pitch text describing Mount Pleasant West, stating that John Lee (VTC_ID 4589) can claim the DA as it’s available, with data-driven details from the JSON sources.
