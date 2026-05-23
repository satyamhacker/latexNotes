

# Section 13: Understanding EvaluatingTesting of LLM Application


### 🗺️ DEPENDENCY MAP

**Concept 1: LLM Evaluation Fundamentals** → no dependencies (start here)
**Concept 2: Traditional NLP Metrics (BLEU/ROUGE)** → needs Concept 1
**Concept 3: Non-Traditional Metrics (BERTScore & Perplexity)** → needs Concept 2
**Concept 4: LLM-Based Scoring (Teacher-Student)** → needs Concept 3
**Concept 5: Evaluation Frameworks (OpenAI Evals vs Ragas)** → needs Concept 4
**Concept 6: Ragas Core Metrics** → needs Concept 5
**Concept 7: Ragas with Local LLM (Ollama & Wrappers)** → needs Concept 5 + Concept 6
**Concept 8: Multi-turn Samples & Tool Messages** → needs Concept 7

---

⚠️ *Since this material contains 8 dense concepts with extensive parameters and code components, I am splitting the output into chunks to ensure zero details are missed. Here is Batch 1 (Concepts 1 to 4).*

---

### CONCEPT 1 — LLM Evaluation Fundamentals [Beginner]

📌 Prerequisites: None (start here)

── PART A: CONCEPT-LEVEL QUESTIONS ──

[WHAT] 🟢 What is LLM Evaluation? Define it in simple words.
[STRUCTURE] 🟢 What are the mandatory components (like benchmarks, test data) required to set up an LLM evaluation pipeline? What goes inside each one? Show the minimal conceptual workflow.
[WHEN] 🟡 When should I use standard LLM evaluation datasets? Give 3 real-world situations/triggers. Also tell me: when should I NOT use them and rely on unit tests instead?
[COMPARE] 🟡 How is LLM Evaluation different from traditional deterministic Software Unit Testing? Make a clear side-by-side comparison table covering: input type, output predictability, metrics used, and when to use.
[PURPOSE] 🟡 If LLM Benchmarks didn't exist, what exact problem would I face when deploying an AI app? Why was evaluation created in the first place?
[ANTI-PATTERN] 🔴 What is the wrong way to evaluate an LLM in a CI/CD pipeline? What common mistake do beginners make regarding exact string matches? What is the correct approach instead?
[REAL EXAMPLE] 🟡 Give a real-world scenario (like a LangChain document-qa bot) where LLM evaluation is used. Show exactly how it fits into the system architecture alongside standard unit tests.
[BREAK IT] 🔴 What can go wrong if an LLM is trained heavily on benchmarks but not tested on real-world scenarios? What exact failure or silent bug will I see in production? What is the root cause and fix?

── PART B: PARAMETER DEEP-DIVE QUESTIONS ──
*(No code-level parameters for this purely theoretical concept. Proceeding to Concept 2).*

---

### CONCEPT 2 — Traditional NLP Metrics [Beginner]

📌 Prerequisites: Concept 1

── PART A: CONCEPT-LEVEL QUESTIONS ──

[WHAT] 🟢 What are Traditional NLP Metrics (Exact Match, BLEU, ROUGE, F1)? Define them in simple words.
[STRUCTURE] 🟢 What are the mandatory text inputs required to calculate these metrics? What goes inside the calculation formula? Show the minimal conceptual structure.
[WHEN] 🟡 When should I use BLEU vs ROUGE? Give 3 real-world situations/triggers for each. Also tell me: when should I NOT use traditional metrics at all?
[COMPARE] 🟡 How is BLEU different from ROUGE? Make a clear side-by-side comparison table covering: precision focus vs recall focus, primary use case (translation vs summarization), and limitations.
[PURPOSE] 🟡 If automated metrics like BLEU/ROUGE didn't exist, what exact problem would I face when training early NLP models? Why were they created in the first place?
[ANTI-PATTERN] 🔴 What is the wrong way to use traditional metrics on modern generative LLMs? What common mistake do beginners make when checking synonyms? What is the correct approach instead?
[REAL EXAMPLE] 🟡 Give a real-world scenario (like building an early Google Translate engine) where BLEU is used. Show exactly how it fits into the model improvement cycle.
[BREAK IT] 🔴 What can go wrong when using Exact Match for a conversational AI? What exact error or false-negative will I see? What is the root cause and fix?

