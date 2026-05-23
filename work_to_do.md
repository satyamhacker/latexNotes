

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

