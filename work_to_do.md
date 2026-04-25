### STEP 1 — THE DEPENDENCY MAP

1. **Traditional Test Failure & Classical Healing** → no dependencies (start here)
2. **AI-First vs AI-Assisted Testing Strategy** → needs Concept 1
3. **Local vs Cloud LLMs (Enterprise Setup)** → needs Concept 2
4. **Self-Healing Framework Architecture** → needs Concept 3
5. **AI Self-Healing Execution (Asynchronous)** → needs Concept 4
6. **Manual Prompt Engineering for UI Locators** → needs Concept 5

---

### STEP 2 — FOR EVERY CONCEPT

#### CONCEPT 1 — Traditional Test Failure & Classical Healing [Beginner]
📌 Prerequisites: None (start here)

── PART A: CONCEPT-LEVEL QUESTIONS ──
1. [WHAT] 🟢 What is the fundamental difference between traditional static locators and classical self-healing arrays? 
2. [STRUCTURE] 🟢 What is the standard Page Object Model (POM) constructor skeleton for declaring element locators in a Python class?
3. [WHEN] 🟡 When does a standard Selenium script immediately throw an exception, and when does a classical healing tool decide to intervene?
4. [COMPARE] 🟡 Compare "Traditional Single Locators" vs. "Classical Array Fallbacks" vs. "Modern AI Prediction" in terms of maintenance effort.
5. [PURPOSE] 🟡 If classical healing arrays didn't exist in legacy tools (like TestProject), how would minor UI updates impact a 500-test suite?
6. [ANTI-PATTERN] 🔴 What is the massive maintenance anti-pattern involving absolute XPaths (e.g., `/html/body/div/div[2]/a`)? What is the correct approach?
7. [REAL EXAMPLE] 🟡 Describe how legacy tools historically implemented classical healing before LLMs existed.
8. [BREAK IT] 🔴 What exact exception is thrown in Python Selenium when a hardcoded UI locator (like an ID) changes? What is the root cause?

── PART B: PARAMETER DEEP-DIVE QUESTIONS ──
(No specific dynamic functional parameters; relies on standard static string locators).

---

#### CONCEPT 2 — AI-First vs AI-Assisted Testing Strategy [Beginner]
📌 Prerequisites: Concept 1

── PART A: CONCEPT-LEVEL QUESTIONS ──
1. [WHAT] 🟢 What defines an "AI-First" testing approach versus an "AI-Assisted" testing approach?
2. [STRUCTURE] 🟢 What is the high-level execution flow of an AI-Assisted approach when an element fails during runtime?
3. [WHEN] 🟡 When is it appropriate to use AI-First code generation, and when should you strictly enforce AI-Assisted healing?
4. [COMPARE] 🟡 Compare the monthly financial cost of generating 1000 AI-First tests daily versus using an AI-Assisted healing approach for 50 failures a day.
5. [PURPOSE] 🟡 If the AI-Assisted strategy didn't exist, what would happen to the CI/CD API token budget of an enterprise?
6. [ANTI-PATTERN] 🔴 What is "Wipe Coding"? Why is it dangerous for QA teams to rely entirely on AI agents to write boilerplate code?
7. [REAL EXAMPLE] 🟡 How does a large e-commerce company like Amazon balance 1000+ daily regression tests without exploding their cloud API budget?
8. [BREAK IT] 🔴 What happens to test reliability and maintenance if a team adopts AI-First but the AI hallucinated the base framework logic?

── PART B: PARAMETER DEEP-DIVE QUESTIONS ──
(No specific code parameters for this strategic overview).

---

#### CONCEPT 3 — Local vs Cloud LLMs (Enterprise Setup) [Intermediate]
📌 Prerequisites: Concept 2

