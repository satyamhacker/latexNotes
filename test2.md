work to do for section ---10------



📦 Module 1: Agent Foundations & Basic Tooling
  ├── Level 1.1 — Core Agent Architecture & Iterative Workflow ([🟡 Intermediate])
  ├── Level 1.2 — LLM Agency Scope & smolagents Implementation ([🟢 Beginner])
  ├── Level 1.3 — Agent Environment Setup & Initialization ([🟢 Beginner])
  └── Level 1.4 — Structured Agent execution & Observability ([🔴 Advanced])

📦 Module 2: Control, Constraints & The Browser Brain
  ├── Level 2.1 — Prompt Template Engineering & Execution Analysis ([🟡 Intermediate])
  ├── Level 2.2 — Playwright Concepts & Toolkit Capabilities ([🟢 Beginner])
  ├── Level 2.3 — Environment Setup & Async Initialization ([🟡 Intermediate])
  └── Level 2.4 — Tool Extraction & Manual Local Execution ([🟡 Intermediate])

📦 Module 3: Advanced Orchestration & Live Web Extraction
  ├── Level 3.1 — Advanced Multi-Agent Orchestration (2026 Standards) ([🔴 Advanced])
  ├── Level 3.2 — Web Extraction Agent Setup & Local LLM Optimization ([🔴 Advanced])
  └── Level 3.3 — Web Extraction & Computation Workflows ([🔴 Advanced])
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Bhai, roadmap ready hai! Main seedha pehle module pe attack kar raha hoon. Let's go!


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
🧩 Module 1: Agent Foundations & Basic Tooling → Level 1.1: Core Agent Architecture & Iterative Workflow [🟡 Intermediate]
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

1. ⚡ The Concept (Ultra-Short)
Agent standard LLM ki tarah single-turn chat nahi karta, woh ReAct (Reasoning and Acting) framework pe chalta hai: Think, Act, Observe ka infinite loop.

2. 💥 Why? (Production Impact)
- Agar ye nahi kiya toh LLM ko bahar ki duniya ka data manually copy-paste karke dena padega.
- Automation impossible ho jayegi. APIs aur databases se LLM khud baat nahi kar payega.

3. 🎯 Practical Tasks (The Mission)
  Task 1: Ek custom `while True` loop ka logic structure banao. Dhyan rakhna ki usme `is_final_answer` check zaroor ho, warna loop break nahi hoga.
  The Logic: Yeh loop tab tak chalta hai jab tak agent ko final answer nahi mil jata. Yahi agent ka dil hai.

  Task 2: Apne loop mein step limits set karo. Wo parameter dhundho aur set karo jo agent ko infinite attempts karne se rokta hai.
  The Logic: API bills aasmaan chhu lenge agar agent kisi error ko fix karne ke loop mein phans gaya (Denial of Wallet). 

  Task 3: Memory update logic implement karo. Jab ek tool execute ho jaye, toh uska JSON result (Observation) agent ki history mein kaise append hoga?
  The Logic: Is feedback loop ke bina LLM apni galti nahi sudhaar payega ya agla step decide nahi kar payega.

  🔥 Combo Task: Router Pattern Flow
  Ek 3-phase flow practically execute karo:
  - Phase 1 (Offline): Ek dummy function banao jo sirf JSON return kare (e.g., weather data).
  - Phase 2 (Fixing): Apna ReAct loop run karo bina step limits ke deliberately, usko infinite loop mein jaane do (Ctrl+C se rokna!), phir limit fix karke dobara chalao.
  - Phase 3 (Live): Ek user query do jisme usko decision lena pade ki kaunsa tool call karna hai (Action determination).
  Challenge: Tool call block mein `execute_tool` logic ko string parse karne ke liye majboor karo.

4. ✅ Definition of Done ("Kaise pata chalega ki sahi hua?")
- Console output mein clearly step-by-step reasoning dikhni chahiye.
- Expected Log: `[Reasoning] User wants... [Observation] {"temp": 30} [Final Answer]...`
- Infinite loop ruk jana chahiye max iterations ke baad aur "Token Limit Exceeded / System Stopped" fallback aana chahiye.
- 💬 Quick Verify: "Agar koi pooche — Feedback loop agents mein kyun zaroori hai — toh seedha jawab de sakta hai?"

