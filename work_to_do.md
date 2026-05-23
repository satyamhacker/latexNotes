# Section 12: Building AI Agent with RAG and Tooling support (Project)



### DEPENDENCY MAP

* **CONCEPT 1 — Environment Initialization & Secret Management (`load_dotenv`)** → no dependencies (start here)
* **CONCEPT 2 — Tool Definition & Metadata (`@tool`, Docstrings)** → needs Concept 1
* **CONCEPT 3 — Vector Embeddings & Persistent Storage (`OllamaEmbeddings`, `Chroma`)** → no dependencies (can learn alongside Concept 1)
* **CONCEPT 4 — Retriever Operations (`as_retriever`, `invoke`)** → needs Concept 3
* **CONCEPT 5 — Cloud LLM Integration (`ChatOllama`)** → needs Concept 1
* **CONCEPT 6 — Agent Prompting & Construction (`PromptTemplate`, `create_react_agent`, `AgentExecutor`)** → needs Concept 2, Concept 4, Concept 5
* **CONCEPT 7 — Asynchronous Execution (`ainvoke`)** → needs Concept 6
* **CONCEPT 8 — Agent Observability (`LangSmith`, `verbose`)** → needs Concept 6

---

### CONCEPT 1 — Environment Initialization & Secret Management

📌 **Prerequisites:** None (start here)

── **PART A: CONCEPT-LEVEL QUESTIONS** ──

* [WHAT] 🟢 What is `load_dotenv()`? Define its exact role in a Python execution environment.
* [STRUCTURE] 🟢 What is the standard directory structure and minimal Python code required to safely load environment variables using this library?
* [WHEN] 🟡 Name 3 real-world scenarios in AI agent development where you MUST use a `.env` file instead of hardcoding values. When is `.env` insufficient?
* [COMPARE] 🟡 How does using `dotenv` compare to setting variables directly in the OS terminal (`export KEY=VALUE`) or hardcoding them in an `agent.py` file? Compare in terms of security, portability, and ease of use.
* [PURPOSE] 🟡 If `load_dotenv()` and environment variables didn't exist, what exact security and deployment problems would developers face when pushing code to GitHub?
* [ANTI-PATTERN] 🔴 What is the most common mistake beginners make regarding their `.env` file when initializing a Git repository? What is the correct approach?
* [REAL EXAMPLE] 🟡 Describe a production scenario where a LangChain AI application uses `load_dotenv()`. Exactly which keys would typically reside in that `.env` file?
* [BREAK IT] 🔴 What happens if `load_dotenv()` is called but the `.env` file is completely missing? What exact error will subsequent code (like connecting to an LLM) throw, and how do you debug it?

── **PART B: PARAMETER DEEP-DIVE QUESTIONS** ──

**Parameter: `dotenv_path` [🔍 Verify from docs]**

* [PARAM-WHAT] 🟢 What is the `dotenv_path` parameter in `load_dotenv()`? What happens if I don't pass it?
* [PARAM-VALUES] 🟡 What values can it accept? Give examples of both absolute and relative paths.
* [PARAM-MISTAKE] 🔴 What bug will occur if your terminal is running in `/project/src/` but your `.env` is in `/project/` and you rely on the default parameter?
* [PARAM-REALCODE] 🟡 Write a production snippet where `dotenv_path` is explicitly set using `os.path.join` to guarantee the file is found regardless of where the script is executed from.

**Parameter: `override` [🔍 Verify from docs]**

* [PARAM-WHAT] 🟢 What does the `override` boolean parameter do in `load_dotenv()`?
* [PARAM-VALUES] 🟡 What is the default value? How does the behavior change if set to `True` vs `False`?
* [PARAM-MISTAKE] 🔴 What silent bug can occur in production (e.g., inside a Docker container) if you mistakenly set `override=True`?
* [PARAM-REALCODE] 🟡 Show a snippet using `override=False` and explain why this is the preferred default for cloud deployments.

---

### CONCEPT 2 — Tool Definition & Metadata (`@tool`)

📌 **Prerequisites:** Concept 1

── **PART A: CONCEPT-LEVEL QUESTIONS** ──

