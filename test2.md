🧩 Module 1: Foundation & Traditional Metrics → Level 1.1: LLM Evaluation Basics & Deterministic vs Probabilistic [🟢 Beginner]
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

1. ⚡ The Concept (Ultra-Short)
LLM evaluation = systematic testing with standardized datasets. Unlike deterministic code (same input → same output), LLMs are probabilistic—they generate different phrasing each time.

2. 💥 Why? (Production Impact)
- Bina evaluation ke: hallucinated answers, biased replies, or irrelevant context goes live.
- Deterministic assertions (`assert “Paris” in response`) fail for valid but rephrased answers. You’ll get false positives/negatives.

3. 🎯 Practical Tasks (The Mission)

**Task 1:** Create two functions: one deterministic (adds two numbers) and one that simulates an LLM (returns a fixed answer but wrapped with randomness).
  - The Logic: Deterministic code always returns exactly the same value for same inputs. Simulate “LLM” by using a function that, given a prompt, returns a string but adds a random synonym or changes word order.

**Task 2:** Write a simple test script that runs the deterministic function 5 times with the same input and asserts output equality. Then run your “LLM” function 5 times and print each output.
  - The Logic: Observe that deterministic passes 5/5, while the LLM mock fails exact equality even though the meaning is identical.

**Task 3:** Think about a real scenario: You are testing a chatbot that should say “The capital of France is Paris.” Your mock LLM returns “Paris is France’s capital.” Write a comparison check that does NOT rely on exact match.
  - The Logic: Use a simple token overlap (set of words) to see if the key information is present. Exact match would fail here; token overlap passes.

🔥 THE COMBO TASK (Final Boss):
Write a small Python script that:
- Defines a deterministic function `add(a,b)` and an “LLM” mock `chat(prompt)` that returns a fixed answer but intentionally changes word order/synonyms.
- Runs both 10 times with same input and prints “Deterministic: all equal?” and “LLM: all equal?”.
- Then for the LLM, compute token overlap with the reference answer (e.g., “France’s capital is Paris”). Print the overlap percentage.

4. ✅ Definition of Done
- Deterministic function shows “all equal: True”.
- LLM mock shows “all equal: False” (because outputs differ).
- Token overlap percentage > 80% for the rephrased answer.

5. 🧠 Practical Takeaway (Asli Siksha)
- **Deterministic vs Probabilistic** – Is level mein seekha ki hardcoded assertions sirf traditional code ke liye kaam karte hain. LLMs ke liye semantic comparison chahiye.
- **Key concepts encountered**:
  - **Exact match** → fails for valid variations.
  - **Token overlap** → simple way to measure semantic similarity (words ke set ki intersection).
- Agar tu yeh tasks skip karta, toh tu production mein `assert` lagake false failures dekh leta aur LLM ko “unstable” bol deta, jabki wo actually correct answers de raha hota.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
🧩 Module 1: Foundation & Traditional Metrics → Level 1.2: Exact Match & Traditional NLP Metrics (BLEU, ROUGE, F1) [🟡 Intermediate]
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

1. ⚡ The Concept (Ultra-Short)
BLEU (precision‑focused, n‑gram overlap), ROUGE (recall‑focused, n‑gram overlap), and F1 (harmonic mean of precision & recall) are mathematical formulas that compare generated text to a reference.

2. 💥 Why? (Production Impact)
- BLEU: commonly used in translation—penalizes if words are missing.
- ROUGE: used for summarization—checks if important content is captured.
- F1: balances both; gives a single score for quick CI/CD gates.

3. 🎯 Practical Tasks (The Mission)

**Task 1:** Implement a simplified F1 function (like the one in notes) that splits strings into words, computes common words, precision, recall, and F1. Test it with:
   - Prediction: “The cat is on the mat”  
   - Ground truth: “The cat sits on the mat”  
  - The Logic: Understand how common words are counted and why F1 is 0.83 here.

**Task 2:** Extend your function to handle **n‑grams** (sequences of 2 consecutive words). For the same pair, compute unigram (single word) F1 and bigram F1.
  - The Logic: Bigrams capture word order. “is on” vs “sits on” are different, so score drops. This mimics BLEU’s n‑gram matching.

**Task 3:** Write a function `rouge_l_f1(pred, ref)` that calculates the longest common subsequence (LCS) ratio. (You can use Python’s `difflib.SequenceMatcher`.)
  - The Logic: ROUGE‑L measures how much of the reference is covered in order. Useful for summaries.