5. 🧠 Practical Takeaway (Asli Siksha — The Deep Dive)
- **max_iterations:** Yeh parameter teri API credits ki life insurance hai. Isko set nahi kiya toh bankruptcy pakki hai.
- **history.append:** LLM ki memory stateless hoti hai. Har iteration mein usko purana kachra (Observation) wapas bhejna padta hai taaki context rahe.
- ⚠️ Anti-Pattern: LLM par blindly trust karna ki woh hamesha sahi JSON dega. Wo extra text add kar deta hai. Isliye strict parsing zaroori hai.


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
🧩 Module 1: Agent Foundations & Basic Tooling → Level 1.2: LLM Agency Scope & smolagents Implementation [🟢 Beginner]
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

1. ⚡ The Concept (Ultra-Short)
smolagents ek Swiss Army Knife wrapper hai jo LLM ko external duniya (Gateway) se connect karta hai via explicit tools (Agency).

2. 💥 Why? (Production Impact)
- Over-privileged agents database uda sakte hain.
- Strict agency define nahi ki toh security breach confirm hai (Prompt Injection).

3. 🎯 Practical Tasks (The Mission)
  Task 1: Hugging Face ka `HfApiModel` initialize karo.
  The Logic: Yeh tera brain hai. Iski jagah tu local Ollama bhi plug in kar sakta hai, par dimaag set karna pehla step hai.

  Task 2: Ek Read-Only tool define karo (jaise `DuckDuckGoSearchTool`). Uske baad ek `CodeAgent` banao aur us tool ko list mein pass karo.
  The Logic: `tools=[]` list hi wo boundary hai jo decide karti hai ki agent bahar ki duniya mein kya kar sakta hai. Yahan "Segregation of Duties" follow hota hai.

  Task 3: Agent se ek simple web search karwao.
  The Logic: `agent.run()` internally wo saara `while True` loop handle karta hai jo tune Level 1.1 mein manually likha tha.

  🔥 Combo Task: Strict Scoping Demo
  Do agents banao: Ek "Read-Only" jiske paas sirf search tool ho, aur ek "Read-Write" jiske paas bash command execute karne ka tool ho (dummy mock karo).
  Challenge: Read-only agent ko bol ki file delete kare. Wo fail hona chahiye kyunki uski "Agency" mein wo tool nahi hai. 

4. ✅ Definition of Done ("Kaise pata chalega ki sahi hua?")
- Output aana chahiye: `[CodeAgent] Thinking... [CodeAgent] Executing tool: duckduckgo_search... [CodeAgent] Observation...`
- Read-only agent destructive prompt par saaf mana kar de.
- 💬 Quick Verify: "Agar koi pooche — Read-only aur Read-write agency mein kya fark hai aur risk kiska zyada hai — toh seedha jawab de sakta hai?"

5. 🧠 Practical Takeaway (Asli Siksha — The Deep Dive)
- **CodeAgent:** Yeh smolagents ka wo jadui wrapper hai jo direct Python code likh ke local sandbox mein chalata hai.
- **tools=[]:** Yeh list teri security firewall hai. Iske bahar agent andha aur lula hai.
- ⚠️ Anti-Pattern: Ek hi agent mein 20 tools daal dena. Agent confuse hoga aur Over-privileged ban jayega. Manager-Worker architecture use kar.


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
🧩 Module 1: Agent Foundations & Basic Tooling → Level 1.3: Agent Environment Setup & Initialization [🟢 Beginner]
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

1. ⚡ The Concept (Ultra-Short)
Manual if-else hatao, LangChain ka `initialize_agent` aur `AgentExecutor` lagao. Clean desk, clean code with `.env` setup.

2. 💥 Why? (Production Impact)
- Hardcoded API keys se tera AWS/OpenAI account hack ho jayega.
- Bina modular folder structure ke, 5+ tools hote hi code maintain karna nightmare ban jayega (DRY principle violation).

3. 🎯 Practical Tasks (The Mission)
  Task 1: Apne project root mein `.env` file banao aur `python-dotenv` use karke variables load karo.
  The Logic: API keys memory mein secure tarike se load honi chahiye, code mein nahi.

  Task 2: Ek alag module folder banao (empty `__init__.py` ke sath) aur wahan se tools import karo. Wildcard import (`*`) mat use karna!
  The Logic: Module isolation se `ModuleNotFoundError` nahi aata aur namespaces clash nahi hote.

  Task 3: LangChain ka `initialize_agent` factory function use karo. Isko tools ki list, LLM, aur `verbose` flag do.
  The Logic: Yeh function backend mein ek system prompt banata hai aur `AgentExecutor` engine return karta hai.

  🔥 Combo Task: The Modular Execution
  Tools ko alag file mein rakho. Jupyter notebook mein `.env` load karo. Dependency Injection ke through LLM aur tools ko `AgentExecutor` mein bhejo.
  Challenge: Agent run karte waqt `verbose=False` karke dekho, aur phir `verbose=True` karke dekho. Difference samjho ki logging kaise kaam karti hai.

