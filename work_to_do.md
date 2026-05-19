# Section 10: Tools and Function Calling with LLMs

### 🗺️ DEPENDENCY MAP

* **Concept 1: LLM Tooling & Context Cutoff** → no dependencies (start here)
* **Concept 2: `DuckDuckGoSearchRun**` → needs Concept 1
* **Concept 3: `WikipediaAPIWrapper**` → needs Concept 1
* **Concept 4: `WikipediaQueryRun**` → needs Concept 3
* **Concept 5: `@tool` Decorator** → needs Concept 1
* **Concept 6: `StructuredTool` (JSON Schema)** → needs Concept 5
* **Concept 7: `ChatOllama` & Model Selection** → needs Concept 1
* **Concept 8: `bind_tools()` Method** → needs Concept 6, Concept 7
* **Concept 9: `AIMessage.tool_calls` Property** → needs Concept 8
* **Concept 10: `ToolMessage` & Execution Pipeline** → needs Concept 9
* **Concept 11: `invoke()` vs `run()` Methods** → needs Concept 5
* **Concept 12: `LangSmith` (Observability/Tracing)** → needs Concept 10

---

### CONCEPT 1 — LLM Tooling & Context Cutoff [Beginner]

📌 Prerequisites: None (start here)

#### ── PART A: CONCEPT-LEVEL QUESTIONS ──

[WHAT] 🟢 What exactly is LLM Tooling, and what fundamental limitation of LLMs does it solve?
[STRUCTURE] 🟢 What is the high-level architecture/flow of a tool-enabled LLM request from the user prompt to the final summarized answer?
[WHEN] 🟡 What are 3 specific real-world triggers where an LLM *must* use a tool? Conversely, when is it an architectural mistake to trigger a tool?
[COMPARE] 🟡 How does relying on an LLM's internal knowledge differ from using a Tool in terms of latency, cost, and hallucination risk? Create a comparison table.
[PURPOSE] 🟡 If tool-calling capabilities didn't exist in modern LLMs, what exact problem would developers face when building applications like stock market bots?
[ANTI-PATTERN] 🔴 What is the "Free Tool Production" anti-pattern mentioned in the notes? Why is it dangerous?
[REAL EXAMPLE] 🟡 Walk me through exactly how a data analysis company uses a "code interpreter" tool to process user-uploaded Excel files.
[BREAK IT] 🔴 If you give an LLM an unrestricted code execution tool or Gmail toolkit without a "Human-in-the-loop", what exact security disaster (involving prompt injection) can occur?

#### ── PART B: PARAMETER DEEP-DIVE QUESTIONS ──

*(No specific configuration parameters for this abstract concept. Moving to concrete implementations.)*

---

### CONCEPT 2 — `DuckDuckGoSearchRun` [Beginner]

📌 Prerequisites: Concept 1

#### ── PART A: CONCEPT-LEVEL QUESTIONS ──

[WHAT] 🟢 What is the `DuckDuckGoSearchRun` class in `langchain_community.tools`?
[STRUCTURE] 🟢 What is the minimal Python code required to import, initialize, and execute this specific tool?
[WHEN] 🟡 When should a developer choose this tool over a paid alternative like Bing Search?
[COMPARE] 🟡 Compare `DuckDuckGoSearchRun` vs. `Bing / Google Search Tool` in a table covering: API Key requirements, reliability/rate limits, and production-readiness.
[PURPOSE] 🟡 Why does this tool exist in the LangChain community library instead of forcing developers to write their own web scraping scripts?
[ANTI-PATTERN] 🔴 What is the common mistake beginners make when deploying this specific tool to a live, high-traffic production environment?
[REAL EXAMPLE] 🟡 Show how this tool fits into a simple CLI-based AI agent that answers quick daily trivia questions for local testing.
[BREAK IT] 🔴 What exact errors (`RateLimitError` or `ConnectionRefusedError`) will I see if I hit this tool too fast? What is the root cause and the immediate fix?