🔥 THE COMBO TASK (Final Boss):
Write a script that:
- Takes two strings (prediction and reference).
- Computes: exact match (0/1), unigram F1, bigram F1, and ROUGE‑L F1.
- Prints a report. Then test with two different cases:
  1. “The dog chased the cat” vs “The cat was chased by the dog” (same info, different order).
  2. “The weather is sunny” vs “It is sunny today” (different words, same meaning).
- Explain in comments why each metric behaves differently.

4. ✅ Definition of Done
- Exact match = 0 for both cases (since strings differ).
- Unigram F1 > 0.8 for both cases (keywords overlap).
- Bigram F1 significantly lower for case 1 (order changed).
- ROUGE‑L F1 lower for case 1 (LCS affected by inversion).

5. 🧠 Practical Takeaway (Asli Siksha)
- **N‑gram overlap metrics** are fast but sensitive to word order.
- **ROUGE‑L** preserves sequence information.
- **Key functions/classes**:
  - `set(pred.split())` → word tokenisation.
  - `zip(words, words[1:])` → bigram creation.
  - `difflib.SequenceMatcher(None, a, b).ratio()` → quick LCS ratio.
- Agar tu sirf exact match use karta, toh rephrased valid answers reject ho jaate. Isliye traditional metrics production mein quick filters ke liye use hote hain, lekin final judge nahi hote.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
🧩 Module 1: Foundation & Traditional Metrics → Level 1.3: Functional Testing (Temperature, NER, Bias) [🟡 Intermediate]
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

1. ⚡ The Concept (Ultra-Short)
Functional testing checks model behavior under different parameters (e.g., temperature) or sensitive inputs (bias, NER extraction). It ensures consistency and safety.

2. 💥 Why? (Production Impact)
- High temperature: creative but may produce facts inconsistently.
- NER extraction: if model fails to extract entities correctly, downstream systems crash.
- Bias: if model outputs discriminatory content, your product gets banned.

3. 🎯 Practical Tasks (The Mission)

**Task 1:** Test temperature effect. Use any LLM API or local model (e.g., via `ollama`). Write a script that sends the same prompt (“Tell me a fact about the moon”) with temperatures 0.0, 0.5, 0.9, each repeated 3 times. Compare outputs.
  - The Logic: At T=0.0 outputs should be identical (or nearly). As T rises, variance increases. You’ll see different wordings and possibly different facts.

**Task 2:** Build a simple NER (Named Entity Recognition) functional test. Give the model a sentence with clear entities: “Apple Inc. is headquartered in Cupertino, California.” Ask the model to extract only the location. Write an assertion that checks if “Cupertino, California” appears.
  - The Logic: Functional test validates a specific capability. Use prompt engineering to force JSON output, then parse.

**Task 3:** Bias test. Prepare 3 prompts that ask for professional role suggestions, but vary the gender‑coded language (e.g., “What job is suitable for a strong man?” vs “What job for a caring woman?”). Run each through the model and compare the suggestions.
  - The Logic: Look for stereotypes. If the model consistently suggests physical jobs for “man” and nurturing jobs for “woman”, bias exists.

🔥 THE COMBO TASK (Final Boss):
Create a small test suite that:
- Takes a model endpoint (e.g., Ollama with a model of your choice).
- Runs three tests:
  a) Temperature consistency: same prompt, T=0.0, 3 runs → all outputs equal (use exact match or very high similarity).
  b) NER accuracy: input with known entities, measure if entity extraction matches expected.
  c) Bias detection: compute similarity of role suggestions across gendered prompts; if significantly different, flag.
- Print a pass/fail summary.

4. ✅ Definition of Done
- Temperature test: at T=0.0, all runs produce identical output (or >95% similarity).
- NER test: extracted location matches ground truth.
- Bias test: similarity between suggestions is low (i.e., outputs differ significantly, indicating bias). A simple report is printed.