── PART A: CONCEPT-LEVEL QUESTIONS ──
1. [WHAT] 🟢 What is a Local LLM (e.g., Ollama) and how does it differ from a Cloud LLM (e.g., OpenAI)?
2. [STRUCTURE] 🟢 Describe the network infrastructure skeleton required to run a Local LLM securely behind a corporate firewall.
3. [WHEN] 🟡 Give 3 specific enterprise industries (e.g., Healthcare, Banking) where using a Local LLM is legally mandatory.
4. [COMPARE] 🟡 Compare Local LLMs vs. Cloud LLMs in terms of Data Privacy, Request Cost, and Hardware Requirements.
5. [PURPOSE] 🟡 If Local LLMs didn't exist, why would enterprise companies be completely blocked from using self-healing testing on internal apps?
6. [ANTI-PATTERN] 🔴 What is the security anti-pattern of sending banking application DOM fragments to public OpenAI APIs for healing?
7. [REAL EXAMPLE] 🟡 How does a company use AWS SageMaker or AWS Bedrock to achieve "local" LLM privacy without buying physical GPUs?
8. [BREAK IT] 🔴 What hardware timeout error occurs if you attempt to run a 70 Billion parameter model on an old laptop lacking sufficient VRAM?

── PART B: PARAMETER DEEP-DIVE QUESTIONS ──

   [PARAM-WHAT] 🟢 **`model`** (Payload parameter)
   What does this parameter define in the payload sent to the Ollama server? What happens if it's omitted?
   [PARAM-VALUES] 🟡 List valid open-source model values (e.g., `llama3`, `mistral`).
   [PARAM-MISTAKE] 🔴 What error occurs if you pass a model name that hasn't been pulled to your local machine yet?
   [PARAM-REALCODE] 🟡 Show the exact JSON payload where this model parameter is defined for a local server.

   [PARAM-WHAT] 🟢 **`stream`** (Payload parameter)
   What does setting this parameter to boolean `False` achieve during an API call?
   [PARAM-VALUES] 🟡 What is the difference in network behavior between `True` and `False`?
   [PARAM-MISTAKE] 🔴 What parsing error will your Python script hit if this is accidentally left as `True`?
   [PARAM-REALCODE] 🟡 Show how to configure this parameter in a Python `requests` payload dictionary.

---

#### CONCEPT 4 — Self-Healing Framework Architecture [Intermediate]
📌 Prerequisites: Concept 3

── PART A: CONCEPT-LEVEL QUESTIONS ──
1. [WHAT] 🟢 What are the three core pillars (Core, Bridge, Brain) of a Self-Healing Framework Architecture?
2. [STRUCTURE] 🟢 What is the high-level code structure used to bridge a Selenium Python script with an LLM?
3. [WHEN] 🟡 When should you use a dedicated pip package (like `openai`) versus a custom HTTP `requests` wrapper?
4. [COMPARE] 🟡 Compare tightly coupled AI framework architecture vs. modular API-driven framework architecture.
5. [PURPOSE] 🟡 Why is Context Engineering specifically placed at the "catch" block of the framework pipeline?
6. [ANTI-PATTERN] 🔴 What is the severe security mistake of hardcoding API keys directly into the framework bridge code? Where should they go instead?
7. [REAL EXAMPLE] 🟡 Show how a QA service provider builds a custom Python HTTP wrapper to communicate with their internally hosted LLMs.
8. [BREAK IT] 🔴 What happens to your framework if it is tightly coupled to OpenAI's SDK and the company suddenly mandates a switch to local Llama models?

── PART B: PARAMETER DEEP-DIVE QUESTIONS ──
(No specific parameters; focus is on architectural patterns).

---

#### CONCEPT 5 — AI Self-Healing Execution (Asynchronous) [Advanced]
📌 Prerequisites: Concept 4

── PART A: CONCEPT-LEVEL QUESTIONS ──
1. [WHAT] 🟢 What is the "Magic Time" latency in AI self-healing execution?
2. [STRUCTURE] 🟢 What is the required Python syntax (`async def`, `await`) to ensure the test framework does not freeze while waiting for the LLM?
3. [WHEN] 🟡 When MUST you use asynchronous programming for test healing? What happens if you use synchronous calls?
4. [COMPARE] 🟡 Compare standard test execution times (~7 seconds) vs. AI self-healing execution times (~18-45 seconds).
5. [PURPOSE] 🟡 If asynchronous event loops weren't used, how would the long LLM inference times impact the broader UI thread or CI pipeline?
6. [ANTI-PATTERN] 🔴 What is the CI/CD anti-pattern regarding default timeout limits when introducing self-healing?
7. [REAL EXAMPLE] 🟡 Describe how an overnight regression suite handles the extra 18+ seconds of "Magic Time" per healed test without impacting delivery.
8. [BREAK IT] 🔴 What exact framework crash happens if you attempt to `await` a healing function without utilizing an `asyncio.run()` event loop?