── PART B: PARAMETER DEEP-DIVE QUESTIONS ──

**Parameter 1: `ground_truth` (Reference Text)**
[PARAM-WHAT] 🟢 What is the ground truth parameter in traditional evaluation? What does it do? What happens if I don't have it?
[PARAM-VALUES] 🟡 What formats can this parameter accept? What is the default format if any? Show an example of a valid ground truth.
[PARAM-MISTAKE] 🔴 What is the most common mistake with creating a ground truth dataset? What silent evaluation bug will I get?
[PARAM-REALCODE] 🟡 Show exactly how ground truth is mathematically compared against a candidate text. Why is this specific baseline chosen?

---

### CONCEPT 3 — Non-Traditional Metrics & BERTScore [Intermediate]

📌 Prerequisites: Concept 2

── PART A: CONCEPT-LEVEL QUESTIONS ──

[WHAT] 🟢 What are Non-Traditional Metrics and BERTScore? Define them in simple words.
[STRUCTURE] 🟢 What are the mandatory components (embedding models, vector arrays) required to calculate BERTScore? What goes inside each step? Show the minimal mathematical workflow.
[WHEN] 🟡 When should I use BERTScore over Exact Match? Give 3 real-world situations/triggers. Also tell me: when should I NOT use BERTScore?
[COMPARE] 🟡 How is Cosine Similarity different from Euclidean Distance and Dot Product in semantic evaluation? Make a clear side-by-side comparison table covering: mathematical focus (angle vs magnitude), speed, and when to use.
[PURPOSE] 🟡 If embedding-based similarity didn't exist, what exact problem would I face with modern LLMs? Why was BERTScore created in the first place?
[ANTI-PATTERN] 🔴 What is the wrong way to interpret "Perplexity"? What common mistake do beginners make regarding high vs low perplexity? What is the correct approach instead?
[REAL EXAMPLE] 🟡 Give a real-world scenario (like evaluating an OpenAI RAG pipeline) where semantic evaluation is used. Show exactly how it handles synonyms and paraphrasing.
[BREAK IT] 🔴 What can go wrong if I use a general embedding model to evaluate highly specialized domain text (like medical documents)? What exact skewed score will I see? What is the root cause and fix?

── PART B: PARAMETER DEEP-DIVE QUESTIONS ──

**Parameter 1: `Perplexity` (Model Confusion Metric)**
[PARAM-WHAT] 🟢 What is the Perplexity metric? What does it measure internally? What happens if I ignore it before deploying a model?
[PARAM-VALUES] 🟡 What numerical range of values can Perplexity take? What is considered a "good" vs "bad" value? Show an example scenario for each.
[PARAM-MISTAKE] 🔴 What is the most common mistake when evaluating Perplexity? What exact production hallucination bug will I get?
[PARAM-REALCODE] 🟡 Show exactly how Perplexity dictates whether a candidate model is ready for production. Why is a specific threshold chosen?

---

### CONCEPT 4 — LLM-Based Scoring (Teacher-Student) [Intermediate]

📌 Prerequisites: Concept 3

── PART A: CONCEPT-LEVEL QUESTIONS ──

[WHAT] 🟢 What is LLM-Based Scoring (Teacher-Student / LLM-as-a-judge)? Define it in simple words.
[STRUCTURE] 🟢 What are the mandatory components (Teacher LLM instance, Student Output, Grading Prompt) required? What goes inside each one? Show the minimal LangChain code skeleton.
[WHEN] 🟡 When should I use an LLM as a judge? Give 3 real-world situations/triggers. Also tell me: when should I NOT use LLM-based scoring?
[COMPARE] 🟡 How is Factuality different from Coherence? Make a clear side-by-side comparison table covering: purpose, evaluation criteria, and how a sentence can be one but not the other.
[PURPOSE] 🟡 If Prompt-Based Evaluation didn't exist, what exact problem would I face when evaluating long-form essays or chat bots? Why was this teacher-student concept created?
[ANTI-PATTERN] 🔴 What is the wrong way to select a Teacher LLM? What common mistake do beginners make with model sizing (e.g., using Llama-7B to grade GPT-4)? What is the correct approach instead?
[REAL EXAMPLE] 🟡 Give a real-world scenario (like HuggingFace Chatbot Arena) where Ranking-Based Evaluation is used. Show exactly how it fits into the scoring system.
[BREAK IT] 🔴 What can go wrong if the Student's answer is injected directly into the Teacher's prompt without boundaries? What exact security vulnerability (Prompt Injection) will I see? What is the root cause and fix?