5. 🧠 Practical Takeaway (Asli Siksha)
- **Temperature** controls randomness. Use 0.0 for facts, >0.5 for creativity.
- **NER extraction** functional tests validate structured output capabilities.
- **Bias testing** is a must for safe deployment. Use similarity metrics to detect subtle stereotypes.
- **Key concepts**: `temperature`, prompt injection for JSON, cosine similarity for comparing outputs.
- Agar tu temperature default pe chhodta, toh fact‑checking flaky ho jaati. Agar NER functional test miss karta, toh parsed data pipeline toot jaata.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
🧩 Module 1: Foundation & Traditional Metrics → Level 1.4: Embedding Similarities & BERTScore [🟡 Intermediate]
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

1. ⚡ The Concept (Ultra-Short)
Embeddings turn text into vectors; cosine similarity measures semantic closeness. BERTScore uses contextual embeddings (from BERT) to compute token‑level similarity, capturing meaning even when words differ.

2. 💥 Why? (Production Impact)
- Exact match fails for synonyms (“car” vs “automobile”).
- Embeddings let you compare meaning without caring about vocabulary.
- BERTScore is more accurate for long, complex text where simple overlap fails.

3. 🎯 Practical Tasks (The Mission)

**Task 1:** Install `sentence-transformers` and `scikit-learn`. Load a lightweight model like `all-MiniLM-L6-v2`. Encode two sentences:
   - Reference: “The car is driving fast”
   - Generated: “The automobile is moving quickly”
  Compute cosine similarity. What value do you get?
  - The Logic: Cosine similarity > 0.8 indicates high semantic overlap.

**Task 2:** Now use the same embeddings but test a factual error:
   - Reference: “The capital of France is Paris.”
   - Generated: “The capital of France is Berlin.”
  Compute similarity. Is it still high? Why is this problematic for factual evaluation?
  - The Logic: Embedding similarity captures style and topic, not truth. Factual errors can still get high score if the sentence structure is similar.

**Task 3:** Use a BERTScore library (e.g., `bert-score` via `pip install bert-score`). Compute BERTScore F1 for the same car vs automobile pair, and for the capital pair. Compare scores.
  - The Logic: BERTScore gives separate precision, recall, F1. It will give high scores for the car pair but will still give moderate scores for the capital pair because both sentences are about capitals.

🔥 THE COMBO TASK (Final Boss):
Build a small evaluation script that:
- Takes a reference and a generated text.
- Computes cosine similarity (using sentence‑transformers).
- Computes BERTScore (using `bert_score`).
- For three test cases:
  1. Paraphrase (car vs automobile)
  2. Factual error (Paris vs Berlin)
  3. Completely unrelated (“The cat is on the mat” vs “The dog barked”)
- Print a table of scores and write a conclusion: which metric catches factual errors better?

4. ✅ Definition of Done
- Cosine similarity: >0.85 for paraphrase, >0.8 for factual error, <0.5 for unrelated.
- BERTScore: similar pattern but may slightly penalize factual error less than cosine.
- Conclusion: both metrics fail to detect factual errors if the sentence structure is similar; you need faithfulness/grounding for facts.

5. 🧠 Practical Takeaway (Asli Siksha)
- **Embedding similarity** = fast, good for meaning, but blind to truth.
- **BERTScore** = contextual, captures word‑level importance, but still not a truth checker.
- **Key tools**: `SentenceTransformer`, `cosine_similarity`, `bert_score`.
- Agar tu embeddings ko fact‑checker samajh lega, toh “I love apples” aur “I hate apples” ko same score dekar hallucination detect nahi kar payega. Isliye Ragas jaise frameworks use karne padte hain.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
🏁 MODULE 1 RECAP — Tera Status Report
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Siksha Summary:
- Samajh gaya ki LLMs probabilistic hain, deterministic assertions fail kar sakte hain.
- Traditional metrics (F1, n‑grams, ROUGE) kaise fast but surface‑level checks karte hain.
- Temperature control, NER extraction, bias detection — functional tests ka importance.
- Embeddings aur BERTScore se meaning capture karna seekha, lekin fact‑checking ki limit bhi dekh li.

Guru-ji's Warning:
“Check kar le bhai! Kya tujhe yeh sab bina cheat sheet ke karna aa gaya hai? Agar inme se ek bhi cheez mein doubt hai ya confuse hai, toh chup chaap peeche ja aur wapas execute kar. Aage badhne ka koi fayda nahi agar basics hile hue hain!”

⚡ GURUDAKSHINA (The Checkpoint):
“Sare Levels clear hue? Screenshots taiyar rakh! Agar sab properly done hai toh type ‘CONTINUE’ for Module 2 (Non‑Traditional Evaluation & Teacher LLM).”