#### ── PART B: PARAMETER DEEP-DIVE QUESTIONS ──

**Parameter: `query` (passed to `.invoke()`)**
[PARAM-WHAT] 🟢 What is the `query` argument? What happens if I pass an empty string?
[PARAM-VALUES] 🟡 What values/formats does this accept? Can I pass a JSON object, or must it be a plain string?
[PARAM-MISTAKE] 🔴 What happens if the query string is too long or contains complex, non-searchable programming syntax?
[PARAM-REALCODE] 🟡 Show a real code snippet using `.invoke()` with a properly formatted query string for finding recent election results.

**Parameter: `[🔍 Verify from docs] kwargs for __init__**`
[PARAM-WHAT] 🟢 Are there any hidden initialization parameters for `DuckDuckGoSearchRun` to control safe search or regional results?
[PARAM-VALUES] 🟡 What are the accepted values for these hidden configuration parameters?
[PARAM-MISTAKE] 🔴 What is the silent bug if I ignore regional search parameters when building an app for a specific country?
[PARAM-REALCODE] 🟡 Show how to initialize this class with specific strict-search parameters (if they exist in the official docs).

---

### CONCEPT 3 — `WikipediaAPIWrapper` [Intermediate]

📌 Prerequisites: Concept 1

#### ── PART A: CONCEPT-LEVEL QUESTIONS ──

[WHAT] 🟢 What is `WikipediaAPIWrapper` and how does it differ from a "Tool"?
[STRUCTURE] 🟢 What are the mandatory imports and setup syntax to instantiate this wrapper?
[WHEN] 🟡 Give 3 scenarios where fetching data via Wikipedia is vastly superior to using a general web search tool.
[COMPARE] 🟡 How does `WikipediaAPIWrapper` differ from `DuckDuckGoSearchRun` regarding data factuality, structure, and rate limiting?
[PURPOSE] 🟡 If this wrapper didn't exist, how much boilerplate HTTP request and HTML parsing code would a developer have to write to get the first 100 characters of a wiki article?
[ANTI-PATTERN] 🔴 Why is it an anti-pattern to pull full Wikipedia pages (without character limits) into an LLM context window?
[REAL EXAMPLE] 🟡 How does a Customer Support bot use this wrapper differently than an order-status tool when a user asks about "Avatar movie details"?
[BREAK IT] 🔴 What `ModuleNotFoundError` will crash my code immediately if I only install `langchain-community`, and what is the exact terminal command to fix it?

#### ── PART B: PARAMETER DEEP-DIVE QUESTIONS ──

**Parameter: `top_k_results**`
[PARAM-WHAT] 🟢 What does `top_k_results` control inside the wrapper? What happens if I don't pass it?
[PARAM-VALUES] 🟡 What integer values are acceptable? What is the default?
[PARAM-MISTAKE] 🔴 What context-window overflow error might I trigger if I set this value to `10` without considering my model's token limits?
[PARAM-REALCODE] 🟡 Show a working code snippet initializing the wrapper where `top_k_results` is explicitly configured to prevent overwhelming the LLM.

**Parameter: `doc_content_chars_max**`
[PARAM-WHAT] 🟢 What exactly does `doc_content_chars_max` truncate?
[PARAM-VALUES] 🟡 What is the standard default value, and what is a realistic value for a production prompt (e.g., 100 vs 4000)?
[PARAM-MISTAKE] 🔴 What silent bug occurs if this is set too low (e.g., 50 characters) when the LLM actually needs deep historical context to answer the user?
[PARAM-REALCODE] 🟡 Show the exact Python initialization injecting this parameter. Why might a senior engineer set this dynamically based on the model being used?

**Parameter: `[🔍 Verify from docs] lang**`
[PARAM-WHAT] 🟢 Is there a `lang` parameter to fetch Wikipedia articles in languages other than English (e.g., Hindi/Spanish)?
[PARAM-VALUES] 🟡 What string formats (like 'en', 'hi') does it accept?
[PARAM-MISTAKE] 🔴 What happens if the user asks a question in Spanish, but the wrapper defaults to the English Wikipedia API?
[PARAM-REALCODE] 🟡 Show the exact code to initialize a Wikipedia wrapper strictly searching the French Wikipedia.