4. ✅ Definition of Done ("Kaise pata chalega ki sahi hua?")
- Keys leak nahi honi chahiye. `.env` perfectly load ho.
- Output mein terminal par AgentExecutor chain dikhe: `> Entering new AgentExecutor chain... [Thought]... [Action]... [Final Answer]`
- 💬 Quick Verify: "Agar koi pooche — Boilerplate code aur Custom Tool Logic Agent framework se kaise replace hota hai — toh seedha jawab de sakta hai?"

5. 🧠 Practical Takeaway (Asli Siksha — The Deep Dive)
- **AgentExecutor:** Yeh wo thekedar hai jo tere tools aur LLM ke beech ka coordination khud handle karta hai. 
- **verbose=True:** Debugging ke liye mic ON. Lekin production mein dhyaan rakhna, PII leak ho sakta hai CloudWatch mein.
- ⚠️ Anti-Pattern: Notebook mein hardcoded keys dalna ya `from module import *` karna. Namespace clash ka sabse bada reason yahi hai.


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
🧩 Module 1: Agent Foundations & Basic Tooling → Level 1.4: Structured Agent execution & Observability [🔴 Advanced]
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

1. ⚡ The Concept (Ultra-Short)
Complex tools (multiple parameters wale) ke liye `STRUCTURED_CHAT` agent JSON payload deta hai, aur in sabke kharche ko track karne ke liye LangSmith meter-reader ka kaam karta hai.

2. 💥 Why? (Production Impact)
- Normal agents math functions jisme `a` aur `b` chahiye, usme strings pass karke fail ho jate hain (JSONDecodeError).
- Bina LangSmith ke, tujhe pata hi nahi chalega ki agent loop mein fass ke 4000 tokens kahan uda gaya.

3. 🎯 Practical Tasks (The Mission)
  Task 1: LangSmith observability on karo. System environment mein specifically V2 tracing aur API key set karo.
  The Logic: Yeh backend telemetry on kar dega bina code mein logic likhe. Ek-ek token track hoga.

  Task 2: `AgentType` ko explicitly us type pe set karo jo JSON payloads handle karta ho (`STRUCTURED_CHAT_ZERO_SHOT_REACT_DESCRIPTION`).
  The Logic: Yeh LLM ko force karega ki wo action inputs JSON `{}` format mein hi de taaki multiple arguments safely pass ho sakein.

  Task 3: Temperature ko 0 pe set karo chat model mein.
  The Logic: Fact-checking aur math tasks mein creativity (hallucination) zero honi chahiye.

  🔥 Combo Task: The Multi-Intent Stress Test
  Agent ko do complex tools do: Ek Math (multi-input) aur ek Wikipedia (string input). 
  Challenge: Agent ko ek single prompt do jismein do alag alag intents hon (e.g., math aur uske baad ek factual question). Observe karo kya wo parallel tool use karta hai ya hallucinate karke "Kamala Harris 2026" jaisa kachra deta hai. Isko LangSmith UI mein trace karo ki tokens kitne ude.

4. ✅ Definition of Done ("Kaise pata chalega ki sahi hua?")
- Output format explicitly JSON block mein aana chahiye `action_input: {"a": 150, "b": 250}`.
- LangSmith dashboard pe ek detailed trace generate hona chahiye jisme token count aur execution latency dikhe.
- 💬 Quick Verify: "Agar koi pooche — Multi-intent loading aur Instruction decay kya hota hai — toh seedha jawab de sakta hai?"

5. 🧠 Practical Takeaway (Asli Siksha — The Deep Dive)
- **STRUCTURED_CHAT_...:** Ye wahan use hoga jahan API ko Pydantic schemas ke mutabiq strictly defined multiple parameters chahiye.
- **LANGCHAIN_TRACING_V2:** Ye flag tere token bankruptcy ko rokhne ka pehla step hai.
- ⚠️ Anti-Pattern: Ek sath bohot saari instructions dena (Multi-intent loading). Isse LLM bhool jata hai ki start kahan se kiya tha (Instruction decay) aur kachra nikalta hai.


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
🏁 MODULE 1 RECAP — Tera Status Report
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Siksha Summary:
- Tu Agent aur Normal LLM ka farq practically samajh chuka hai.
- Tune smolagents aur LangChain dono use karke tools bind kiye hain.
- Tune structured JSON parsing ensure ki aur LangSmith se token tracking seekhi.