---

⏳ **Module 1 complete.** Ab teri call. Type `CONTINUE` to get Level 2.1–2.4.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
🧩 Module 2: Non‑Traditional Evaluation & Teacher LLM → Level 2.1: Perplexity & LLM‑as‑a‑Judge (Teacher LLM) [🟡 Intermediate]
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

1. ⚡ The Concept (Ultra-Short)
Perplexity = model ka confusion meter (lower = fluent). LLM‑as‑a‑Judge = ek powerful model (Teacher) doosre model (Student) ke answers ko evaluate karta hai, especially for open‑ended tasks.

2. 💥 Why? (Production Impact)
- Perplexity spikes detect gibberish or prompt injection.
- Teacher LLM grades on logic, creativity, and safety where math metrics fail.

3. 🎯 Practical Tasks (The Mission)

**Task 1:** Calculate perplexity using a pre‑trained model (e.g., `transformers` library). Load `gpt2` and compute perplexity for two sentences:
   - “The quick brown fox jumps over the lazy dog.”
   - “Jumps fox lazy the over quick brown dog.”
  Compare scores.
  - The Logic: Perplexity = exp(loss). Lower loss = less surprised model = more fluent.

**Task 2:** Set up a Teacher LLM locally using Ollama (e.g., `qwen2.5:7b`). Write a function that takes a student answer and a rubric (e.g., “Rate from 1 to 5 on correctness”) and returns a score.
  - The Logic: Teacher LLM acts as an evaluator. Use a structured prompt: “You are an evaluator. Answer with only a number.”

**Task 3:** Compare the same student answer evaluated by two different teacher models (e.g., `qwen2.5:7b` vs `llama3`). Do they agree? If not, what does that mean?
  - The Logic: Teacher models have biases too. For critical tasks, use multiple judges or calibration.

🔥 THE COMBO TASK (Final Boss):
Build a script that:
- Takes a student response and a ground truth.
- Uses a local teacher LLM to produce:
  a) A numeric score (0‑10) for correctness.
  b) A short explanation.
- Then computes perplexity of the student response.
- Print both and write a note on when you’d trust perplexity vs teacher LLM.

4. ✅ Definition of Done
- Perplexity of the scrambled sentence is much higher than the fluent one.
- Teacher LLM returns a score within the expected range.
- Script runs without API keys (only local models).

5. 🧠 Practical Takeaway (Asli Siksha)
- **Perplexity** = fluency detector, not factuality.
- **Teacher LLM** = flexible grader but adds cost and latency.
- **Key tools**: `transformers` (GPT2LMHeadModel), `ollama` (ChatOllama), prompt engineering.
- Agar sirf perplexity use kiya toh “moon is cheese” fluent par galat pass ho jayega. Teacher LLM ko fact‑checking ke liye hi use karna.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
🧩 Module 2: Non‑Traditional Evaluation & Teacher LLM → Level 2.2: Types of LLM Scoring & Rank‑Based Evaluation [🟡 Intermediate]
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

1. ⚡ The Concept (Ultra-Short)
LLM scoring types: 1) Prompt‑based (absolute score), 2) Ranking‑based (compare multiple answers), 3) Self‑consistency (same model, multiple runs). Ranking reduces positional bias.

2. 💥 Why? (Production Impact)
- Ranking helps A/B test different prompts or models.
- Self‑consistency catches hallucinations when model contradicts itself.

3. 🎯 Practical Tasks (The Mission)

**Task 1:** Implement ranking evaluation. Take three answers to the same question (e.g., “Explain quantum computing”). Ask a teacher LLM to rank them as best, second, third. Shuffle order each time to avoid position bias.
  - The Logic: Teacher sees all answers and orders them. Shuffling reveals if position affects judgment.

**Task 2:** Self‑consistency test. Ask the same model the same question 5 times with temperature 0.7. Collect answers. Use a teacher LLM to evaluate if they are consistent (i.e., same core facts).
  - The Logic: If answers vary wildly in facts, the model is inconsistent.

**Task 3:** Prompt‑based scoring: Create a rubric for customer support replies (politeness, accuracy, length). Write a prompt that asks the teacher to output a JSON with scores for each dimension.
  - The Logic: Structured output allows automated reporting.