── PART B: PARAMETER DEEP-DIVE QUESTIONS ──

**Parameter 1: `temperature` (inside `OpenAI()` for Teacher LLM)**
[PARAM-WHAT] 🟢 What is the temperature parameter here? What does it do to the Teacher LLM? What happens if I don't pass it?
[PARAM-VALUES] 🟡 What values can temperature accept? What is the default value? Show an example of why a specific value is used for evaluation.
[PARAM-MISTAKE] 🔴 What is the most common mistake with temperature during evaluation? What exact silent bug (inconsistent grading) will I get?
[PARAM-REALCODE] 🟡 Show exactly how temperature is set in the `OpenAI()` instantiation code. Why is `0` strictly chosen here?

**Parameter 2: `eval_template` string (inside `PromptTemplate`)**
[PARAM-WHAT] 🟢 What is the eval_template? What does it structure? What happens if I make it too vague?
[PARAM-VALUES] 🟡 What syntax elements (like `{question}`, `{student_answer}`) must this template accept? [🔍 Verify from docs: LangChain PromptTemplate syntax]. Show an example of a strict grading rubric.
[PARAM-MISTAKE] 🔴 What is the most common mistake when writing an evaluation prompt? What exact hallucinated score will I get?
[PARAM-REALCODE] 🟡 Show exactly how the template is formatted and passed to `PromptTemplate.from_template()`. Why are explicit grading rules (e.g., "Score out of 10") critical here?

**Parameter 3: `chain.invoke()` arguments**
[PARAM-WHAT] 🟢 What are the dictionary keys passed to `chain.invoke()`? What do they map to? What happens if I miss one?
[PARAM-VALUES] 🟡 What data structures can these keys accept in LangChain LCEL? What is the default behavior?
[PARAM-MISTAKE] 🔴 What is the most common mistake when invoking the evaluation chain? What exact `KeyError` or mismatch will I see?
[PARAM-REALCODE] 🟡 Show exactly how the `invoke` method is called with `question` and `student_answer`. Why must these perfectly match the placeholders in the prompt template?

---

**→ Chunk 1 Complete.**
Reply **CONTINUE** for the next batch covering Concepts 5 through 8 (Ragas Framework, Ragas Metrics, Local Ollama Wrappers, and Multi-turn Sample Tool calls).

Here is Batch 2, covering the remaining concepts to complete your dependency map and curriculum.

---

### CONCEPT 5 — Evaluation Frameworks (OpenAI Evals vs Ragas) [Intermediate]

📌 Prerequisites: Concept 4

── PART A: CONCEPT-LEVEL QUESTIONS ──

[WHAT] 🟢 What is the Ragas Library? Define it in simple words and explain what "SOTA LLM assisted method" means in this context.
[STRUCTURE] 🟢 What are the mandatory components (like Registry of Evals) required to run Ragas? What goes inside the Ragas execution flow? Show the minimal conceptual architecture.
[WHEN] 🟡 When should I use Ragas over OpenAI Evals? Give 3 real-world situations/triggers. Also tell me: when should I NOT use Ragas and stick to proprietary evals?
[COMPARE] 🟡 How is an open-source framework like Ragas different from a proprietary framework like OpenAI Evals? Make a clear side-by-side comparison table covering: ecosystem lock-in, data format requirements, and custom model flexibility.
[PURPOSE] 🟡 If frameworks with automated metrics didn't exist, what exact problem would I face regarding "annotated evaluation datasets"? Why was the SOTA-assisted method created?
[ANTI-PATTERN] 🔴 What is the wrong way to evaluate a multi-model pipeline (e.g., Llama Index + Ollama)? What common ecosystem lock-in mistake do beginners make? What is the correct approach instead?
[REAL EXAMPLE] 🟡 Give a real-world enterprise RAG app scenario where Ragas is integrated into a CI/CD pipeline to track "pipeline performance". Show exactly how it gates a production deployment.
[BREAK IT] 🔴 What can go wrong if I don't use environment variables securely? What exact `AuthenticationError` will I see in Ragas? What is the root cause and fix?