Guru-ji's Warning:
"Check kar le bhai! Kya tujhe yeh sab bina cheat sheet ke karna aa gaya hai? Agar inme se ek bhi cheez mein doubt hai ya confuse hai, toh chup chaap peeche ja aur wapas execute kar. Aage badhne ka koi fayda nahi agar basics hile hue hain!"

⚡ GURUDAKSHINA (The Checkpoint):
"Sare Levels clear hue? Screenshots taiyar rakh! Agar sab properly done hai toh type 'CONTINUE' for the next Module."

--- ⏸️ OUTPUT LIMIT APPROACHING. Type 'CONTINUE' to get the next part.
✅ Completed so far : Level 1.1, Level 1.2, Level 1.3, Level 1.4
⏳ Remaining       : Module 2 (Levels 2.1 to 2.4) and Module 3 (Levels 3.1 to 3.3)
📊 Progress        : 4 Levels done / 11 Levels total | Module 1 of 3

Bhai, aage badhte hain! Module 1 clear karke tera basic foundation strong ho chuka hai. Ab hum LLM ko ek proper direction aur "live web" ki aankhein dene wale hain. Seedha terminal aur editor focus!


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
🧩 Module 2: Control, Constraints & The Browser Brain → Level 2.1: Prompt Template Engineering & Execution Analysis [🟡 Intermediate]
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

1. ⚡ The Concept (Ultra-Short)
Agent ek khula sand hai. `ChatPromptTemplate` uska patta aur uniform hai jo usko "expert" banata hai aur JSON constraints enforce karta hai.

2. 💥 Why? (Production Impact)
- Bina System Message ke agent ko tone samajh nahi aati. Craziness aur Instruction Decay start ho jata hai.
- Format break hoga toh Garbage In Garbage Out (GIGO) ki wajah se application crash ho jayegi.

3. 🎯 Practical Tasks (The Mission)
  Task 1: `ChatPromptTemplate.from_messages` ka block banao. System role set karo as "expert in math and latest news" aur strict JSON output mandate karo.
  The Logic: Persona set karna aur rule banana (Output Constraints) pehla step hai hallucination rokne ka.

  Task 2: Ek `HumanMessage` block mein `{user_query}` variable inject karo using `format_messages`.
  The Logic: System aur User messages ko alag rakhne se "Prompt Injection" attacks avoid hote hain.

  🔥 Combo Task: The "Synthesis Failure" Trap
  Do tools setup karo (Math aur Wiki). Agent ko ek confusing query do: "Who is the president of 2025 and won in 2024?" (alternative query testing).
  Challenge: Isko execute karke dekho aur Observation vs Final Answer ko LangSmith trace mein analyze karo. Dekho kya tool simultaneous invoke hua? Aur kya LLM ka final answer anomalous (weird) nikla despite correct tool execution?

4. ✅ Definition of Done ("Kaise pata chalega ki sahi hua?")
- Trace mein ⭐"simultaneous tool invocation" (parallel execution) dikhna chahiye.
- Final Answer mein ⭐"anomalous answer" dikhna chahiye due to Synthesis Failure (e.g., mixing Biden with 2025).
- 💬 Quick Verify: "Agar koi pooche — Orchestration capability aur Generation (Synthesis) capability mein kya difference hai — toh seedha jawab de sakta hai?"

5. 🧠 Practical Takeaway (Asli Siksha — The Deep Dive)
- **ChatPromptTemplate:** Ye teri shield hai against agent going wild.
- **Data Source Limitation vs Framework Error:** Agar Wikipedia ne "Top Gun Maverick" ko latest movie bata diya, toh woh tool data limitation hai, LLM framework ka fault nahi.
- ⚠️ Anti-Pattern: "Agent kharab hai" bolke pura code delete mat kar. LangSmith mein check kar ki fault Orchestration (tool chunk execution) ka hai ya Synthesis (Final text generation) ka.


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
🧩 Module 2: Control, Constraints & The Browser Brain → Level 2.2: Playwright Concepts & Toolkit Capabilities [🟢 Beginner]
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

1. ⚡ The Concept (Ultra-Short)
Playwright agent ko ek invisible (headless) browser deta hai taaki woh JavaScript-heavy dynamic websites (React/Angular) padh sake.

