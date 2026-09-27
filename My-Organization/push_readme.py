import os
import json
import base64
from urllib.request import Request, urlopen
from urllib.error import HTTPError

# 1. Fetch token securely from Termux Environment Variables
GITHUB_TOKEN = os.environ.get("GITHUB_TOKEN")

if not GITHUB_TOKEN:
    print("❌ Error: GITHUB_TOKEN variable is missing!")
    print("Please run: export GITHUB_TOKEN='my_token' in Termux first.")
    exit(1)

# 2. Configuration Parameters
REPO_NAME = "AnticipatedD/galaxium-travels"
FILE_PATH = "My-Organization/README.md"
COMMIT_MESSAGE = "docs: initialize organization Bobalytics metrics dashboard"

# 3. Markdown Content Dashboard
MARKDOWN_CONTENT = """# Bobalytics: Metrics

> **Data is refreshed every 60 minutes.** All times are in UTC.
> **Scope:** Team (`ibm-hackathon-lablab`) | **Target Org:** `ibm-coding-challenge-uat (us-east)`
> **Timeline:** Last 30 days · Weekends included

---

## 📊 Core Performance Metrics

### 🤖 1. Bob Factor
* **Current Value:** `1%`
* **Volume:** **274,484** out of **20,696,293** total lines of code.
* **Trend:** 📈 +100%

### 🪙 2. Bobcoin Spend
* **Current Spend:** `21.28K BC` (5% of overall budget)
* **Budget Health:** **21,279.6 BC** spent / **400,000 BC** period budget
* **Remaining Balance:** **378,720.4 BC** remaining
* **Trend:** 📈 +100%

### 👥 3. Adoption Rate
* **Team Adoption:** `0%` 
* **Personal Progress:** `0%` (Pending workspace setup / active initialization)
* **Usage Footprint:** **41** of **10,000** active tokens on a typical day.
* **Status:** 0 frequent users, 10,000 occasional & inactive users.

---

## 📈 Activity & Spend Volume Trends

### Daily Commits & Spend Surge (Through 2026-09-27)
```text
  12000 ┼                                                  ╭─╮
  10000 ┤                                                 ╱   ╲
   8000 ┤                                                ╱     ╲
   6000 ┤                                               ╱       ╲
   4000 ┤                                              ╱         ╲
   2000 ┤                                            ╭─┘          ╲
      0 ┼────────────────────────────────────────────┴─────────────┴─
        2026-08-30      2026-09-08      2026-09-17      2026-09-27
```

---

## 🗃️ Supporting Metrics & Repository Impact

### 💳 Repositories by Bobcoin Spend

| Repository | Bob Lines | User Lines | Total Lines | Bob Factor | Bob Commits | Bobcoin Spend |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **playground** | 0 | 0 | 0 | 0.0% | 0 | **470.4 BC** |
| **DareDevilLuc/scrum-up** | 4,834 | 19,151 | 23,985 | 20.1% | 20 | **228.9 BC** |
| **IBM BOB** | 0 | 0 | 0 | 0.0% | 0 | **198.5 BC** |
| **IBM** | 0 | 0 | 0 | 0.0% | 0 | **195.2 BC** |
| **bob_sessions** | 0 | 0 | 0 | 0.0% | 0 | **128.3 BC** |
| **ibm** | 0 | 0 | 0 | 0.0% | 0 | **121.9 BC** |
| **aditya-padmar/FlakeGuard** | 7 | 35,730 | 35,737 | 0.0% | 1 | **112.0 BC** |
| **blacksheep-afk/vesper** | 1,211 | 15,379 | 16,790 | 7.2% | 9 | **103.2 BC** |
| **Cwjee/Echo** | 649 | 9,935 | 10,584 | 6.1% | 12 | **96.9 BC** |
| **project-xeroo/log-pilot** | 1,243 | 31,569 | 32,812 | 3.8% | 5 | **96.8 BC** |

### 🛠️ Bob's Contribution Impact

| Repository | Bob Lines | User Lines | Total Lines | Bob Factor | Bob Commits |
| :--- | :---: | :---: | :---: | :---: | :---: |
| **Tushar01/Necro-Code-Archaeology** | 3,316 | 0 | 3,316 | 100.0% | 1 |
| **gabrielantonyxavier/fine-print** | 1,651 | 0 | 1,651 | 100.0% | 1 |
| **bhargav-mohan/SkillSearch** | 1,423 | 0 | 1,423 | 100.0% | 1 |
| **bernardjayzo/LFworkIBMBOB** | 1,019 | 0 | 1,019 | 100.0% | 1 |
| **Modales/ibm-bob-2.0-hackathon** | 584 | 0 | 584 | 100.0% | 1 |
| **lokeshk-rookie/ChroniQ** | 309 | 0 | 309 | 100.0% | 1 |
| **Tawfiq247/tawfiq247_ecosystem-orchestrator** | 253 | 0 | 253 | 100.0% | 1 |
| **rrcf-foundation/RRCF** | 14 | 0 | 14 | 100.0% | 5 |
| **AbdullahKhetran/TicketSeed** | 2 | 0 | 2 | 100.0% | 1 |
| **sankalp-tripathi12/RootTrace-Evidence-Driven...** | 1 | 0 | 1 | 100.0% | 1 |

---

## 🏦 Subscription Profile & Allocations

* **Account Holder:** `MD ABUL HOSSAIN`
* **Assigned Role:** User
* **Assigned Plan:** Enterprise
* **Deployment Region:** United States (East)

### 🎫 Team Allocation Inventory
* **Team Profile:** `ibm-hackathon-lablab`
* **Personal Allocation Balance:** 🪙 **40 Bobcoins**
* **Active Allocation Usage:** 🪙 **0 Bobcoins**
* **Remaining Initial Balance:** 🪙 **40 Bobcoins**
"""

# 4. API Request Config Setup
api_url = f"https://github.com{REPO_NAME}/contents/{FILE_PATH}"
headers = {
    "Authorization": f"token {GITHUB_TOKEN}",
    "Accept": "application/vnd.github.v3+json",
    "User-Agent": "Termux-Secure-Agent"
}

encoded_content = base64.b64encode(MARKDOWN_CONTENT.encode("utf-8")).decode("utf-8")

# 5. Check if document path already exists to fetch its current SHA hash identifier
sha = None
try:
    check_req = Request(api_url, headers=headers, method="GET")
    with urlopen(check_req) as response:
        file_info = json.loads(response.read().decode("utf-8"))
        sha = file_info.get("sha")
except HTTPError as e:
    if e.code != 404:
        print(f"❌ Error checking file: {e.read().decode('utf-8')}")
        exit(1)

# 6. Prepare push parameters payload
payload = {
    "message": COMMIT_MESSAGE,
    "content": encoded_content,
    "branch": "main"
}
if sha:
    payload["sha"] = sha

# 7. Push payload securely to GitHub API endpoint
try:
    data = json.dumps(payload).encode("utf-8")
    push_req = Request(api_url, data=data, headers=headers, method="PUT")
    with urlopen(push_req) as response:
        res_data = json.loads(response.read().decode("utf-8"))
        action = "updated" if sha else "created"
        print(f"🚀 Success! File securely {action} via Environment Variables at:")
        print(res_data['content']['html_url'])
except HTTPError as e:
    print(f"❌ API Upload Failed: {e.read().decode('utf-8')}")