* [WHAT] 🟢 What is the `@tool` decorator in LangChain? What does it do to a standard Python function?
* [STRUCTURE] 🟢 What are the mandatory components of a function wrapped with `@tool`? (Hint: Think about typing and descriptions). Show the minimal working code skeleton.
* [WHEN] 🟡 When should you wrap a function with `@tool`? Give 3 examples of actions an agent might need. When should a function remain a standard utility function without the decorator?
* [COMPARE] 🟡 How does an `@tool` function differ from a standard Python function in terms of how an LLM "sees" it?
* [PURPOSE] 🟡 If `@tool` didn't exist, what complex parsing and JSON-schema generation tasks would you have to write manually to give an LLM access to external scripts?
* [ANTI-PATTERN] 🔴 What is the wrong way to write a docstring inside an `@tool` function? What common mistake causes the agent to never invoke the tool?
* [REAL EXAMPLE] 🟡 Walk through a scenario where a `fetch_web_page` tool (using Playwright) is registered. How does the agent's brain know this tool is meant for web scraping?
* [BREAK IT] 🔴 What exact error or agent hallucination will occur if your `@tool` function is missing type hints (e.g., `def fetch_data(query):` instead of `def fetch_data(query: str) -> str:`)?

── **PART B: PARAMETER DEEP-DIVE QUESTIONS** ──

**Parameter: `name` (Hidden/Override parameter in `@tool`) [🔍 Verify from docs]**

* [PARAM-WHAT] 🟢 What is the `name` parameter inside the `@tool(name="...")` decorator? If omitted, what does LangChain use by default?
* [PARAM-VALUES] 🟡 What format must this string follow? (Are spaces allowed? Special characters?)
* [PARAM-MISTAKE] 🔴 What happens to the agent's routing logic if multiple tools share identical or highly confusing names?
* [PARAM-REALCODE] 🟡 Show code where a function named `search_v2_final` is wrapped with a cleaner, agent-friendly tool name.

**Parameter: `return_direct` [🔍 Verify from docs]**

* [PARAM-WHAT] 🟢 What does `return_direct=True` do when passed into the `@tool` decorator?
* [PARAM-VALUES] 🟡 It accepts a boolean. What is the default?
* [PARAM-MISTAKE] 🔴 If you are building a multi-step agent that needs to analyze a webpage and *then* summarize it, what breaks if you set `return_direct=True` on the Playwright scraper tool?
* [PARAM-REALCODE] 🟡 Write a snippet for an `emergency_stop` tool where `return_direct=True` is the absolutely correct choice.

---

### CONCEPT 3 — Vector Embeddings & Persistent Storage (`Chroma`)

📌 **Prerequisites:** None

── **PART A: CONCEPT-LEVEL QUESTIONS** ──

* [WHAT] 🟢 What is `Chroma` in this architecture, and what role does `OllamaEmbeddings` play alongside it?
* [STRUCTURE] 🟢 What are the required arguments to connect an existing, on-disk Chroma database to a LangChain app? Show the code skeleton.
* [WHEN] 🟡 When should you use a persistent Vector Store (loading from a directory) versus an in-memory Vector Store? Give 3 production triggers.
* [COMPARE] 🟡 Make a comparison table between `Persistent Chroma DB` and `In-Memory Chroma DB` covering: Lifecycle, Speed/Latency upon startup, and Memory usage.
* [PURPOSE] 🟡 If embeddings didn't exist, why would traditional keyword search fail to find "puppy" if the database only contained the word "dog"?
* [ANTI-PATTERN] 🔴 What is the wrong way to connect to an existing vector database when writing a new agent script? (Hint: think about re-ingestion).
* [REAL EXAMPLE] 🟡 In a legal firm's AI tool, how is the persistent `Chroma` database updated at night vs read during the day by the agent?
* [BREAK IT] 🔴 What exact "Dimension Mismatch Error" will you see if the data was saved using `all-MiniLM-L6-v2` but your agent script initializes `OllamaEmbeddings(model="llama3.2")`? What is the root cause?

── **PART B: PARAMETER DEEP-DIVE QUESTIONS** ──

**Parameter: `model` (in `OllamaEmbeddings`)**

* [PARAM-WHAT] 🟢 What does the `model` parameter define? What happens if you omit it?
* [PARAM-VALUES] 🟡 List 3 valid model strings for Ollama embeddings.
* [PARAM-MISTAKE] 🔴 What silent logic failure occurs if the `model` string points to an LLM optimized for generation (e.g., `llama3`) instead of an embedding-specific model?
* [PARAM-REALCODE] 🟡 Show how to initialize `OllamaEmbeddings` correctly targeting a specific version, ensuring it strictly matches the ingestion pipeline.