── PART B: PARAMETER DEEP-DIVE QUESTIONS ──

**Parameter 1: `OPENAI_API_KEY` (Environment Variable)**
[PARAM-WHAT] 🟢 What is the `OPENAI_API_KEY` environment variable in the context of Ragas? What does it do internally? What happens if I don't set it?
[PARAM-VALUES] 🟡 What exact string format must this key hold? What is the default fallback if any? Show an example of exporting it via the terminal.
[PARAM-MISTAKE] 🔴 What is the most common and dangerous security mistake with this API key? What exact financial or access breach will I face?
[PARAM-REALCODE] 🟡 Show exactly how this parameter is set programmatically using Python's `os.environ`. Why is this preferred over hardcoding?

---

### CONCEPT 6 — Ragas Core Metrics [Intermediate]

📌 Prerequisites: Concept 5

── PART A: CONCEPT-LEVEL QUESTIONS ──

[WHAT] 🟢 What are the 4 core Ragas metrics (Context Precision, Context Recall, Faithfulness, Response Relevance)? Define each in simple words.
[STRUCTURE] 🟢 What are the mandatory logical steps Ragas uses to calculate the final Retrieval Augmented Generation Assurance Score (RAGAS score)? What goes inside the Retriever evaluation vs the Generator evaluation?
[WHEN] 🟡 When should I prioritize optimizing the "Faithfulness" metric? Give 3 real-world situations/triggers (e.g., medical/legal bots). Also tell me: when do Context Precision/Recall NOT matter?
[COMPARE] 🟡 How is Context Precision different from Context Recall? Make a clear side-by-side comparison table covering: signal-to-noise ratio, coverage, and how to fix each when they fail.
[PURPOSE] 🟡 If Ragas core metrics didn't separate retrieval from generation, what exact debugging problem would I face when a RAG bot gives a wrong answer?
[ANTI-PATTERN] 🔴 What is the wrong way to analyze a RAGAS score? What common mistake do beginners make when looking only at the overall average? What is the correct approach instead?
[REAL EXAMPLE] 🟡 Give a real-world scenario (like BloombergGPT) where "factually grounded truth" is critical. Show exactly how the Faithfulness metric safeguards the system.
[BREAK IT] 🔴 What can go wrong if Context Precision is very low (e.g., 0.2) but the LLM is highly creative? What exact type of hallucinated response will I see? What is the root cause (Vector DB tuning) and fix?

── PART B: PARAMETER DEEP-DIVE QUESTIONS ──
*(This is a conceptual metric breakdown; code parameters for running these are covered in Concept 7).*

---

### CONCEPT 7 — Ragas Implementation with Local LLM (Ollama) [Advanced]

📌 Prerequisites: Concept 5, Concept 6

── PART A: CONCEPT-LEVEL QUESTIONS ──