2. 💥 Why? (Production Impact)
- BeautifulSoup sirf static HTML uthata hai. Modern SPAs (Single Page Applications) pe wo fail ho jayega aur `Loading...` laa ke de dega.

3. 📚 Research & Answer Tasks:
  (Yeh theory-heavy concept hai, isliye keyboard teri documentation dhoondhne mein chalega!)
  
  - Task 1: LangChain docs mein Playwright toolkit check kar. Wahan `click_element` aur `extract_text` exactly kis `BaseTool` class se inherit karte hain?
  - Task 2: 'Headless Browser' exactly RAM/CPU pe kaise save karta hai as compared to full UI browser?
  - Task 3: Granular Browser Control mein 'navigate back tool' (previous_webpage) ki kab zaroorat padti hai ek agent ko?

  🔥 Combo Task: The Security Threat Analysis
  Imagine kar tune Playwright browser agent ko dediya. What happens if the agent hits a website with malicious JavaScript?
  Challenge: "Confused Deputy" attack ke baare mein padh aur soch ki Playwright agent iska shikar kaise ban sakta hai.

4. ✅ Definition of Done ("Kaise pata chalega ki sahi hua?")
- Tujhe explicitly pata hona chahiye ki Chromium aur Webkit engines backend mein kaise execute hote hain.
- 💬 Quick Verify: "Agar koi pooche — BeautifulSoup aur Playwright mein se SPA (Single Page Application) ke liye konsa theek hai aur kyun — toh seedha jawab de sakta hai?"

5. 🧠 Practical Takeaway (Asli Siksha — The Deep Dive)
- **Headless Browser:** Bina screen (UI) wala browser jo fast execute karta hai background RAM mein.
- **Principle of Least Privilege:** Pure astra ke bakse (7 tools) ka access mat de, sirf zaroori tools hi allow kar.
- ⚠️ Anti-Pattern: Har website pe Playwright use karna bewakoofi hai. Static site ke liye simple HTTP requests (BeautifulSoup) zyada fast aur cheap hoti hain.


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
🧩 Module 2: Control, Constraints & The Browser Brain → Level 2.3: Environment Setup & Async Initialization [🟡 Intermediate]
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

1. ⚡ The Concept (Ultra-Short)
Jupyter notebook ke event loop aur Playwright ke async engine ka collision rokne ke liye `nest_asyncio` ka injection zaroori hai.

2. 💥 Why? (Production Impact)
- Bina iske tera browser initialize hote hi `RuntimeError` de dega. Poora headless setup crash ho jayega pheli line pe.

3. 🎯 Practical Tasks (The Mission)
  Task 1: `nest_asyncio.apply()` ko notebook cell ke top pe execute kar.
  The Logic: Yeh current REPL loop ko patch karta hai taaki naye async loops nest ho sakein. 

  Task 2: Background mein Chromium browser launch kar explicitly `create_async_playwright_browser()` call karke.
  The Logic: Yeh actual engine start karega.

  Task 3: Browser instance ko `PlaywrightWebBrowserToolkit.from_browser()` use karke LangChain se bind kar aur fir `.get_tools()` chala.
  The Logic: LangChain sidha Chromium nahi chalata, usko ek "Toolkit wrapper" chahiye hota hai jisse tools ki list nikle.

  🔥 Combo Task: Tool Count Verification
  Is loop ko run karke variables mein tools store kar aur explicitly count print kar. 
  Challenge: Ensure kar ki output strictly `Loaded 7 tools successfully.` aaye. 

4. ✅ Definition of Done ("Kaise pata chalega ki sahi hua?")
- Koi `RuntimeError` ya `This event loop is already running` nahi aana chahiye.
- Console output exactly: `Loaded 7 tools successfully.`
- 💬 Quick Verify: "Agar koi pooche — Production Server (FastAPI) aur local Jupyter mein nest_asyncio use karne ka farq kya hai — toh seedha jawab de sakta hai?"

5. 🧠 Practical Takeaway (Asli Siksha — The Deep Dive)
- **nest_asyncio:** Jupyter/Colab specific hack hai. Standard Python (.py) scripts mein iski zaroorat nahi.
- **browser.close():** Memory leak bachane ke liye session ke baad browser close zaroori hai (Singleton pattern in production).
- ⚠️ Anti-Pattern: Sirf `pip install` chalana aur `playwright install` bhool jana. Chromium binaries bina uske download nahi hongi aur `NotImplementedError` aayega.


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
🧩 Module 2: Control, Constraints & The Browser Brain → Level 2.4: Tool Extraction & Manual Local Execution [🟡 Intermediate]
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