---

### CONCEPT 4 — `WikipediaQueryRun` [Intermediate]

📌 Prerequisites: Concept 3

#### ── PART A: CONCEPT-LEVEL QUESTIONS ──

[WHAT] 🟢 What is the exact purpose of `WikipediaQueryRun`?
[STRUCTURE] 🟢 Show the code required to bind `WikipediaAPIWrapper` inside `WikipediaQueryRun`.
[WHEN] 🟡 At what specific point in the development pipeline do you transition from using the wrapper to using this tool object?
[COMPARE] 🟡 What is the architectural difference between a "Utility/Wrapper" (like `WikipediaAPIWrapper`) and a "Tool" (like `WikipediaQueryRun`) in LangChain?
[PURPOSE] 🟡 Why can't we just pass the `WikipediaAPIWrapper` directly into the LLM's `bind_tools` method?
[ANTI-PATTERN] 🔴 What happens if you try to pass raw text into this tool's `.invoke()` method instead of the expected dictionary format in newer LangChain versions?
[REAL EXAMPLE] 🟡 Show how this tool is placed inside a `tool_array` list alongside custom tools.
[BREAK IT] 🔴 What validation error is thrown if the LLM attempts to pass multiple arguments to this tool when it only expects one?

#### ── PART B: PARAMETER DEEP-DIVE QUESTIONS ──

**Parameter: `api_wrapper**`
[PARAM-WHAT] 🟢 What is the `api_wrapper` parameter inside `WikipediaQueryRun`?
[PARAM-VALUES] 🟡 Does it only accept `WikipediaAPIWrapper` instances, or can I pass other wrappers?
[PARAM-MISTAKE] 🔴 What `TypeError` or initialization failure occurs if I forget to pass the initialized wrapper and pass a raw string or nothing instead?
[PARAM-REALCODE] 🟡 Show the 2-line combination of initializing the wrapper and injecting it into the Tool object.

---

### CONCEPT 5 — The `@tool` Decorator [Advanced]

📌 Prerequisites: Concept 1

#### ── PART A: CONCEPT-LEVEL QUESTIONS ──

[WHAT] 🟢 What does the `@tool` decorator actually do to a standard Python function?
[STRUCTURE] 🟢 Show the strict syntax requirements for a custom tool: decorator placement, function definition, type hints, and docstring.
[WHEN] 🟡 Give 3 scenarios where you *must* write a custom tool rather than relying on a community tool.
[COMPARE] 🟡 Compare a standard Python function vs. an `@tool` decorated function in terms of how LangChain extracts metadata.
[PURPOSE] 🟡 If the `@tool` decorator didn't exist, how much manual JSON schema generation would a developer have to write to explain their function to an LLM?
[ANTI-PATTERN] 🔴 What is the fatal mistake regarding "vague docstrings" (e.g., `"Does math"`)?
[REAL EXAMPLE] 🟡 Write a production-ready custom `@tool` for a `check_order_status(order_id: str)` function.
[BREAK IT] 🔴 What `ValidationError` or execution bug will occur if you omit Python type hints (`a: int`) in your function parameters?

#### ── PART B: PARAMETER DEEP-DIVE QUESTIONS ──

**"Parameter": `docstring` (The internal description property)**
[PARAM-WHAT] 🟢 How does the LLM use the Python docstring inside an `@tool`? What happens if you leave it completely blank?
[PARAM-VALUES] 🟡 What makes a "high-quality" value for this string? What should be explicitly stated?
[PARAM-MISTAKE] 🔴 What is the exact silent failure if the description is too generic and conflicts with another tool in the toolkit?
[PARAM-REALCODE] 🟡 Show a perfectly crafted docstring for a `delete_database_record` tool that strictly guides the LLM's behavior.