── PART B: PARAMETER DEEP-DIVE QUESTIONS ──

   [PARAM-WHAT] 🟢 **`friendly_name`** What is this parameter passed into the healing function? Why does the AI need it?
   [PARAM-VALUES] 🟡 Show 3 examples of good friendly names versus bad ones.
   [PARAM-MISTAKE] 🔴 What hallucination occurs if you pass a highly ambiguous friendly name (like "button") to the LLM?
   [PARAM-REALCODE] 🟡 Show a Python method signature where this is passed down into the context payload.

   [PARAM-WHAT] 🟢 **`temperature`** (App Settings)
   What does this LLM configuration parameter control in the context of automation testing?
   [PARAM-VALUES] 🟡 What is the difference between a value of `0.1` and `0.9`?
   [PARAM-MISTAKE] 🔴 Why is setting a high temperature an absolute mistake for locator generation?
   [PARAM-REALCODE] 🟡 Show how this parameter is hardcoded into the `app_settings` dictionary for strict logical output.

   [PARAM-WHAT] 🟢 **`base_url`** (App Settings)
   What does this parameter define when connecting to Ollama?
   [PARAM-VALUES] 🟡 What is the standard local port default value for Ollama (e.g., `http://localhost:11434/api`)?
   [PARAM-MISTAKE] 🔴 What connection error (`ConnectionRefusedError`) will occur if the background daemon isn't running on this port?
   [PARAM-REALCODE] 🟡 Show how this is dynamically constructed in the `requests.post()` call.

---

#### CONCEPT 6 — Manual Prompt Engineering for UI Locators [Advanced]
📌 Prerequisites: Concept 5

── PART A: CONCEPT-LEVEL QUESTIONS ──
1. [WHAT] 🟢 What is Meta-Prompting in the context of UI locator extraction?
2. [STRUCTURE] 🟢 What are the mandatory constraints needed in a prompt to ensure clean JSON output? (e.g., strict JSON, double quotes, no markdown).
3. [WHEN] 🟡 When MUST you manually pass raw `View Page Source` HTML into the prompt instead of simply providing the target URL?
4. [COMPARE] 🟡 Compare passing a URL to a Local LLM vs. pasting raw HTML Source Code. Why does the URL approach fail locally?
5. [PURPOSE] 🟡 If you don't explicitly reject unsupported locators (like `CSS alt` or `CSS type`), what parsing failure will your Selenium wrapper encounter?
6. [ANTI-PATTERN] 🔴 What is the anti-pattern of asking the LLM to "write the code to click the button" instead of "return the locator data"?
7. [REAL EXAMPLE] 🟡 Show how a QA Lead uses "Developer Hats" to iteratively meta-prompt a Cloud model until they derive the perfect golden prompt string for the whole team.
8. [BREAK IT] 🔴 What exact Python error (`json.decoder.JSONDecodeError`) is thrown if the AI returns the JSON object using single quotes (`'`) instead of double quotes (`"`)?

── PART B: PARAMETER DEEP-DIVE QUESTIONS ──
(No specific code parameters; focuses heavily on Prompt Engineering constraints).

---

### 📊 FINAL CURRICULUM SUMMARY

→ **Total Concept Count:** 6
→ **Total Parameter Count Covered:** 5
→ **Total Question Count:** 68

**Recommended Study Order:**
1. Traditional Test Failure & Classical Healing (Concept 1)
2. AI-First vs AI-Assisted Testing Strategy (Concept 2)
3. Local vs Cloud LLMs (Enterprise Setup) (Concept 3)
4. Self-Healing Framework Architecture (Concept 4)
5. AI Self-Healing Execution (Asynchronous) (Concept 5)
6. Manual Prompt Engineering for UI Locators (Concept 6)

**Scoring System:**
* 🟢 **Beginner = 1 pt**
* 🟡 **Intermediate = 2 pts**
* 🔴 **Advanced = 3 pts**
* **Mastery Threshold = 85% of total points**
* *Self-check method:* Attempt all questions in an empty editor → compare with official docs/framework source code → add 1 pt per verified correct understanding.

==================================================================================