1. ⚡ The Concept (Ultra-Short)
Agent ko andha-dhun saare tools dene se pehle "Tool Extraction" karke specific tool nikalo aur `.arun()` se locally test karo.

2. 💥 Why? (Production Impact)
- LLM ko agar galat CSS selector wala tool diya, toh wo confuse ho jayega. "Tool Isolation" bina test kiye directly Agent run karna debug nightmares lata hai.

3. 🎯 Practical Tasks (The Mission)
  Task 1: Tools ki list par conditional loop chala aur exact `tool.name` match karke sirf `Maps_browser` aur `get_elements` ko alag variables mein nikal.
  The Logic: Principle of least privilege. Jo chahiye sirf wahi nikal (O(n) filter vs O(1) Tool Registry lookup).

  Task 2: Ek async function bana aur usme navigation test kar: `await navigate_tool.arun({"url": "https://eapp.swami.com"})`.
  The Logic: `.run()` synchronous hai jo hang kar dega. Playwright tools hamesha `.arun()` (asynchronous run) mangte hain.

  Task 3: Page navigate hone ke baad, `.arun()` chala `get_elements` pe, aur usko specific target de: tag `h1` aur attribute `innerText`.
  The Logic: Humein backend ka ganda HTML nahi chahiye, sirf clean visible English text chahiye (innerText) taaki parse karne mein error na aaye.

  🔥 Combo Task: Full Manual Verification Loop
  Poora async loop ek single `asyncio.run()` mein bind kar aur run kar.
  Challenge: Is data ko bina Agent ke strictly JSON shape mein print karwa terminal pe. Dekh ki element_data ka result list array ke andar dictionary `{"innerText": ...}` mein aa raha hai ya nahi.

4. ✅ Definition of Done ("Kaise pata chalega ki sahi hua?")
- Output pehle `Navigating...` dikhaye, fir target page hit ho.
- Expected Extract: `Extracted Data: [{"innerText": "Login to eapp.swami.com"}]`
- 💬 Quick Verify: "Agar koi pooche — `.run()` aur `.arun()` mein main farq kya hai tools invoke karte waqt — toh seedha jawab de sakta hai?"

5. 🧠 Practical Takeaway (Asli Siksha — The Deep Dive)
- **tool.name filtering:** Hamesha tool filter karke do.
- **innerText via CSS Selectors:** XPATHs se zyada fast CSS selectors chalte hain Playwright mein, aur text visible render karta hai.
- ⚠️ Anti-Pattern: Direct LLM Agent start kar dena bina tools ko manually test kiye. CSS classes website pe daily change hoti hain, tera LLM hallucinate karega agar DOM empty return hua.


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
🏁 MODULE 2 RECAP — Tera Status Report
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Siksha Summary:
- Tune Prompt Templates se Agent ki madness control karni seekh li (Orchestration vs Synthesis).
- Tune Playwright Async Browser ka environment set kiya bina Jupyter crash kiye.
- Tune specific browser tools ko isolate karke `.arun()` ke zariye CSS targeting perfectly verify ki.

Guru-ji's Warning:
"Check kar le bhai! Kya tujhe yeh sab bina cheat sheet ke karna aa gaya hai? Agar inme se ek bhi cheez mein doubt hai ya confuse hai, toh chup chaap peeche ja aur wapas execute kar. Aage badhne ka koi fayda nahi agar basics hile hue hain!"

⚡ GURUDAKSHINA (The Checkpoint):
"Sare Levels clear hue? Screenshots taiyar rakh! Agar sab properly done hai toh type 'CONTINUE' for the next (AND FINAL) Module jahan hum sabko aapas mein connect karenge 2026 standards ke according!"

--- ⏸️ OUTPUT LIMIT APPROACHING. Type 'CONTINUE' to get the next part.
✅ Completed so far : Module 1 (All Levels), Module 2 (Levels 2.1 to 2.4)
⏳ Remaining       : Module 3 (Levels 3.1 to 3.3)
📊 Progress        : 8 Levels done / 11 Levels total | Module 2 of 3