[WHAT] 🟢 What is a LangChain LLM Wrapper in the context of Ragas? Define it in simple words.
[STRUCTURE] 🟢 What are the mandatory classes (`ChatOllama`, `LangchainLLMWrapper`, `evaluate`) required to run Ragas locally? What goes inside each one? Show the minimal working VS Code Python skeleton.
[WHEN] 🟡 When should I use Local Large Language Models (via Ollama) for evaluation? Give 3 real-world situations/triggers. Also tell me: when should I NOT use local models and stick to Cloud APIs?
[COMPARE] 🟡 How does a local `ChatOllama` evaluation compare to native `Chat OpenAI` evaluation? Make a clear side-by-side comparison table covering: cost, data privacy, speed, and integration steps.
[PURPOSE] 🟡 If the `LangchainLLMWrapper` didn't exist, what exact problem would I face when trying to pass a LangChain model into Ragas? Why was this adapter created?
[ANTI-PATTERN] 🔴 What is the wrong way to pass an Ollama model to the Ragas `evaluate` function? What common `TypeError` do beginners get? What is the correct approach instead?
[REAL EXAMPLE] 🟡 Give a real-world scenario (like a legal-tech startup) where LangSmith traces are used alongside local Ragas evaluation. Show exactly how it provides observability.
[BREAK IT] 🔴 What can go wrong if the local Ollama server isn't running in the background? What exact `ConnectionRefusedError` will I see? What is the root cause and terminal fix?

── PART B: PARAMETER DEEP-DIVE QUESTIONS ──

**Parameter 1: `model` (inside `ChatOllama`)**
[PARAM-WHAT] 🟢 What is the `model` parameter? What does it do? What happens if I don't pass it?
[PARAM-VALUES] 🟡 What values can this parameter accept? What is the default value if any? [🔍 Verify from docs: default ChatOllama model]. Show an example of a valid local model string.
[PARAM-MISTAKE] 🔴 What is the most common mistake with this parameter? What exact error will I get if the model isn't pulled locally?
[PARAM-REALCODE] 🟡 Show exactly how this parameter is used in `ChatOllama(model="llama3")`. Why must this exactly match the model pulled via CLI?

**Parameter 2 & 3: `LANGCHAIN_TRACING_V2` & `LANGCHAIN_API_KEY` (Environment Flags)**
[PARAM-WHAT] 🟢 What are these environment variables? What do they enable in the backend (LangSmith)? What happens if I skip them?
[PARAM-VALUES] 🟡 What exact string value must `LANGCHAIN_TRACING_V2` be set to? Show an example.
[PARAM-MISTAKE] 🔴 What is the most common mistake when setting these up in a `.env` file? What exact silent failure (missing traces) will I get?
[PARAM-REALCODE] 🟡 Show exactly how these are loaded into the script. Why is observability critical for complex Ragas metrics?

**Parameter 4: `question`, `answer`, `ground_truth` (Keys in Singleton Sample Data)**
[PARAM-WHAT] 🟢 What are these specific dictionary keys? What data do they represent in a Ragas dataset? What happens if I misspell one?
[PARAM-VALUES] 🟡 What exact data types must be passed as values for these keys in Ragas (e.g., lists of strings)? Show a valid example.
[PARAM-MISTAKE] 🔴 What is the most common mistake regarding the `answer` vs `ground_truth` keys? What exact evaluation logic error will I get?
[PARAM-REALCODE] 🟡 Show exactly how a "singleton sample" dictionary is structured using these keys. Why are lists used instead of raw strings?

---

### CONCEPT 8 — Multi-turn Samples & Tool Messages [Advanced]

📌 Prerequisites: Concept 7

── PART A: CONCEPT-LEVEL QUESTIONS ──

[WHAT] 🟢 What is a Multi-turn Sample in evaluation? Define it and explain how it differs from a singleton sample.
[STRUCTURE] 🟢 What are the mandatory message classes (`HumanMessage`, `AIMessage`, `ToolMessage`) required to build a multi-turn history? What goes inside each one? Show the minimal working code skeleton.
[WHEN] 🟡 When should I evaluate using multi-turn samples? Give 3 real-world situations/triggers (e.g., AI Agents, API calling bots). Also tell me: when should I NOT use multi-turn and stick to singleton?
[COMPARE] 🟡 How is an `AIMessage` containing a tool call different from a standard text `AIMessage`? Make a clear side-by-side comparison table covering: structure, execution intent, and next step in the pipeline.
[PURPOSE] 🟡 If `ToolMessage` didn't exist, what exact problem would I face when an LLM tries to read the output of a Weather API? Why was this specific message class created?
[ANTI-PATTERN] 🔴 What is the wrong way to test an AI agent's memory? What common mistake do beginners make by only sending the last two messages to the evaluator? What is the correct approach instead?
[REAL EXAMPLE] 🟡 Give a real-world scenario (like an Expedia flight booking bot) where multi-turn evaluation is critical. Show exactly how the "reference response" and "multi score" validate the conversation logic.
[BREAK IT] 🔴 What can go wrong if I grant an AI agent tool access to a Read/Write database without strict boundaries? What exact security vulnerability (Prompt Injection) will I see? What is the root cause and fix?