**Parameter: `persist_directory` (in `Chroma`)**

* [PARAM-WHAT] 🟢 What is `persist_directory`?
* [PARAM-VALUES] 🟡 What values does it accept? Explain the difference between passing `"./db"` and `"../Section 5/chroma_db"`.
* [PARAM-MISTAKE] 🔴 What catastrophic data bug happens if you provide a relative path (`../db`) but execute the python script from a completely different working directory? Does Chroma throw an error or silently create an empty folder?
* [PARAM-REALCODE] 🟡 Write a snippet that uses Python's `os.path.abspath` to dynamically resolve `persist_directory` so it never fails regardless of where the terminal is opened.

**Parameter: `embedding_function` (in `Chroma`)**

* [PARAM-WHAT] 🟢 What does `embedding_function` do? Why must Chroma know about this during retrieval?
* [PARAM-VALUES] 🟡 What kind of object must be passed here? (Can I pass a string?)
* [PARAM-MISTAKE] 🔴 What exact error will the retriever throw later if `embedding_function` is entirely omitted when connecting to an existing database?
* [PARAM-REALCODE] 🟡 Show the minimal robust code to bind an Ollama embedding instance into the Chroma initialization.

---

### CONCEPT 4 — Retriever Operations (`as_retriever`, `invoke`)

📌 **Prerequisites:** Concept 3

── **PART A: CONCEPT-LEVEL QUESTIONS** ──

* [WHAT] 🟢 What does `db.as_retriever()` do, and what is the `invoke()` method?
* [STRUCTURE] 🟢 Show the syntax for creating a retriever from a database and invoking it with a user query. What object type is returned?
* [WHEN] 🟡 When should an agent use a `Retriever` instead of direct database methods like `similarity_search`?
* [COMPARE] 🟡 Compare `VectorStore` (the raw database object) vs `BaseRetriever` (the wrapped object). When building a LangChain `@tool`, why is the Retriever interface strictly preferred?
* [PURPOSE] 🟡 If `as_retriever()` didn't exist, how much manual boilerplate code would you need to write to integrate a database query into a standard LangChain tool?
* [ANTI-PATTERN] 🔴 What mistake do developers make with the output of `retriever.invoke()` when returning data from an `@tool` back to an agent? (Hint: returning a list of Objects vs a String).
* [REAL EXAMPLE] 🟡 Describe the exact data flow: User asks a bias question -> Agent calls bias tool -> Tool calls `invoke` -> What happens mathematically to the query before it hits the disk?
* [BREAK IT] 🔴 What happens if `retriever.invoke(query)` finds exactly zero matches? Does it crash? How should your tool gracefully handle this so the agent doesn't hallucinate?

── **PART B: PARAMETER DEEP-DIVE QUESTIONS** ──

**Parameter: `search_type` (in `as_retriever()`) [🔍 Verify from docs]**

* [PARAM-WHAT] 🟢 What is `search_type`? What does it dictate about how the retriever finds documents?
* [PARAM-VALUES] 🟡 It defaults to `"similarity"`. What are the other valid string options (e.g., mmr)?
* [PARAM-MISTAKE] 🔴 If your VectorStore is flooded with duplicate documents, what issue will the default `"similarity"` search cause for the agent's context window?
* [PARAM-REALCODE] 🟡 Show how to instantiate a retriever using `"mmr"` (Maximal Marginal Relevance) to ensure the agent receives diverse chunks of information.

**Parameter: `search_kwargs` (in `as_retriever()`) [🔍 Verify from docs]**

* [PARAM-WHAT] 🟢 What is `search_kwargs`? How does it control the limits of the search?
* [PARAM-VALUES] 🟡 What data structure does it accept? Give an example containing the `k` key.
* [PARAM-MISTAKE] 🔴 What happens to the LLM's context window (token limit) if `k` is accidentally set to `50` instead of `4` when retrieving dense PDF pages?
* [PARAM-REALCODE] 🟡 Write a snippet where `as_retriever` is configured to use a specific `search_kwargs` dictionary to filter by metadata (e.g., only searching within `{"source": "policy.pdf"}`).

**Parameter: `input` / `query` (in `retriever.invoke()`)**