Bhai, aakhri padav aa gaya! Ab tak tune jo seekha woh baccho ka khel tha. Ab hum 2026 standards ka hardcore "Multi-Agent System" aur "Web Extraction" lagayenge. Yeh tera final boss fight hai. Terminal khol aur focus 200% kar le!

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
🧩 Module 3: Advanced Orchestration & Live Web Extraction → Level 3.1: Advanced Multi-Agent Orchestration (2026 Standards) [🔴 Advanced]
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

1. ⚡ The Concept (Ultra-Short)
"God Agent" banane ke bajaye hum LangGraph ka use karke Supervisor (Manager) aur Worker (Mazdoor) agents banate hain jo ek `AgentState` (shared memory) ke through baat karte hain.

2. 💥 Why? (Production Impact)
- Ek single agent ko 15 tools dega toh wo infinite loop mein fass ke tera API bill (Denial of Wallet) aasmaan pe pahuncha dega.
- Agent isolation nahi hogi toh ek tool ke fail hone se poora system crash ho jayega.

3. 🎯 Practical Tasks (The Mission)
  Task [1]: Ek shared memory class banao `AgentState` naam se. Isme `TypedDict` aur `Annotated` use karke messages list aur `next_agent` string define kar.
  The Logic: Yeh inki common memory hai. `operator.add` ensure karega ki purane messages overwrite na hon, balki append hon.

  Task [2]: Do dummy Python functions bana: ek `supervisor_agent` aur ek `worker_agent`. Supervisor ka return state aisa ho jo agla agent "WebWorker" define kare, aur Worker ka return state "END" define kare.
  The Logic: Supervisor sirf routing karta hai, worker actual task execute karta hai aur loop end karta hai.

  Task [3]: LangGraph ka `StateGraph` setup kar. Start se Supervisor ko connect kar, Supervisor se WebWorker ko, aur WebWorker se `END` ko.
  The Logic: Yeh Directed Graph tera office map hai. Data ek node se dusre node pe safely flow karega.

  🔥 THE COMBO TASK (Final Boss):
  Is poore graph ko `.compile()` karke executable app bana.
  Challenge: Is `app.invoke` ko start kar ek initial message dekar. Check kar ki kya data sequentially flow hota hai aur sahi jagah pe print logging hoti hai.

4. ✅ Definition of Done ("Kaise pata chalega ki sahi hua?")
- Output mein clear dikhna chahiye: `[Supervisor] Routing task to WebWorker.` aur phir `[WebWorker] Executing extraction tool...`
- Graph loop complete hoke ruk jana chahiye (END state).
- 💬 Quick Verify: "Agar koi pooche — Multi-Agent workflows mein 'Blast Radius' kaise kam hota hai — toh seedha jawab de sakta hai?"

5. 🧠 Practical Takeaway (Asli Siksha — The Deep Dive)
- **AgentState:** Bina common state ke agents ek dusre ko nahi samajh sakte.
- **max_iterations per agent:** Isko set karna mat bhoolna, warna A->B->A->B ka infinite loop ban jayega.
- ⚠️ Anti-Pattern: Har chiz ke liye ek hi "God Agent" banana. Delegation is the key to reliability!


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
🧩 Module 3: Advanced Orchestration & Live Web Extraction → Level 3.2: Web Extraction Agent Setup & Local LLM Optimization [🔴 Advanced]
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

1. ⚡ The Concept (Ultra-Short)
Agent ko Playwright ka chashma pehna ke local Llama 3.2 model ke sath async loop mein daalna, taaki PII data safe rahe aur PC hang na ho.