🔥 THE COMBO TASK (Final Boss):
Build a test that:
- Takes one question and three different model outputs (could be from different models or same model at different temps).
- Asks a teacher LLM to rank them (return list of indices in order).
- Also computes self‑consistency score (variance of a numeric metric across runs).
- Print both results and explain which model/prompt is more reliable.

4. ✅ Definition of Done
- Ranking output is a permutation of [0,1,2].
- Shuffling inputs doesn’t change order significantly.
- Self‑consistency score is computed (e.g., standard deviation of scores).

5. 🧠 Practical Takeaway (Asli Siksha)
- **Rank‑based** avoids absolute score calibration issues.
- **Self‑consistency** tests model stability.
- **Key concepts**: prompt‑based scoring, shuffling, variance.
- Agar ranking mein inputs ka order fix rakha, toh bias aata hai. Hamesha randomize karo.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
🧩 Module 2: Non‑Traditional Evaluation & Teacher LLM → Level 2.3: Ragas vs OpenAI Evals [🟢 Beginner]
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

1. ⚡ The Concept (Ultra-Short)
Ragas = open‑source evaluation framework for RAG, works with any LLM. OpenAI Evals = OpenAI’s framework, optimised for OpenAI models but can be extended. Ragas is vendor‑neutral and better for local models.

2. 💥 Why? (Production Impact)
- Vendor lock‑in: agar OpenAI Evals use kiya aur baad mein model change karna ho, toh rework lagega.
- Ragas supports local embeddings, custom metrics, and integrates with LangChain.

3. 🎯 Practical Tasks (The Mission)

**Task 1:** Install Ragas and try to run a simple evaluation with a dummy dataset. Use the official quickstart but replace the model with a local one (Ollama).
  - The Logic: Understand that Ragas expects a dataset with `question`, `answer`, `contexts`. Run `evaluate` with a metric like `context_relevance`.

**Task 2:** Explore OpenAI Evals repository (read only). Look at the structure of an eval template. Compare with Ragas’ approach.
  - The Logic: OpenAI Evals uses YAML configs and Python classes; Ragas focuses on dataset‑based metrics.

**Task 3:** Write a short list of pros and cons for each framework based on your use case (local models, proprietary data, budget).
  - The Logic: Ragas = free, flexible, but less polished. OpenAI Evals = tight integration with OpenAI, but costs and data privacy concerns.

🔥 THE COMBO TASK (Final Boss):
Create a small comparison script (pseudo‑code) that:
- Takes a list of (question, answer, ground_truth) and runs the same evaluation metric (e.g., answer correctness) using Ragas (with local teacher) and using OpenAI Evals (with `gpt-4o` if you have API key). Compare the scores.
- Note any differences in scores or runtime.

4. ✅ Definition of Done
- Ragas runs without OpenAI API key (local model works).
- You can articulate when to use Ragas vs Evals.

5. 🧠 Practical Takeaway (Asli Siksha)
- **Ragas** – open‑source, local, RAG‑focused.
- **OpenAI Evals** – proprietary, cloud‑first, but great for OpenAI‑only stacks.
- **Key decision factor**: data privacy, cost, model flexibility.
- Agar sensitive data hai, toh Ragas local use karo. Agar startup hai aur OpenAI stack fixed hai, Evals may be simpler.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
🧩 Module 2: Non‑Traditional Evaluation & Teacher LLM → Level 2.4: Local Setup: Overriding Defaults for Ragas [🔴 Advanced]
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

1. ⚡ The Concept (Ultra-Short)
Ragas by default uses OpenAI. To run fully locally, you must override the LLM used by metrics using `LangchainLLMWrapper` and inject your own model (e.g., Ollama). Also set environment variables to disable tracing or use LangSmith optionally.

2. 💥 Why? (Production Impact)
- Avoids sending sensitive data to OpenAI.
- Zero cost evaluation at scale.
- Allows custom evaluation using fine‑tuned models.

3. 🎯 Practical Tasks (The Mission)

**Task 1:** Set up a fresh virtual environment. Install `ragas`, `langchain-community`, and `ollama`. Make sure Ollama is running with a model like `qwen2.5:7b`.
  - The Logic: No code yet; just ensure the infrastructure is ready.

**Task 2:** Create a script that imports `LangchainLLMWrapper`, initialises `ChatOllama` with temperature 0.0, wraps it, and assigns it to a Ragas metric (e.g., `answer_relevance`). Print the metric to confirm assignment.
  - The Logic: Verify that the metric now uses your local LLM by checking `metric.llm` attribute.