**"Parameter": `type_hints` (e.g., `a: int`, `-> int`)**
[PARAM-WHAT] 🟢 Why are type hints not just "good practice" but *mandatory* for the `@tool` decorator?
[PARAM-VALUES] 🟡 Can you use complex Pydantic models here, or only primitive types like `int` and `str`? `[🔍 Verify from docs]`
[PARAM-MISTAKE] 🔴 What happens to the generated JSON Function Schema if you omit the return type hint (`-> int`)?
[PARAM-REALCODE] 🟡 Show a custom tool signature that accepts a complex dictionary or List as an argument using strict typing.

---

**⚠️ STATUS CHECK:** We have covered 5 major concepts, extracting multiple classes, decorators, and deep-diving into 7 specific parameters/configurations.

**Reply "CONTINUE" to generate the next batch:** `StructuredTool`, `ChatOllama (Model compatibility)`, `bind_tools()`, and the `tool_calls` execution pipeline.

### CONCEPT 6 — `StructuredTool` (JSON Schema) [Intermediate]

📌 Prerequisites: Concept 5

#### ── PART A: CONCEPT-LEVEL QUESTIONS ──

[WHAT] 🟢 What is a `StructuredTool` in the context of LangChain, and how does it relate to the `@tool` decorator?
[STRUCTURE] 🟢 Show the structural representation of the JSON schema generated by a `StructuredTool`. What are its main top-level keys?
[WHEN] 🟡 When does the framework internally convert your Python function into this structured format? Does this happen at runtime or definition time?
[COMPARE] 🟡 Compare a raw Python function's memory signature vs. the `StructuredTool` JSON schema. Why is the latter the only thing an LLM can understand?
[PURPOSE] 🟡 If `StructuredTool` didn't exist, how would the LLM know exactly what arguments (and their data types) to generate for a tool call?
[ANTI-PATTERN] 🔴 Why is it a bad practice to try and manually write these JSON schemas as giant strings instead of relying on LangChain's abstractions?
[REAL EXAMPLE] 🟡 Show what the final `StructuredTool` JSON payload looks like for a `get_weather(city: str, metric: bool)` function before it gets sent to the LLM.
[BREAK IT] 🔴 If your underlying function is missing type hints, what will be missing in the `StructuredTool` schema, and how will the LLM react?

#### ── PART B: PARAMETER DEEP-DIVE QUESTIONS ──

**Key: `name**`
[PARAM-WHAT] 🟢 What does the `name` key represent in the schema? What happens if it has spaces?
[PARAM-VALUES] 🟡 What are the strict naming conventions for this string (e.g., alphanumeric, underscores)?
[PARAM-MISTAKE] 🔴 What happens if two different tools in your toolkit generate the exact same `name` value?
[PARAM-REALCODE] 🟡 Show how to explicitly override the tool `name` via the `@tool(name="custom_name")` syntax instead of using the function name.

**Key: `description**`
[PARAM-WHAT] 🟢 How is the `description` key populated in the schema?
[PARAM-VALUES] 🟡 Is there a character limit to this string? What makes an optimal value?
[PARAM-MISTAKE] 🔴 What hallucination risk increases if the `description` key is left entirely blank?
[PARAM-REALCODE] 🟡 Show how the docstring of a Python function perfectly maps to this specific JSON key in the final schema.

**Key: `args` / `args_schema**`
[PARAM-WHAT] 🟢 What is the purpose of the `args` dictionary within the schema?
[PARAM-VALUES] 🟡 How does this key represent nested objects or complex types (like Enums)?
[PARAM-MISTAKE] 🔴 What execution error occurs if the LLM ignores the types defined in `args` and passes a string instead of an expected integer?
[PARAM-REALCODE] 🟡 Show how a `Pydantic` model can be used to generate a highly robust `args_schema` for complex tool inputs. `[🔍 Verify from docs]`

---

### CONCEPT 7 — `ChatOllama` & Model Selection [Intermediate]

📌 Prerequisites: Concept 1

#### ── PART A: CONCEPT-LEVEL QUESTIONS ──