── PART B: PARAMETER DEEP-DIVE QUESTIONS ──

**Parameter 1: `content` (inside `HumanMessage`, `AIMessage`, `ToolMessage`)**
[PARAM-WHAT] 🟢 What is the `content` parameter? What does it store? What happens if it is left empty in a standard text message?
[PARAM-VALUES] 🟡 What values can this accept? [🔍 Verify from docs: Can content be a list of dictionaries for multimodal data?]. Show an example of JSON stringified content in a `ToolMessage`.
[PARAM-MISTAKE] 🔴 What is the most common mistake when populating `content` for an `AIMessage` that is meant to call a tool? What silent bug will I get?
[PARAM-REALCODE] 🟡 Show exactly how `content` is used across all three message types. Why is it often left as an empty string `""` when a tool is being called?

**Parameter 2: `tool_calls` (inside `AIMessage`)**
[PARAM-WHAT] 🟢 What is the `tool_calls` parameter? What does it instruct the underlying system to do? What happens if I don't include it in an agent flow?
[PARAM-VALUES] 🟡 What is the exact list-of-dictionaries structure required here? What keys (`name`, `args`, `id`) must exist inside it? Show a valid JSON/dict example.
[PARAM-MISTAKE] 🔴 What is the most common mistake when formatting the `args` within `tool_calls`? What exact parsing error will I get?
[PARAM-REALCODE] 🟡 Show exactly how `tool_calls` is defined in an `AIMessage`. Why is the `id` field absolutely critical?

**Parameter 3: `tool_call_id` (inside `ToolMessage`)**
[PARAM-WHAT] 🟢 What is the `tool_call_id` parameter? What does it map to? What happens if I don't pass it?
[PARAM-VALUES] 🟡 What values can this accept? Show an example of how it connects to the previous step.
[PARAM-MISTAKE] 🔴 What is the most common mistake regarding `tool_call_id`? What exact `ValidationError` will I get from the LLM?
[PARAM-REALCODE] 🟡 Show exactly how `tool_call_id` in a `ToolMessage` matches the ID generated in the preceding `AIMessage`. Why does the LLM completely lose context if these don't match?

---

### 📊 CURRICULUM SUMMARY & SCORING SYSTEM

**→ Total Concept Count:** 8
**→ Total Parameter Deep-Dives:** 11 parameters/keys mapped across code boundaries.
**→ Total Question Count:** 64 Concept Questions + 44 Parameter Questions = 108 Questions.

**📚 Recommended Study Order:**

1. LLM Evaluation Fundamentals
2. Traditional NLP Metrics
3. Non-Traditional Metrics & BERTScore
4. LLM-Based Scoring (Teacher-Student)
5. Evaluation Frameworks (OpenAI Evals vs Ragas)
6. Ragas Core Metrics
7. Ragas Implementation with Local LLM (Ollama)
8. Multi-turn Samples & Tool Messages

**🏆 Scoring System for Self-Study:**

* 🟢 **Beginner Questions:** 1 pt each (43 questions) = 43 pts
* 🟡 **Intermediate Questions:** 2 pts each (43 questions) = 86 pts
* 🔴 **Advanced/Anti-pattern Questions:** 3 pts each (22 questions) = 66 pts
* **Total Possible Points:** 195 pts
* **Mastery Threshold (85%):** 165 pts

**How to self-check:**
Write the code and theoretical answers for every question above. Compare your code against the official LangChain/Ragas documentation. If your code compiles, handles the errors described, and correctly uses the hidden parameters, award yourself the points! If a parameter behaves differently than expected, look up the `[🔍 Verify from docs]` tags.

==================================================================================