2. 💥 Why? (Production Impact)
- Cloud LLMs par employee ka PII data (Karthik's email, salary) bhejega toh compliance breach ho jayega.
- Agar synchronous loop `.run()` chalaya Playwright pe, toh API endpoints block ho jayenge.

3. 🎯 Practical Tasks (The Mission)
  Task [1]: `ChatOllama` initialize kar, explicitly `model="llama3.2"` aur `temperature=0` set karke.
  The Logic: Llama 3.2 use karne ka specific reason hai iska ⭐"native tooling support" jo tool outputs strictly JSON mein nikalta hai. Temperature 0 fact-check ke liye zaroori hai.

  Task [2]: Apne agent ko `STRUCTURED_CHAT_ZERO_SHOT_REACT_DESCRIPTION` type ke sath initialize kar aur Playwright tools bind kar.
  The Logic: Yeh type ensure karta hai ki LLM complex tools ke parameters strictly JSON dictionary mein format karke de.

  Task [3]: Apne agent invocation ko `async def` function mein daal aur wahan explicitly `await agent_chain.arun(query)` use kar.
  The Logic: Playwright hamesha async hota hai. `await` nahi lagayega toh execution wahi freeze ho jayega.

  🔥 THE COMBO TASK (Final Boss):
  Ek dummy HTML structure dimag mein soch (internal-portal.local).
  Challenge: Agent ko user query de: "Go to the portal and find Karthik's salary and email". Dhyan rakh ki tu non-blocking `asyncio.run()` call karke is loop ko run kare aur agent properly navigate karke elements extract kare.

4. ✅ Definition of Done ("Kaise pata chalega ki sahi hua?")
- Terminal pe agent ki chain chalni chahiye bina code atke.
- Agent khud se `Maps_browser` aur `get_elements` choose kare aur exact final answer nikal ke de: "Karthik's email is karthik@company.com and his salary is $95000."
- 💬 Quick Verify: "Agar koi pooche — Web extraction agents mein `agent.arun()` kyun use karte hain aur Llama 3.2 ka native tooling support kya hai — toh seedha jawab de sakta hai?"

5. 🧠 Practical Takeaway (Asli Siksha — The Deep Dive)
- **Model Quantization (GGUF):** Heavy models local system ka VRAM kha jate hain, quantized models use kar taaki Context Window jaldi exhaust na ho.
- **RBAC:** Live portals pe agent utna hi dekh paye jiske paas uska access ho, warna Prompt Injection se internal data leak ho jayega.
- ⚠️ Anti-Pattern: Asynchronous backend mein synchronous `agent.run()` call karna. Event loop block hoga aur poori application dead ho jayegi.


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
🧩 Module 3: Advanced Orchestration & Live Web Extraction → Level 3.3: Web Extraction & Computation Workflows (DOM, JSON & Math) [🔴 Advanced]
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

1. ⚡ The Concept (Ultra-Short)
Agent ko sirf web page padhna nahi, balki multiple Employee IDs ki links nikalna, kachra data theek karna aur properly external math tool se average calculate karna aana chahiye.

2. 💥 Why? (Production Impact)
- LLMs math mein bohot weak hote hain. Agar string read karke average LLM se nikalwaya toh wo ⭐"2022.22" ki jagah kuch bhi hallucinate kar dega.
- Jab text ko JSON mein format karna hota hai, toh aksar LLM format break kar deta hai (JSONDecodeError). 

3. 🎯 Practical Tasks (The Mission)
  Task [1]: Apne `tools` list mein `extract_hyperlink_tool` aur ek explicit `calculator_tool` (ya REPL) combine kar.
  The Logic: SPAs pe data ek jagah nahi hota. Hrefs nikal ke navigate karna padta hai aur final computation calculator se hi karni hai.

  Task [2]: Ek aisi python `try-except` block bana jahan tu explicitly `JSONDecodeError` ko catch kare aur fallback logic set kare.
  The Logic: Agar LLM ne bola "Here is the data: {...}" toh standard `json.loads` fail ho jayega (Unparseable data). Error catch karna script ki jaan hai.

  🔥 THE COMBO TASK (Final Boss):
  Query bana: "Extract Employee IDs 23, 71, 489 links. Extract Karthik's salary. Compute the average salary."
  Challenge: Asynchronously run kar. Ek error simulate kar ke dikha (JSON raw string fail) jisko tera except block catch karke ek fixed dictionary `{"Karthik": 4000, "Average": 2022.22}` print kare. Is multi-step reasoning workflow ka poora execution smooth hona chahiye.

4. ✅ Definition of Done ("Kaise pata chalega ki sahi hua?")
- Output me print aana chahiye: `[WARNING] Unparseable data caught. Triggering fallback parser.`
- Final data perfectly parsed hona chahiye: `Final Computed Data: {'Karthik': 4000, 'Average': 2022.22}`
- 💬 Quick Verify: "Agar koi pooche — Agentic workflow mein mathematical aggregation ke liye explicitly calculator tool kyun chahiye — toh seedha jawab de sakta hai?"

5. 🧠 Practical Takeaway (Asli Siksha — The Deep Dive)
- **JSONDecodeError:** LLM format todega. Production mein `OutputFixingParser` ya `RetryOutputParser` lagana padta hai theek karne ke liye.
- **Combined Extraction and Computation:** Agent ko clearly batao ki calculation ke liye kaunsa tool call karna hai. 
- ⚠️ Anti-Pattern: LLM ko calculation khud textual predict karne bolna. Hamesha tool handoff karo computation ke liye.


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