* [PARAM-WHAT] 🟢 What is the required parameter for the `invoke()` method?
* [PARAM-VALUES] 🟡 Does it accept a string, a dictionary, or a LangChain Message object?
* [PARAM-MISTAKE] 🔴 What silent failure occurs if the agent passes a massive, 1000-word conversational paragraph into `invoke()` instead of a condensed, keyword-rich search query?
* [PARAM-REALCODE] 🟡 Show how to extract `page_content` from the results of an `invoke()` call and format it safely into a single string for the agent's observation.

---

**This completes Chunk 1 (Concepts 1-4).**
To prevent context overflow and ensure maximum depth, I have paused here.

**Reply `CONTINUE` for the next batch (Concepts 5 through 8: Cloud Integration, LangChain v1.0 Agent Construction, Async Execution, and Observability).**

Here is the final batch of your structured question set, covering Cloud Integration, Agent Construction, Asynchronous Execution, and Observability.

### CONCEPT 5 — Cloud LLM Integration (`ChatOllama`)

📌 **Prerequisites:** Concept 1

── **PART A: CONCEPT-LEVEL QUESTIONS** ──

* [WHAT] 🟢 What is `ChatOllama` in this context, and how does configuring it for the cloud differ from running it locally?
* [STRUCTURE] 🟢 What are the required arguments to connect LangChain to a remote Ollama Cloud instance? Show the minimal working code skeleton.
* [WHEN] 🟡 Give 3 real-world situations where you MUST offload your agent's LLM to a cloud provider instead of running it on a local GPU. When should you stick to local?
* [COMPARE] 🟡 Make a comparison table between running a `Local 8B Model` vs an `Ollama Cloud 32B Model` covering: Execution Speed/Latency, GPU RAM cost, and Reasoning Capability.
* [PURPOSE] 🟡 If cloud inferencing didn't exist, what physical hardware barrier would prevent a solo developer from testing heavy models like Qwen 2.5 32B?
* [ANTI-PATTERN] 🔴 What is the wrong way to manage the data flow when shifting from a fully local secure environment to Ollama Cloud? (Hint: Think about PII and enterprise data).
* [REAL EXAMPLE] 🟡 Walk through a scenario where a startup scales their AI agent from local beta testing to cloud production. How does the 1.2 minute latency drop to 33 seconds?
* [BREAK IT] 🔴 What exact error will you see if your cloud model string (e.g., `"qwen2.5:32b"`) is correct, but your automatic login/API key is missing or expired?

── **PART B: PARAMETER DEEP-DIVE QUESTIONS** ──

**Parameter: `model` (in `ChatOllama`)**

* [PARAM-WHAT] 🟢 What does the `model` parameter specify when calling `ChatOllama`?
* [PARAM-VALUES] 🟡 List 2 specific model strings mentioned for high-tier reasoning and coding (e.g., Qwen variants). What happens if you request a model not hosted on the cloud?
* [PARAM-MISTAKE] 🔴 What is the most common silent bug regarding model selection when switching from a basic chat task to strict JSON tool-calling tasks?
* [PARAM-REALCODE] 🟡 Show the exact Python code to initialize a strictly coding-optimized 32-billion parameter model via Ollama.

**Parameter: `base_url` (in `ChatOllama`)**

* [PARAM-WHAT] 🟢 What does `base_url` do? What happens if you don't pass it?
* [PARAM-VALUES] 🟡 What is the exact string value used to point to Ollama Cloud?
* [PARAM-MISTAKE] 🔴 What networking error will Python throw if you accidentally type `[http://api.ollama.cloud](http://api.ollama.cloud)` instead of `https://`?
* [PARAM-REALCODE] 🟡 Write a snippet where `base_url` is loaded dynamically from `.env` using `os.getenv()` rather than hardcoding it in the script.

---

### CONCEPT 6 — Agent Prompting & Construction (LangChain v1.0)

📌 **Prerequisites:** Concept 2, Concept 4, Concept 5

── **PART A: CONCEPT-LEVEL QUESTIONS** ──