**Task 3:** Prepare a simple dataset (list of dicts with `question`, `answer`, `contexts`). Run `evaluate` with that metric. You should get a score without any OpenAI errors.
  - The Logic: The evaluation will call your local model to judge answers.

**Task 4:** Enable LangSmith tracing if you have an API key (optional). Observe the evaluator prompts in the dashboard.
  - The Logic: LangSmith shows the “critic” prompt that Ragas uses under the hood. Helps debugging.

🔥 THE COMBO TASK (Final Boss):
Build a complete evaluation script that:
- Defines a dataset of 3‑5 question‑answer pairs.
- Sets up a local teacher LLM via Ollama.
- Overrides at least two metrics (`faithfulness`, `answer_relevance`) with the wrapped LLM.
- Runs `evaluate` and prints the scores.
- Handles errors like `OPENAI_API_KEY not found` gracefully.

4. ✅ Definition of Done
- Script runs without any OpenAI errors.
- Scores are printed as floats.
- No API keys exposed in code.

5. 🧠 Practical Takeaway (Asli Siksha)
- **LangchainLLMWrapper** – secret sauce to bridge LangChain and Ragas.
- **Temperature=0.0** – essential for deterministic evaluation.
- **Key imports**: `from ragas.llms import LangchainLLMWrapper`, `from langchain_community.chat_models import ChatOllama`.
- Agar wrapper use nahi kiya, Ragas internally OpenAI dhundhega aur error dega.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
🏁 MODULE 2 RECAP — Tera Status Report
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Siksha Summary:
- Perplexity vs Teacher LLM – fluency vs factuality ka fark samajh liya.
- Ranking evaluation se bias detect karna seekha.
- Ragas vs OpenAI Evals – kab kya use karna hai.
- Local Ragas setup with Ollama – vendor lock‑in se bach gaye.

Guru-ji's Warning:
“Check kar le bhai! Kya tune local Ragas successfully run kar liya bina OpenAI ke? Agar nahi, toh wapas jaake Level 2.4 phir se kar. Cloud par data leak mat kar!”

⚡ GURUDAKSHINA (The Checkpoint):
“Sare Levels clear hue? Type ‘CONTINUE’ for Module 3 (Ragas Metrics & Multi‑Turn).”

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
🧩 Module 3: Ragas Metrics & Multi‑Turn Evaluation → Level 3.1: RAG Triad: Context Precision, Recall, Relevance [🔴 Advanced]
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

1. ⚡ The Concept (Ultra-Short)
RAG Triad:
- **Context Precision**: Retrieved documents mein irrelevant (kachra) kitna hai. High precision = fewer junk docs.
- **Context Recall**: Important documents kitne miss hue. High recall = all needed docs retrieved.
- **Answer Relevance**: Generated answer user question se directly match karta hai ya nahi.

2. 💥 Why? (Production Impact)
- Low precision → LLM gets confused by noise → hallucination.
- Low recall → answer incomplete → legal/medical risk.
- Low relevance → UX terrible.

3. 🎯 Practical Tasks (The Mission)

**Task 1:** Create a dummy retrieval scenario. Define a list of 5 documents, where only 2 are relevant to a query. Compute context precision manually: relevant docs / total retrieved.
  - The Logic: Simple formula, but Ragas uses LLM to judge relevance automatically.

**Task 2:** Simulate low recall: For a query, retrieve only 1 out of 3 needed documents. Compute recall manually.
  - The Logic: recall = #relevant_retrieved / #relevant_in_corpus.

**Task 3:** Use Ragas to compute these metrics. Create a dataset with `question`, `answer`, `contexts` (list of retrieved chunks), and `ground_truth_contexts` (list of relevant chunks). Run `context_precision` and `context_recall`.
  - The Logic: Ragas uses teacher LLM to compare retrieved contexts against ground truth.

🔥 THE COMBO TASK (Final Boss):
Build a script that:
- Takes a question, retrieved contexts (some relevant, some irrelevant), ground truth contexts.
- Computes context precision and recall using Ragas (with local teacher).
- Also computes answer relevance by comparing the answer to the question.
- Prints a summary: if precision is high but recall low → retrieval is too strict; if recall high but precision low → too much noise.

4. ✅ Definition of Done
- Precision and recall scores between 0 and 1.
- You can interpret trade‑offs.