[WHAT] 🟢 What is the `ChatOllama` class, and what specific role does it play in a local tooling setup?
[STRUCTURE] 🟢 What is the required Python code to import and instantiate a `ChatOllama` object?
[WHEN] 🟡 Why would a developer choose `ChatOllama` running locally over a cloud-based provider like OpenAI's `ChatOpenAI`? Give 3 reasons.
[COMPARE] 🟡 Based on the notes, create a comparison table between Qwen 2.5/Llama 3.1 and DeepSeek R1 specifically regarding Native Tool Calling Support and Metadata returned.
[PURPOSE] 🟡 Why is model selection the most critical point of failure when building a function-calling pipeline?
[ANTI-PATTERN] 🔴 What is the "Reasoning Model Fallacy" (e.g., blindly using DeepSeek R1 for tool-calling) and why does it crash the agent?
[REAL EXAMPLE] 🟡 Walk through a scenario where a local Llama 3.1 model running via Ollama successfully parses a math question and decides to use a local Python tool.
[BREAK IT] 🔴 If you start your script but haven't actually pulled the model via the Ollama CLI terminal (`ollama run ...`), what exact connection or model-not-found error will you see?

#### ── PART B: PARAMETER DEEP-DIVE QUESTIONS ──

**Parameter: `model**`
[PARAM-WHAT] 🟢 What does the `model` parameter define? What happens if you skip it?
[PARAM-VALUES] 🟡 List 3 valid string values based on the recommended models in the notes.
[PARAM-MISTAKE] 🔴 What is the exact string formatting mistake beginners make when trying to specify model versions/tags (e.g., `qwen2.5:7b`)?
[PARAM-REALCODE] 🟡 Show the exact initialization line targeting the `qwen2.5:7b` model. Why is this specific tag chosen over the massive 72b version for local testing?

**Parameter: `[🔍 Verify from docs] temperature**`
[PARAM-WHAT] 🟢 What is the `temperature` parameter, and how does it affect tool-calling reliability?
[PARAM-VALUES] 🟡 What float values are accepted? What is the standard default?
[PARAM-MISTAKE] 🔴 What is the danger of setting `temperature=1.0` (high creativity) when you strictly need the model to output a perfectly formatted JSON `tool_call`?
[PARAM-REALCODE] 🟡 Show how to instantiate the model with a temperature explicitly set to `0.0` for deterministic tool selection.

---

### CONCEPT 8 — `bind_tools()` Method [Advanced]

📌 Prerequisites: Concept 6, Concept 7

#### ── PART A: CONCEPT-LEVEL QUESTIONS ──

[WHAT] 🟢 What does the `bind_tools()` method technically do to the LLM's API payload?
[STRUCTURE] 🟢 What is the correct syntax to bind an array of tools to an initialized LLM object?
[WHEN] 🟡 Give 3 scenarios where you should dynamically bind tools rather than permanently attaching them to the model at the start.
[COMPARE] 🟡 How does using `bind_tools()` compare to manually writing a huge system prompt saying: "Please output JSON if you want me to run a function"?
[PURPOSE] 🟡 If `bind_tools()` didn't exist in LangChain, how would developers manually pass the `StructuredTool` array to the model?
[ANTI-PATTERN] 🔴 What is the critical mistake of calling `llm.bind_tools(tools)` but ignoring the return value?
[REAL EXAMPLE] 🟡 Show how to define a list containing `wiki_tool` and `add_numbers`, and bind them to a `ChatOllama` instance.
[BREAK IT] 🔴 What error occurs if you pass a raw un-decorated Python function inside the list provided to `bind_tools()`?

#### ── PART B: PARAMETER DEEP-DIVE QUESTIONS ──

**Parameter: `tools` (positional / first argument)**
[PARAM-WHAT] 🟢 What exactly are you passing into this parameter?
[PARAM-VALUES] 🟡 Does this accept a list, a single item, or a dictionary? Can it be a mix of custom and community tools?
[PARAM-MISTAKE] 🔴 What happens if you pass an empty list `[]` to this parameter and then ask the model a question requiring external data?
[PARAM-REALCODE] 🟡 Show a snippet where a `tool_array` containing 3 different tools is passed to this parameter.