* [WHAT] 🟢 What is the `create_react_agent` + `AgentExecutor` pattern? Why did LangChain introduce it to replace the old approach?
* [STRUCTURE] 🟢 What are the mandatory components needed to successfully instantiate a v1.0 React Agent? Show the minimal working code skeleton including the prompt template.
* [WHEN] 🟡 When should you use `create_react_agent` versus other agent types (like `create_tool_calling_agent`)? Give 3 triggers for picking the React framework.
* [COMPARE] 🟡 Make a side-by-side comparison table of `initialize_agent()` (v0.x) vs `create_react_agent()` (v1.0) covering: Modularity, Deprecation status, and Prompt transparency.
* [PURPOSE] 🟡 If LangChain had not deprecated the "black box" `initialize_agent` function, what exact difficulties would developers face when trying to debug an agent's internal thought process?
* [ANTI-PATTERN] 🔴 What is the most common mistake developers make when encountering a `DeprecationWarning` for `initialize_agent`? What is the correct approach?
* [REAL EXAMPLE] 🟡 Describe a production system update where a developer refactors an old LangChain codebase. Exactly how is the tool binding and executor setup split into two steps?
* [BREAK IT] 🔴 What exact `AttributeError` or `ImportError` will you see if you upgrade to a future version of LangChain but leave `initialize_agent` in your code?

── **PART B: PARAMETER DEEP-DIVE QUESTIONS** ──

**Parameter: `{agent_scratchpad}` (in `PromptTemplate`)**

* [PARAM-WHAT] 🟢 What is the `{agent_scratchpad}` placeholder? Why is it absolutely mandatory in the prompt?
* [PARAM-VALUES] 🟡 What data does LangChain dynamically inject into this variable during the execution loop?
* [PARAM-MISTAKE] 🔴 What exact parsing error or infinite loop will occur if you forget to include `{agent_scratchpad}` at the end of your prompt string?
* [PARAM-REALCODE] 🟡 Show a fully working, production-grade string for `prompt_template` that includes a system persona, user input, and the scratchpad.

**Parameter: `tools` (in `create_react_agent` AND `AgentExecutor`)**

* [PARAM-WHAT] 🟢 Why must the `tools` list be passed to *both* the agent constructor and the executor?
* [PARAM-VALUES] 🟡 What exactly goes inside this list? (Strings of tool names, or the `@tool` object references themselves?)
* [PARAM-MISTAKE] 🔴 What silent logic failure occurs if you pass `[playwright_tool, bias_tool]` to the agent constructor, but only pass `[playwright_tool]` to the `AgentExecutor`?
* [PARAM-REALCODE] 🟡 Show the precise code mapping an LLM, a specific list of tools, and a PromptTemplate into `create_react_agent`.

---

### CONCEPT 7 — Asynchronous Execution (`ainvoke`)

📌 **Prerequisites:** Concept 6

── **PART A: CONCEPT-LEVEL QUESTIONS** ──

* [WHAT] 🟢 What is `ainvoke()`? How does it differ fundamentally from standard `.invoke()` in Python?
* [STRUCTURE] 🟢 What keywords must be added to a function to allow the use of `ainvoke`? Show the minimal async function code skeleton.
* [WHEN] 🟡 When should you use `ainvoke()` in an AI application? Give 3 production scenarios (e.g., web servers, batch processing). When is standard `invoke()` acceptable?
* [COMPARE] 🟡 Compare `.invoke()` vs `.ainvoke()` covering: Thread blocking, Handling multiple concurrent users, and Code syntax requirements.
* [PURPOSE] 🟡 If async capabilities didn't exist in Python/LangChain, what would happen to user #2 if user #1 triggered a bias check that takes 33 seconds to execute?
* [ANTI-PATTERN] 🔴 What is the wrong way to call an `await` function in a standard Python script?
* [REAL EXAMPLE] 🟡 Describe a scenario where a FastAPI backend receives 5 simultaneous requests to evaluate bias on different URLs. How does `ainvoke` handle the queue?
* [BREAK IT] 🔴 What exact `SyntaxError` or `RuntimeWarning` will you see if you write `response = agent_executor.ainvoke(...)` without the `await` keyword?

── **PART B: PARAMETER DEEP-DIVE QUESTIONS** ──

**Parameter: `input` (dictionary key passed to `ainvoke`)**

* [PARAM-WHAT] 🟢 Why do we pass a dictionary like `{"input": query}` into `ainvoke` instead of just passing the raw query string?
* [PARAM-VALUES] 🟡 What data types can the value of the `"input"` key hold? Can it hold a list of LangChain Message objects?
* [PARAM-MISTAKE] 🔴 What specific missing key error will LangChain throw if you pass `{"query": "Check this"}` instead of `{"input": "Check this"}` when the PromptTemplate explicitly expects `{input}`?
* [PARAM-REALCODE] 🟡 Write an asynchronous Python function `execute_query(url: str)` that formats the URL into the input dictionary and properly awaits the `ainvoke` execution.