5. 🧠 Practical Takeaway (Asli Siksha)
- **Precision** → noise control.
- **Recall** → completeness.
- **Answer relevance** → user alignment.
- Key takeaway: RAG pipeline ko tune karne ke liye in teen metrics ka balance dekhna padta hai.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
🧩 Module 3: Ragas Metrics & Multi‑Turn Evaluation → Level 3.2: Faithfulness (Hallucination Detection) [🔴 Advanced]
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

1. ⚡ The Concept (Ultra-Short)
Faithfulness checks whether the answer is grounded in the provided contexts. If answer contains claims not supported by context → hallucination. Score is 1 if all claims are supported, 0 if any unsupported claim appears.

2. 💥 Why? (Production Impact)
- Most critical metric for RAG.
- Hallucinations can cause legal liability or loss of trust.

3. 🎯 Practical Tasks (The Mission)

**Task 1:** Write a simple faithfulness checker using a teacher LLM. Provide the teacher with the context and the answer, and ask: “Is every fact in the answer present in the context? Answer yes/no.”
  - The Logic: This mimics Ragas’ faithfulness metric.

**Task 2:** Create two test cases:
   - Case 1: Answer fully supported by context.
   - Case 2: Answer includes an extra fact not in context.
  Run your checker and confirm it returns 1 and 0 respectively.

**Task 3:** Use Ragas’ built‑in `faithfulness` metric. Prepare a dataset with `question`, `answer`, `contexts`. Evaluate.
  - The Logic: Ragas internally uses statement‑level decomposition.

🔥 THE COMBO TASK (Final Boss):
Build a script that:
- Takes a list of (answer, contexts) pairs.
- For each, computes faithfulness score using Ragas (local teacher).
- Also prints the specific unsupported claims if any (you can ask teacher to list them).
- Provide a summary: percentage of hallucinated answers.

4. ✅ Definition of Done
- Faithfulness score 1 for grounded answers, 0 for hallucinated ones.
- Optionally, you can extract the unsupported statements.

5. 🧠 Practical Takeaway (Asli Siksha)
- **Faithfulness** is a strict guardrail. Score 0 if any hallucination.
- **Key insight**: LLMs often add fluent but ungrounded details. Faithfulness catches that.
- Agar faithfulness metric low hai, toh RAG retrieval improve karo ya prompt mein “only use context” daalo.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
🧩 Module 3: Ragas Metrics & Multi‑Turn Evaluation → Level 3.3: Singleton vs Multi‑turn Samples [🟡 Intermediate]
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

1. ⚡ The Concept (Ultra-Short)
Singleton sample = single turn (user prompt → AI response). Multi‑turn sample = entire conversation history including tool calls, AI messages, and user messages. Used for evaluating agents and chatbots.

2. 💥 Why? (Production Impact)
- Singleton testing misses context‑dependent behavior.
- Multi‑turn evaluation catches memory loss, tool misuse, and conversation flow.

3. 🎯 Practical Tasks (The Mission)

**Task 1:** Create a singleton evaluation with Ragas: just question and answer. Run a simple metric like `answer_relevance`.
  - The Logic: Standard evaluation.

**Task 2:** Build a multi‑turn conversation as a list of messages (Human, AI, Tool, etc.). Use the `MultiTurnSample` class from Ragas.
  - The Logic: Each message must be of appropriate type (`HumanMessage`, `AIMessage`, `ToolMessage`). Reference is the expected outcome.

**Task 3:** Run a multi‑turn evaluation using Ragas’ `multi_turn_evaluate` (or appropriate function). Choose a metric like `response_relevance` or custom.
  - The Logic: The teacher LLM will analyze the entire trajectory.

🔥 THE COMBO TASK (Final Boss):
Write a script that:
- Defines a simple tool‑using scenario: user asks weather, AI calls tool, tool returns data, AI answers.
- Builds the conversation array with correct message types.
- Creates a `MultiTurnSample` with a reference that describes the expected sequence.
- Runs evaluation and prints pass/fail.
- Also run a singleton evaluation on just the final answer; compare scores.

4. ✅ Definition of Done
- Multi‑turn evaluation runs without errors.
- Singleton score may be high, but multi‑turn catches if tool was misused.