**Parameter: `[🔍 Verify from docs] tool_choice**`
[PARAM-WHAT] 🟢 What does the `tool_choice` parameter do?
[PARAM-VALUES] 🟡 What are the valid string values (e.g., "auto", "any", or a specific tool name)?
[PARAM-MISTAKE] 🔴 What is the risk of hardcoding `tool_choice="specific_tool_name"` when the user asks a completely unrelated conversational question?
[PARAM-REALCODE] 🟡 Show how to use this parameter to *force* the LLM to use the `multiply_numbers` tool regardless of the user's prompt.

---

### CONCEPT 9 — `AIMessage.tool_calls` Property [Advanced]

📌 Prerequisites: Concept 8

#### ── PART A: CONCEPT-LEVEL QUESTIONS ──

[WHAT] 🟢 What is the `tool_calls` property, and where does it live within the LLM's response object?
[STRUCTURE] 🟢 What is the data structure of `response.tool_calls`? (Is it a string, dictionary, list of dictionaries?)
[WHEN] 🟡 When does the LLM decide to populate this property instead of returning standard text content?
[COMPARE] 🟡 Compare a standard `AIMessage` containing a string `content` vs. an `AIMessage` containing populated `tool_calls`. How does the Python script treat them differently?
[PURPOSE] 🟡 Why is this returned as a structured metadata block rather than just generating a text string like `"TOOL_CALL: add_numbers(2, 2)"`?
[ANTI-PATTERN] 🔴 Why is it dangerous to assume `response.tool_calls` will always exist and immediately try to loop over it without checking?
[REAL EXAMPLE] 🟡 Show a scenario where an LLM returns a list with *multiple* tool calls simultaneously (e.g., fetching weather for both London and Tokyo).
[BREAK IT] 🔴 What exact `AttributeError` will you get if you try to access this property on an older version of LangChain, or if you forgot to run `bind_tools()`?

#### ── PART B: PARAMETER DEEP-DIVE QUESTIONS ──

**Key: `name` (inside the tool_calls dict)**
[PARAM-WHAT] 🟢 What does the `name` value represent in this metadata dictionary?
[PARAM-VALUES] 🟡 Does this name exactly match the Python function name or the overridden `@tool(name=...)` value?
[PARAM-MISTAKE] 🔴 Why does the speaker in the notes suggest using `name.lower()`? What casing hallucination problem does this solve?
[PARAM-REALCODE] 🟡 Show the basic execution logic (an `if` statement) that checks this `name` key to trigger the correct local Python function.

**Key: `args` (inside the tool_calls dict)**
[PARAM-WHAT] 🟢 What does the `args` dictionary contain?
[PARAM-VALUES] 🟡 Will the keys in this dictionary always match the parameter names defined in your custom tool's function signature?
[PARAM-MISTAKE] 🔴 What happens if the LLM hallucinates an argument that your underlying Python function doesn't accept?
[PARAM-REALCODE] 🟡 Show how to unpack the `args` dictionary dynamically when invoking the target tool using `tool.invoke(args)`.

**Key: `id` (inside the tool_calls dict)**
[PARAM-WHAT] 🟢 What is the purpose of the `id` string (e.g., `'call_1234'`)?
[PARAM-VALUES] 🟡 Who generates this ID? The LLM, LangChain, or your Python script?
[PARAM-MISTAKE] 🔴 What happens in the next step of the pipeline if you discard or lose this ID before sending the result back to the LLM?
[PARAM-REALCODE] 🟡 Show where this `id` is accessed in the response dictionary and how it looks conceptually.

---

### CONCEPT 10 — `ToolMessage` & Execution Pipeline [Advanced]

📌 Prerequisites: Concept 9

#### ── PART A: CONCEPT-LEVEL QUESTIONS ──