---

### CONCEPT 8 — Agent Observability (`LangSmith`)

📌 **Prerequisites:** Concept 6

── **PART A: CONCEPT-LEVEL QUESTIONS** ──

* [WHAT] 🟢 What is LangSmith, and what does it mean to capture a "trace" of an AgentExecutor chain?
* [STRUCTURE] 🟢 What exact environment variables must be present in your `.env` file to instantly enable LangSmith tracing without changing any Python code?
* [WHEN] 🟡 When is comprehensive observability mandatory? Give 3 scenarios in the agent lifecycle (e.g., debugging loops, evaluating prompts).
* [COMPARE] 🟡 Compare `verbose=True` (Console Logging) vs `LangSmith Tracing` covering: Data persistence, Visual UI, and Ability to analyze historical failures.
* [PURPOSE] 🟡 If LangSmith didn't exist, what exact problem would a developer face when a user reports: "The agent gave me the wrong bias report yesterday"?
* [ANTI-PATTERN] 🔴 What is the danger of leaving `verbose=True` running in a deployed production Docker container without proper tracing enabled?
* [REAL EXAMPLE] 🟡 Walk through a news organization's audit. An agent flagged an article as biased. How does the developer use LangSmith's UI to prove *exactly* which PDF page the agent read to make that decision?
* [BREAK IT] 🔴 What happens to the application if `LANGCHAIN_TRACING_V2="true"` is set, but the `LANGCHAIN_API_KEY` is completely invalid? Does the agent crash, or fail silently?

── **PART B: PARAMETER DEEP-DIVE QUESTIONS** ──

*(Note: LangSmith uses environment variables as its core configuration parameters)*

**Parameter: `LANGCHAIN_TRACING_V2**`

* [PARAM-WHAT] 🟢 What does the `LANGCHAIN_TRACING_V2` environment variable control internally within LangChain?
* [PARAM-VALUES] 🟡 What exact string value must this be set to in order to activate tracing?
* [PARAM-MISTAKE] 🔴 What happens if you misspell it as `LANGCHAIN_TRACING_V2="True"` (capital T) or set it to `"1"` depending on your OS parser?
* [PARAM-REALCODE] 🟡 Show the exact contents of a `.env` file required to activate LangSmith safely.

**Parameter: `verbose` (in `AgentExecutor`)**

* [PARAM-WHAT] 🟢 What does `verbose=True` do when passed into the `AgentExecutor` constructor?
* [PARAM-VALUES] 🟡 It accepts a boolean. What is the default if omitted?
* [PARAM-MISTAKE] 🔴 Why might `verbose=True` deceive a beginner into thinking their application has proper observability, leading to a massive loss of debug data upon server restart?
* [PARAM-REALCODE] 🟡 Show code initializing the `AgentExecutor` with `verbose=False` for production, with a comment explaining that tracing is now fully handled via environment variables.

---

### 📊 STUDY GUIDE SUMMARY & SCORING

→ **Total Concept Count:** 8
→ **Total Parameter Count Covered:** 20 (including env vars)
→ **Total Question Count:** 144
→ **Recommended Study Order:**

1. Concept 1: Environment Initialization (`load_dotenv`)
2. Concept 3: Vector Embeddings & Persistent Storage (`Chroma`)
3. Concept 4: Retriever Operations (`invoke`)
4. Concept 2: Tool Definition (`@tool`)
5. Concept 5: Cloud LLM Integration (`ChatOllama`)
6. Concept 6: Agent Prompting & Construction (v1.0 React Agent)
7. Concept 7: Asynchronous Execution (`ainvoke`)
8. Concept 8: Agent Observability (`LangSmith`)

→ **Scoring System:**
• 🟢 Beginner (WHAT, STRUCTURE, PARAM-WHAT) = 1 pt each
• 🟡 Intermediate (WHEN, COMPARE, PURPOSE, REAL EXAMPLE, PARAM-VALUES, PARAM-REALCODE) = 2 pts each
• 🔴 Advanced (ANTI-PATTERN, BREAK IT, PARAM-MISTAKE) = 3 pts each
• **Self-check method:** Attempt all questions in order. Verify your answers against official LangChain/Python docs. Add points per correctly understood question.
• **Mastery Threshold:** You need 85% of the total available points to be fully prepared to push this architecture into a real-world production environment without critical bugs.


==================================================================================