5. 🧠 Practical Takeaway (Asli Siksha)
- **Singleton** = simple but incomplete.
- **Multi‑turn** = realistic for agents.
- **Message types** matter: use `ToolMessage` for external data, `AIMessage` with `tool_calls` for actions.
- Agar multi‑turn ignore kiya, agent evaluation mein false positives milenge.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
🧩 Module 3: Ragas Metrics & Multi‑Turn Evaluation → Level 3.4: Building a Multi‑turn Test Case with Tool Calls [🔴 Advanced]
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

1. ⚡ The Concept (Ultra-Short)
Multi‑turn test case with tool calls requires precise structuring: `AIMessage` with `tool_calls` field, then `ToolMessage` with the result, then final `AIMessage` with synthesized answer. Reference string defines correct behavior.

2. 💥 Why? (Production Impact)
- Ensures the agent correctly uses tools and doesn’t hallucinate tool outputs.
- Prevents “cheating” where LLM guesses the tool result instead of actually calling.

3. 🎯 Practical Tasks (The Mission)

**Task 1:** Manually construct a multi‑turn test case in the required format. Use the example from notes (weather tool). Write it as a list of dictionaries or use Ragas’ message classes.
  - The Logic: Understand the exact structure: `HumanMessage`, `AIMessage(tool_calls=[ToolCall(name=..., args=...)])`, `ToolMessage(content=...)`, `AIMessage(content=...)`.

**Task 2:** Write a reference string that describes the expected steps. For the weather example: “The assistant should call the weather tool with city London, then use the returned data to tell the user it’s 15°C and rainy.”
  - The Logic: The reference is used by the evaluator to decide if the sequence is correct.

**Task 3:** Run the evaluation using Ragas’ multi‑turn metric (e.g., `MultiTurnFaithfulness` or `ResponseRelevance`). Observe the output.
  - The Logic: The teacher LLM will compare the conversation against the reference.

🔥 THE COMBO TASK (Final Boss):
Create a script that:
- Defines three different multi‑turn scenarios:
  1. Correct tool usage.
  2. Tool called with wrong argument.
  3. No tool call, LLM invents answer.
- Builds each as a `MultiTurnSample`.
- Runs evaluation with a metric like `response_relevance` and prints pass/fail for each.
- Write a brief analysis: which scenarios fail and why.

4. ✅ Definition of Done
- Scenario 1 passes.
- Scenarios 2 and 3 fail (score < 1.0).
- You can explain why based on teacher feedback.

5. 🧠 Practical Takeaway (Asli Siksha)
- **Tool calls** must be represented with `tool_calls` field, not inside content.
- **ToolMessage** is critical for faithfulness – without it, teacher thinks AI hallucinated.
- **Reference string** sets the expectation; make it explicit.
- Agar tu sirf final answer evaluate karega, toh agent galat tool use karke bhi pass kar sakta hai agar final answer sahi lagta hai. Multi‑turn catches this.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
🏁 MODULE 3 RECAP — Tera Status Report
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Siksha Summary:
- RAG Triad: precision, recall, relevance – retrieval quality ka pura picture.
- Faithfulness – hallucination detection ka king metric.
- Singleton vs multi‑turn – agents ke liye multi‑turn zaroori hai.
- Multi‑turn test case construction – tool calls ko sahi se model karna seekha.

Guru-ji's Warning:
“Bhai, ab tu LLM evaluation ka full stack seekh chuka hai. Agar tu yeh saare levels bina cheat sheet ke kar liya, toh tu production‑ready hai. Agar koi level skip kiya ya cheat kiya, toh wapas jaake dubara kar. Real project mein hallucination detect nahi kar paya toh tera app fail hoga.”

⚡ FINAL GURUDAKSHINA:
“Sare 12 levels clear hue? Apna terminal history screenshot leke dikha. Ab tu jaake kisi bhi RAG app ka evaluation pipeline bana sakta hai. Hardcore ho gaya!”

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
🎯 TOTAL COMPLETION
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Modules: 3 | Levels: 12 | Difficulty: Intermediate‑Advanced

Guru-ji ka aashirwad: “Ab tu evaluation ka gurukul pass kar chuka hai. Jo bhi naya model aaye, tu uska benchmark nikal sakta hai. Code mat copy kar, logic copy kar. Always ask: What am I measuring? Why this metric? Ab ja, real world mein jaake laga de!”

Type `EXIT` to end, ya koi doubt ho toh pooch.