[WHAT] 🟢 What is a `ToolMessage`, and what role does it play in the conversational history?
[STRUCTURE] 🟢 What are the mandatory fields required to construct a valid `ToolMessage` object?
[WHEN] 🟡 At what specific moment in the execution pipeline do you instantiate a `ToolMessage`?
[COMPARE] 🟡 Compare `HumanMessage`, `AIMessage`, and `ToolMessage`. What specific "speaker role" does each represent in the prompt template?
[PURPOSE] 🟡 If we execute the tool and just print the result to the user, why must we bother creating a `ToolMessage` and sending it back to the LLM?
[ANTI-PATTERN] 🔴 What is the logical gap if you execute the tool but fail to append the resulting `ToolMessage` to the message history before querying the LLM again?
[REAL EXAMPLE] 🟡 Walk through the 3-step message history array for a travel booking bot canceling a flight (Human asks -> AI calls tool -> Python executes and creates ToolMessage -> AI confirms).
[BREAK IT] 🔴 What exact validation error will the LLM API throw if you send a `ToolMessage` that doesn't explicitly reference the `id` of the original tool call?

#### ── PART B: PARAMETER DEEP-DIVE QUESTIONS ──

**Parameter: `[🔍 Verify from docs] content` (inside ToolMessage)**
[PARAM-WHAT] 🟢 What does the `content` parameter of a `ToolMessage` hold?
[PARAM-VALUES] 🟡 Should this be a strictly formatted JSON string, or can it be plain text like `"The flight was deleted"`?
[PARAM-MISTAKE] 🔴 What happens if the tool execution crashes and you pass the raw Python stack trace string into the `content` parameter?
[PARAM-REALCODE] 🟡 Show how to capture the integer output of `add_numbers`, convert it to a string, and pass it as `content` to instantiate a `ToolMessage`.

**Parameter: `[🔍 Verify from docs] tool_call_id` (inside ToolMessage)**
[PARAM-WHAT] 🟢 Why is the `tool_call_id` parameter mandatory for a `ToolMessage`?
[PARAM-VALUES] 🟡 Where exactly do you extract the value for this parameter?
[PARAM-MISTAKE] 🔴 What conversational confusion occurs if the AI requested two tool calls simultaneously, but you return two `ToolMessage`s with mismatched or missing IDs?
[PARAM-REALCODE] 🟡 Show the exact code snippet mapping the `call["id"]` from the `AIMessage` into the initialization of the `ToolMessage`.

---

### CONCEPT 11 — `invoke()` vs `run()` Methods [Beginner]

📌 Prerequisites: Concept 5

#### ── PART A: CONCEPT-LEVEL QUESTIONS ──

[WHAT] 🟢 What is the difference between the `run()` and `invoke()` methods when executing a LangChain tool?
[STRUCTURE] 🟢 Show the syntax difference: how do you pass arguments to `.run()` vs. `.invoke()`?
[WHEN] 🟡 Why is `invoke()` now the industry standard over `run()`?
[COMPARE] 🟡 Create a comparison table for `run()` vs `invoke()` covering: Accepted input formats, Support for multiple arguments, and Deprecation status.
[PURPOSE] 🟡 Why did the older `.run()` method fail so poorly when developers tried to build complex tools requiring multiple parameters (like a mathematical `add(a, b)` function)?
[ANTI-PATTERN] 🔴 What common mistake do developers making updating legacy code when transitioning from `.run("Avatar")` to `.invoke()`?
[REAL EXAMPLE] 🟡 Show how to execute a dictionary lookup tool using `invoke` passing a dictionary containing `{"word": "ephemeral", "language": "en"}`.
[BREAK IT] 🔴 What exact error (`TypeError` or `ValidationError`) will you see if you try `add_numbers.run("2, 22")`?

#### ── PART B: PARAMETER DEEP-DIVE QUESTIONS ──

**Parameter: `input` (for `.invoke()`)**
[PARAM-WHAT] 🟢 What does the `input` parameter expect when calling `tool.invoke()`?
[PARAM-VALUES] 🟡 Must it always be a dictionary? What happens if the tool only has one argument (like Wikipedia search)?
[PARAM-MISTAKE] 🔴 What silent parsing error happens if you pass a string to `invoke()` when the tool strictly expects a JSON dictionary?
[PARAM-REALCODE] 🟡 Show exactly how the `args` dictionary extracted from `response.tool_calls` is passed directly into this `input` parameter.

---

### CONCEPT 12 — `LangSmith` (Observability/Tracing) [Intermediate]

📌 Prerequisites: Concept 10

#### ── PART A: CONCEPT-LEVEL QUESTIONS ──

[WHAT] 🟢 What is LangSmith, and what specific problem does it solve in a tooling/agentic workflow?
[STRUCTURE] 🟢 What are the standard environment variables (`.env`) required to connect a LangChain application to LangSmith?
[WHEN] 🟡 Give 3 scenarios during the "Fixing/Iteration Phase" where checking LangSmith traces is superior to reading terminal prints.
[COMPARE] 🟡 How does using LangSmith for "observability and traceability" differ from just using standard Python `logging` or `print()` statements?
[PURPOSE] 🟡 When an LLM mysteriously picks the dictionary tool instead of the map tool, how exactly does LangSmith help you find the root cause?
[ANTI-PATTERN] 🔴 Why is it an anti-pattern to deploy a complex multi-tool AI agent to production without any tracing platform enabled?
[REAL EXAMPLE] 🟡 Walk through what a developer visually sees on the LangSmith web UI when a `tool_calls` request fails due to an invalid argument.
[BREAK IT] 🔴 What happens to your LangChain application if your `LANGCHAIN_API_KEY` is invalid or expired? Does the app crash, or does it just fail to upload traces silently? `[🔍 Verify from docs]`

#### ── PART B: PARAMETER DEEP-DIVE QUESTIONS ──

*(LangSmith relies primarily on environment variables rather than direct class parameters in this context.)*

**Env Var: `LANGCHAIN_TRACING_V2**`
[PARAM-WHAT] 🟢 What does setting `LANGCHAIN_TRACING_V2="true"` actually do under the hood?
[PARAM-VALUES] 🟡 What are the valid string boolean values for this?
[PARAM-MISTAKE] 🔴 What happens if you define your API key but forget to set this specific boolean variable to true?
[PARAM-REALCODE] 🟡 Show the exact `.env` file structure to enable tracing in your project.

---

### 📊 FINAL METRICS & STUDY PLAN

→ **Total Concept Count:** 12
→ **Total Parameter Count Covered:** 17
→ **Total Question Count:** 164 (96 Concept Qs + 68 Parameter Qs)

**📚 Recommended Study Order:**

1. Concept 1: LLM Tooling & Context Cutoff
2. Concept 2: `DuckDuckGoSearchRun`
3. Concept 3: `WikipediaAPIWrapper`
4. Concept 4: `WikipediaQueryRun`
5. Concept 5: The `@tool` Decorator
6. Concept 11: `invoke()` vs `run()` Methods *(Moved up slightly as it pertains to testing tools directly)*
7. Concept 6: `StructuredTool` (JSON Schema)
8. Concept 7: `ChatOllama` & Model Selection
9. Concept 8: `bind_tools()` Method
10. Concept 9: `AIMessage.tool_calls` Property
11. Concept 10: `ToolMessage` & Execution Pipeline
12. Concept 12: `LangSmith` (Observability/Tracing)

**🏆 Scoring System:**

* 🟢 Beginner = 1 pt
* 🟡 Intermediate = 2 pts
* 🔴 Advanced = 3 pts
* **Mastery Threshold:** 85% of total points.
* **Self-check method:** Attempt all questions locally without looking at the notes. Compare with official LangChain/Ollama documentation. Add 1 point per verified correct understanding. Revisit the "Anti-Pattern" (🔴) questions if you encounter silent bugs in production!

==================================================================================
