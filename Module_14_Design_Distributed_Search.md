# Module 14: Design Distributed Search (Elasticsearch & Typeahead)

## Topic 14.1: Search System Fundamentals - Inverted Index

---

## 🎯 1. Title / Topic: Inverted Index (Search Engine ka Dil)

---

## 🐣 2. Samjhane ke liye (Simple Analogy):

Inverted Index ek **Book ke end mein Index** jaisa hai. Jaise book ke last page par "Apple - Page 5, 12, 45" likha hota hai, waise hi search engine mein "Apple" word ke liye document IDs store hoti hain. Normal approach: Har document ko ek-ek karke read karo aur "Apple" dhundo (slow - 1 million documents = 1 million reads). Inverted Index approach: Seedha "Apple" ke entry par jao, saari document IDs mil jayengi (fast - 1 read). Result: Google 0.5 second mein 1 billion pages search kar leta hai.

---

## 📖 3. Technical Definition (Interview Answer):

**Inverted Index** is a data structure that maps each unique word (term) to a list of documents containing that word, enabling fast full-text search by looking up terms instead of scanning documents.

**Key terms:**
- **Term:** Unique word after processing (e.g., "running" → "run" after stemming)
- **Posting List:** Document IDs jahan ye term present hai (e.g., "apple" → [doc1, doc5, doc12])
- **Forward Index:** Document → Words mapping (normal, slow search)
- **Inverted Index:** Word → Documents mapping (reverse, fast search)
- **TF-IDF:** Term Frequency-Inverse Document Frequency (relevance scoring formula)

---

## 🧠 4. Zaroorat Kyun Hai? (Why?):

**Main Problem:** Bina Inverted Index ke, search karne ke liye har document ko sequentially read karna padega. Example: 1 million documents, har document 1KB → 1GB data scan karna padega har query ke liye (10-20 seconds).

**Business Impact:** Slow search = Bad UX = Users leave. Google ka success Inverted Index ki wajah se hai (0.5 sec mein results).

**Technical Benefits:**
- **Speed:** O(1) term lookup vs O(n) document scan (1000x faster)
- **Scalability:** Billion documents bhi fast search (index distributed across servers)
- **Relevance:** TF-IDF scoring se best results pehle (ranking)
- **Memory Efficient:** Sirf unique terms store (compression techniques)

---

## 🚫 5. Iske Bina Kya Hoga? (Failure Scenario):

**Scenario: Linear Scan (No Index)**
- Database: 10 million documents, avg size 2KB each = 20GB
- Query: "machine learning"
- Process: Har document ko read → Check if contains "machine" AND "learning" → 10M reads
- Time: 20GB / 100MB/s (disk speed) = 200 seconds (3+ minutes)
- User: Frustrated, closes tab, uses Google instead

**Real Example:** **Early Yahoo (1995)** - No proper inverted index → Search took 30+ seconds → Users switched to Google (launched 1998 with advanced inverted index) → Yahoo lost search market. Google's PageRank + Inverted Index = 0.5 sec results → Dominated search industry.

**Impact:** Without inverted index, modern search engines (Google, Elasticsearch, Amazon product search) impossible.

---

## ⚙️ 6. Under the Hood (Technical Working):

**Inverted Index Creation (Indexing Phase):**

1. **Document Ingestion:** New document aata hai (e.g., "The quick brown fox")
2. **Tokenization:** Text ko words mein split (["The", "quick", "brown", "fox"])
3. **Normalization:** Lowercase conversion (["the", "quick", "brown", "fox"])
4. **Stop Words Removal:** Common words remove (["quick", "brown", "fox"] - "the" removed)
5. **Stemming/Lemmatization:** Root form (["quick", "brown", "fox"] - already root)
6. **Index Update:** Har term ke liye document ID add
   - "quick" → [doc1, doc5, doc10, doc15]
   - "brown" → [doc1, doc8, doc15]
   - "fox" → [doc1, doc12]

**Search Query Processing:**

1. **Query Parsing:** User query "quick fox" → Tokenize → ["quick", "fox"]
2. **Index Lookup:** 
   - "quick" → [doc1, doc5, doc10, doc15]
   - "fox" → [doc1, doc12]
3. **Intersection:** Common documents (AND operation) → [doc1] (both terms present)
4. **Ranking:** TF-IDF score calculate → doc1 score = 0.85
5. **Return Results:** Sorted by score (highest first)

**ASCII Diagram (Inverted Index Structure):**

```
DOCUMENTS (Forward Index - Slow):
+-------+--------------------------------+
| Doc1  | "the quick brown fox jumps"   |
| Doc2  | "the lazy dog sleeps"          |
| Doc3  | "quick brown rabbit runs"      |
| Doc4  | "the fox hunts rabbit"         |
+-------+--------------------------------+

        ↓ ↓ ↓ (Indexing Process)

INVERTED INDEX (Fast Lookup):
+----------+------------------------+----------+
| Term     | Posting List (Doc IDs) | Freq     |
+----------+------------------------+----------+
| quick    | [Doc1, Doc3]           | 2        |
| brown    | [Doc1, Doc3]           | 2        |
| fox      | [Doc1, Doc4]           | 2        |
| jumps    | [Doc1]                 | 1        |
| lazy     | [Doc2]                 | 1        |
| dog      | [Doc2]                 | 1        |
| rabbit   | [Doc3, Doc4]           | 2        |
| hunts    | [Doc4]                 | 1        |
+----------+------------------------+----------+

SEARCH QUERY: "quick fox"
     |
     v
[Lookup "quick"] → [Doc1, Doc3]
[Lookup "fox"]   → [Doc1, Doc4]
     |
     v
[Intersection (AND)] → [Doc1] (common)
     |
     v
[Ranking (TF-IDF)] → Doc1: score=0.85
     |
     v
[Return] → Doc1: "the quick brown fox jumps"

Time: 2 lookups + 1 intersection = <1ms (vs 4 document scans = 10ms)
```

**Detailed Indexing Pipeline:**

```
RAW DOCUMENT
     |
     v
[Tokenizer]
"The Quick Brown Fox" → ["The", "Quick", "Brown", "Fox"]
     |
     v
[Lowercase Filter]
["The", "Quick", "Brown", "Fox"] → ["the", "quick", "brown", "fox"]
     |
     v
[Stop Words Filter]
["the", "quick", "brown", "fox"] → ["quick", "brown", "fox"]
(removed: "the")
     |
     v
[Stemmer]
["quick", "brown", "fox"] → ["quick", "brown", "fox"]
(already root forms)
     |
     v
[Inverted Index Update]
Term: "quick"  → Posting: [doc1, doc5] → Add doc_new → [doc1, doc5, doc_new]
Term: "brown"  → Posting: [doc1, doc8] → Add doc_new → [doc1, doc8, doc_new]
Term: "fox"    → Posting: [doc1]       → Add doc_new → [doc1, doc_new]
     |
     v
[Index Stored on Disk/Memory]
```

---

## 🛠️ 7. Problems Solved:

- **Fast Search:** O(1) term lookup instead of O(n) document scan → 1000x speed improvement (1ms vs 1000ms)
- **Full-Text Search:** Any word search kar sakte ho, SQL LIKE '%word%' se better (indexed)
- **Relevance Ranking:** TF-IDF scoring se most relevant documents pehle → Better UX
- **Phrase Search:** "machine learning" (exact phrase) bhi possible (positional index)
- **Fuzzy Search:** Typos handle (Levenshtein distance) → "machne" → "machine"
- **Scalability:** Index sharding across servers → Billion documents search (Google, Amazon)

---

## 🌍 8. Real-World Example:

**Elasticsearch (Used by Uber, Netflix, GitHub):** Inverted Index based search engine. Uber: 100M+ trips indexed, search by rider name/location in <50ms. Implementation: Lucene library (Java) for inverted index, distributed across 100+ nodes. Features: Real-time indexing (new document indexed in 1 sec), fuzzy search (typo tolerance), aggregations (faceted search). Scale: 1TB+ data, 10K queries/sec. Benefit: Riders find past trips instantly, drivers searchable by name, support team resolves issues fast. Without inverted index, searching 100M trips would take minutes.

---

## 🔧 9. Tech Stack / Tools:

- **Elasticsearch:** Distributed search engine based on Lucene. Use for: Full-text search, log analysis (ELK stack), real-time analytics. Features: RESTful API, horizontal scaling, auto-sharding.

- **Apache Solr:** Another Lucene-based search. Use for: Enterprise search, e-commerce product search, document management. Features: Rich query language, faceting, highlighting.

- **Apache Lucene:** Core library (Java) for inverted index. Use for: Building custom search engines, embedded search in applications. Low-level control but complex.

---

## 📐 10. Architecture/Formula:

**TF-IDF Scoring Formula:**

```
TF-IDF(term, doc) = TF(term, doc) × IDF(term)

Where:
TF (Term Frequency) = (Number of times term appears in doc) / (Total terms in doc)
IDF (Inverse Document Frequency) = log(Total documents / Documents containing term)

Example:
Document: "machine learning is great. machine learning rocks."
Total docs in corpus: 1000
Docs containing "machine": 50

Term: "machine"
TF = 2 / 10 = 0.2 (appears 2 times, total 10 words)
IDF = log(1000 / 50) = log(20) = 1.3
TF-IDF = 0.2 × 1.3 = 0.26

Interpretation:
- High TF: Term frequent in this doc (relevant)
- High IDF: Term rare across corpus (distinctive)
- High TF-IDF: Term important for this doc (good match)
```

**Inverted Index Storage Structure:**

```
TERM DICTIONARY (B-Tree for fast lookup):
+-------+----------+
| Term  | Pointer  |
+-------+----------+
| apple | 0x1000   | ──┐
| brown | 0x2000   |   │
| fox   | 0x3000   |   │
+-------+----------+   │
                       │
POSTING LISTS (Linked lists): ←┘
+-------+--------+-------+-------+
| DocID | TF     | Pos   | Next  |
+-------+--------+-------+-------+
| 1     | 3      | [2,5] | 0x1010| ← "apple" in doc1, appears 3 times at positions 2,5
| 5     | 1      | [10]  | 0x1020| ← "apple" in doc5
| 12    | 2      | [1,8] | NULL  | ← "apple" in doc12
+-------+--------+-------+-------+

Compression: Delta encoding for DocIDs
Instead of: [1, 5, 12, 15, 20]
Store: [1, +4, +7, +3, +5] (differences)
Saves 40-60% space
```

**Distributed Search Architecture:**

```
                    [User Query: "machine learning"]
                              |
                              v
                    +-------------------+
                    |  Query Coordinator|
                    |  (Parse & Route)  |
                    +-------------------+
                              |
        +---------------------+---------------------+
        |                     |                     |
        v                     v                     v
   +--------+            +--------+            +--------+
   | Shard1 |            | Shard2 |            | Shard3 |
   | Docs   |            | Docs   |            | Docs   |
   | 1-1M   |            | 1M-2M  |            | 2M-3M  |
   +--------+            +--------+            +--------+
   | Index1 |            | Index2 |            | Index3 |
   +--------+            +--------+            +--------+
        |                     |                     |
        v                     v                     v
   [Results: 10]        [Results: 15]        [Results: 8]
        |                     |                     |
        +---------------------+---------------------+
                              |
                              v
                    +-------------------+
                    |  Merge & Rank     |
                    | (Top 10 results)  |
                    +-------------------+
                              |
                              v
                    [Return to User: 33 total, showing top 10]

Parallel search across shards → 3x faster
```

---

## 💻 11. Code / Flowchart:

**Flowchart (Search Query Processing):**

```
START: User query "quick fox"
     |
     v
[Tokenize Query]
"quick fox" → ["quick", "fox"]
     |
     v
[Normalize]
["quick", "fox"] → ["quick", "fox"] (lowercase)
     |
     v
[Remove Stop Words]
(none to remove)
     |
     v
[Stem Terms]
["quick", "fox"] → ["quick", "fox"]
     |
     v
[Lookup in Inverted Index]
     |
     +---> "quick" → [doc1, doc3, doc5]
     |
     +---> "fox" → [doc1, doc4, doc7]
     |
     v
[Boolean Operation: AND]
Intersection: [doc1] (common in both)
     |
     v
[Calculate TF-IDF Scores]
doc1: score = 0.85
     |
     v
[Sort by Score (Descending)]
     |
     v
[Return Top Results]
doc1: "the quick brown fox jumps"
     |
     v
   END
```

**Code (Simple Inverted Index - Python):**

```python
from collections import defaultdict
import re

class InvertedIndex:
    def __init__(self):
        self.index = defaultdict(list)  # term -> [doc_ids]
        self.documents = {}  # doc_id -> content
    
    def add_document(self, doc_id, text):
        self.documents[doc_id] = text
        terms = self._tokenize(text)
        
        for term in terms:
            if doc_id not in self.index[term]:  # Avoid duplicates
                self.index[term].append(doc_id)
    
    def _tokenize(self, text):
        # Lowercase + split + remove stop words
        text = text.lower()
        words = re.findall(r'\w+', text)
        stop_words = {'the', 'is', 'a', 'an'}
        return [w for w in words if w not in stop_words]
    
    def search(self, query):
        terms = self._tokenize(query)
        
        if not terms:
            return []
        
        # Get posting lists for all terms
        result_sets = [set(self.index[term]) for term in terms]
        
        # Intersection (AND operation)
        result_docs = set.intersection(*result_sets) if result_sets else set()
        
        return list(result_docs)

# Usage
idx = InvertedIndex()
idx.add_document(1, "The quick brown fox jumps")
idx.add_document(2, "The lazy dog sleeps")
idx.add_document(3, "Quick brown rabbit runs")

results = idx.search("quick fox")  # Returns: [1]
print(f"Found in documents: {results}")
```

---

## 📈 12. Trade-offs:

- **Gain:** 1000x faster search (1ms vs 1000ms), scalable to billions of docs | **Loss:** Extra storage (index size = 20-40% of original data), indexing time (new docs take 1-5 sec to index)

- **Gain:** Relevance ranking (TF-IDF), fuzzy search, phrase search | **Loss:** Complex updates (document update requires re-indexing), eventual consistency (real-time search has 1-2 sec delay)

- **Gain:** Distributed search (horizontal scaling) | **Loss:** Network overhead (query multiple shards), merge complexity (combine results from shards)

- **When to use:** Full-text search (Google, Amazon products), log analysis (ELK), document search | **When to skip:** Simple exact match (SQL sufficient), very small datasets (<1000 docs), frequently changing data (index rebuild expensive)

---

## 🐞 13. Common Mistakes:

- **Mistake:** Not using stemming/lemmatization
  - **Why wrong:** "running", "runs", "ran" treated as different terms → Missed results
  - **What happens:** User searches "run" but docs with "running" not returned (poor recall)
  - **Fix:** Apply stemmer (Porter/Snowball) → All forms → "run" (root)

- **Mistake:** Indexing stop words ("the", "is", "a")
  - **Why wrong:** 30-40% of text is stop words → Index size bloated, no value (too common)
  - **What happens:** 2x storage cost, slower search (more postings to process)
  - **Fix:** Remove stop words during indexing (standard list of 100-200 words)

- **Mistake:** Not compressing posting lists
  - **Why wrong:** DocIDs stored as full integers (4 bytes each) → Large index
  - **What happens:** 1 billion docs × 4 bytes = 4GB just for IDs (memory expensive)
  - **Fix:** Delta encoding + variable byte encoding → 60% compression

- **Mistake:** Synchronous indexing (blocking)
  - **Why wrong:** New document → Index update → User waits 5 seconds
  - **What happens:** Bad UX, slow writes
  - **Fix:** Async indexing (queue-based) → Document saved immediately, indexed in background

---

## ✅ 14. Zaroori Notes for Interview:

**Must Mention Points:**
1. **Start with definition:** "Inverted Index ek data structure hai jo Word → Documents mapping store karta hai. Normal approach (Forward Index) mein Document → Words hota hai, jo slow hai (har doc scan karna padta hai)."

2. **Draw structure:** Term Dictionary (B-Tree) → Posting Lists (DocIDs). Mention: "quick" → [1, 5, 12] means docs 1, 5, 12 contain "quick".

3. **Explain indexing pipeline:** Tokenization → Lowercase → Stop words removal → Stemming → Index update. Mention: "running" → "run" (stemming important).

4. **Common follow-ups:**
   - **"TF-IDF kya hai?"** → Term Frequency × Inverse Document Frequency. TF: Term kitni baar doc mein (relevance), IDF: Term kitna rare corpus mein (distinctiveness). High TF-IDF = Important term for this doc.
   - **"Phrase search kaise kaam karta hai?"** → Positional index store karo (term ke saath position). "machine learning" → "machine" at pos 5, "learning" at pos 6 (adjacent) → Match.
   - **"Real-time indexing kaise?"** → In-memory buffer (new docs) + On-disk index (old docs). Har 1 sec buffer flush → Merge with main index. Elasticsearch ka approach.

5. **Mention compression:** "Delta encoding for DocIDs: [1, 5, 12] → [1, +4, +7] saves 40-60% space."

6. **Distributed search:** "Index sharding across nodes. Query coordinator sends query to all shards parallel, merges results. 3 shards = 3x faster."

7. **Pro tip:** "Interview mein TF-IDF formula zaroor likho aur example do. Interviewer impressed hota hai."

---

## ❓ 15. FAQ & Comparisons (MANDATORY - 5 Questions):

**Q1: Forward Index vs Inverted Index - Main difference?**
A: **Forward Index:** Document → Words mapping. Example: Doc1 → ["quick", "fox"]. Search: Har document ko scan karo (slow - O(n)). **Inverted Index:** Word → Documents mapping. Example: "quick" → [Doc1, Doc3]. Search: Seedha term lookup (fast - O(1)). Inverted Index 1000x faster hai large datasets mein. Forward Index use: Document display (original text retrieve). Inverted Index use: Search queries.

**Q2: Stemming vs Lemmatization - Kaunsa use karein?**
A: **Stemming:** Rule-based, fast, approximate. "running" → "run", "better" → "bett" (wrong but fast). **Lemmatization:** Dictionary-based, slow, accurate. "running" → "run", "better" → "good". **Choice:** Stemming for speed (search engines - Elasticsearch default), Lemmatization for accuracy (NLP tasks). Most production systems use Stemming (Porter/Snowball algorithm) kyunki 10x faster hai aur 95% cases mein sufficient.

**Q3: Inverted Index update kaise karte hain jab document change ho?**
A: **3 approaches:** (1) **Delete + Re-add:** Old doc ke saare terms se doc_id remove, new doc index karo (simple but slow). (2) **Incremental Update:** Sirf changed terms update karo (complex but fast). (3) **Versioning:** New version index karo, old version mark deleted, periodic cleanup (Elasticsearch approach). **Best:** Versioning with background merge. New docs in-memory buffer (1 sec), then merge to disk index (efficient).

**Q4: TF-IDF vs BM25 - Kaunsa better ranking algorithm hai?**
A: **TF-IDF:** Classic, simple formula (TF × IDF). Problem: Term frequency linear hai (10 occurrences = 10x score of 1 occurrence - unrealistic). **BM25:** Modern, saturation-based (10 occurrences ≈ 3x score of 1 - diminishing returns). Formula: Complex but better. **Result:** BM25 gives better rankings (Elasticsearch default since v5). **When:** Use BM25 for production (industry standard), TF-IDF for learning/simple cases.

**Q5: Distributed search mein results kaise merge karte hain?**
A: **Process:** (1) Query coordinator sends query to all shards parallel, (2) Each shard returns top-K results with scores (e.g., top 10), (3) Coordinator merges using min-heap (K-way merge), (4) Return global top-K. **Challenge:** Shard1 returns score=0.9, Shard2 returns score=0.85 - scores comparable? **Solution:** Normalized scoring (same IDF across shards - share global stats) ya re-scoring (fetch top 100 from each, re-calculate scores centrally). Elasticsearch uses normalized scoring.

---



---

## Topic 14.2: Search System Architecture - Crawler to Searcher

---

## 🎯 1. Title / Topic: Distributed Search Architecture (Crawler → Indexer → Searcher)

---

## 🐣 2. Samjhane ke liye (Simple Analogy):

Search Engine ek **Library System** jaisa hai with 3 departments:
1. **Crawler (Book Collector):** Duniya bhar se books collect karta hai (web pages download), har din naye books laata hai
2. **Indexer (Librarian):** Books ko categorize karta hai, index cards banata hai (word → book mapping), shelves par arrange karta hai
3. **Searcher (Help Desk):** User aata hai "machine learning" book chahiye, index cards check karta hai, relevant books instantly deta hai

Result: User ko 0.5 second mein exact books mil jaati hain, manually dhundne mein 1 hour lagta.

---

## 📖 3. Technical Definition (Interview Answer):

**Distributed Search Architecture** is a scalable system design that separates concerns into crawling (data collection), indexing (inverted index creation), and searching (query processing) components, distributed across multiple servers for high throughput and low latency.

**Key Components:**
- **Crawler:** Web pages/documents download karta hai, URL frontier maintain karta hai
- **Indexer:** Raw documents ko process karke inverted index banata hai
- **Searcher:** User queries ko process karke relevant documents return karta hai
- **Coordinator:** Query ko multiple shards par distribute, results merge karta hai
- **Replication:** High availability ke liye data copies (Master-Slave)

---

## 🧠 4. Zaroorat Kyun Hai? (Why?):

**Main Problem:** Single server par billion documents index karna impossible hai. 1 billion docs × 2KB = 2TB data. Ek server mein 2TB RAM nahi hota, aur ek server 10K queries/sec handle nahi kar sakta.

**Business Impact:** Slow search = Users leave. Google processes 8.5 billion searches/day (100K queries/sec) - single server se impossible.

**Technical Benefits:**
- **Horizontal Scaling:** 100 servers add karo → 100x capacity (documents + queries)
- **Fault Tolerance:** Ek server crash → Replica se serve (99.99% uptime)
- **Parallel Processing:** Query 10 shards par parallel → 10x faster results
- **Separation of Concerns:** Crawler, Indexer, Searcher independent scale (crawler slow, searcher fast)

---

## 🚫 5. Iske Bina Kya Hoga? (Failure Scenario):

**Scenario: Monolithic Search (Single Server)**
- Data: 100M documents, 200GB index
- Traffic: 1000 queries/sec
- Single server: 64GB RAM (index disk se load → slow), 100 queries/sec capacity
- Result: 900 queries queued → 10 sec latency → Users frustrated → Leave

**Crawler Impact:**
- No crawler → Manual data entry (impossible at scale)
- Slow crawler → Stale data (yesterday's news shown today)
- No URL deduplication → Same page crawled 100 times (waste)

**Real Example:** **DuckDuckGo (Early days 2008)** - Single server architecture → Could handle only 100 queries/sec → Slow during traffic spikes → Users switched to Google. After implementing distributed architecture (2012) → 1000x scale → Now handles 100M+ queries/day.

---

## ⚙️ 6. Under the Hood (Technical Working):

### **Component 1: Web Crawler**

**Working:**
1. **Seed URLs:** Start with initial URLs (e.g., top 1000 websites)
2. **URL Frontier:** Queue of URLs to crawl (priority queue - important sites first)
3. **Fetch:** HTTP request bhejo, HTML download karo
4. **Parse:** HTML parse karke new URLs extract (links)
5. **Deduplication:** URL hash check (already crawled? skip)
6. **Politeness:** Same domain ko 1 sec gap (robots.txt respect)
7. **Store:** Raw HTML store (distributed storage - S3/HDFS)

**Data Flow:**
```
Seed URLs → URL Frontier → Fetcher → Parser → Dedup → Storage
              ↑                                      |
              +---------- New URLs -----------------+
```

### **Component 2: Indexer**

**Working:**
1. **Document Queue:** Crawled documents queue se pick
2. **Text Extraction:** HTML se text extract (remove tags)
3. **Tokenization:** Text → Words
4. **Normalization:** Lowercase, stemming, stop words removal
5. **Inverted Index Update:** Term → DocID mapping
6. **Shard Assignment:** Document ko shard assign (hash-based)
7. **Persistence:** Index disk par save (SSD for speed)

**Batch Processing:**
- Real-time: New docs 1 sec mein indexed (in-memory buffer)
- Batch: Har 10 min buffer flush → Merge with main index

### **Component 3: Query Processor (Searcher)**

**Working:**
1. **Query Parsing:** User query "machine learning" → Tokenize
2. **Query Rewriting:** Spell correction, synonym expansion
3. **Shard Routing:** Query ko all shards par bhejo (parallel)
4. **Index Lookup:** Har shard apne index mein search
5. **Scoring:** TF-IDF/BM25 calculate
6. **Merge:** Results from all shards merge (top-K)
7. **Ranking:** Final ranking (may include ML model)
8. **Return:** Top 10 results user ko

**ASCII Architecture Diagram:**

```
                        [WEB / DATA SOURCES]
                        (Websites, APIs, DBs)
                                |
                                v
                    +----------------------+
                    |   WEB CRAWLER        |
                    | (Distributed)        |
                    | - URL Frontier       |
                    | - Fetcher Pool       |
                    | - Deduplicator       |
                    +----------------------+
                                |
                                | Raw Documents
                                v
                    +----------------------+
                    |   DOCUMENT QUEUE     |
                    |   (Kafka/RabbitMQ)   |
                    +----------------------+
                                |
                                v
                    +----------------------+
                    |   INDEXER CLUSTER    |
                    | (Parallel Workers)   |
                    | - Tokenizer          |
                    | - Stemmer            |
                    | - Index Builder      |
                    +----------------------+
                                |
                                v
        +-------------------------------------------+
        |           DISTRIBUTED INDEX               |
        |  (Sharded across multiple nodes)          |
        +-------------------------------------------+
        |  Shard1  |  Shard2  |  Shard3  | Shard4  |
        | Docs 1-  | Docs 25M-| Docs 50M-| Docs 75M|
        |  25M     |  50M     |  75M     | -100M   |
        | (Master) | (Master) | (Master) | (Master)|
        |    |     |    |     |    |     |    |    |
        | (Slave)  | (Slave)  | (Slave)  | (Slave) |
        +-------------------------------------------+
                                |
                                | Query
                                v
                    +----------------------+
                    | QUERY COORDINATOR    |
                    | - Parse Query        |
                    | - Route to Shards    |
                    | - Merge Results      |
                    +----------------------+
                                |
                                v
                    +----------------------+
                    |  RANKING ENGINE      |
                    | (ML Model - optional)|
                    | - Personalization    |
                    | - Click-through data |
                    +----------------------+
                                |
                                v
                        [USER RESULTS]
                        (Top 10 documents)


DETAILED QUERY FLOW:

[User: "machine learning"]
         |
         v
[Load Balancer] → [Query Coordinator-1]
         |
         +---> Shard1: Search "machine learning"
         |              ↓
         |         Results: [doc5(0.9), doc12(0.8)]
         |
         +---> Shard2: Search "machine learning"
         |              ↓
         |         Results: [doc30(0.95), doc45(0.7)]
         |
         +---> Shard3: Search "machine learning"
         |              ↓
         |         Results: [doc60(0.85), doc78(0.75)]
         |
         v
[Merge Results]
Min-Heap: [doc30(0.95), doc5(0.9), doc60(0.85), ...]
         |
         v
[Top 10 Results]
         |
         v
[Return to User]
Time: 50ms (parallel search across 3 shards)
```

---

## 🛠️ 7. Problems Solved:

- **Scalability:** Billion documents indexed → Sharding across 100+ servers (horizontal scaling)
- **High Throughput:** 100K queries/sec → Load balanced across searcher nodes
- **Low Latency:** Parallel shard search → 50ms response (vs 500ms sequential)
- **Fault Tolerance:** Server crash → Replica serves → 99.99% uptime
- **Fresh Data:** Crawler continuously updates → Real-time news indexed in 1 min
- **Relevance:** Multi-stage ranking (TF-IDF + ML model) → Best results first

---

## 🌍 8. Real-World Example:

**Google Search Architecture:** 100+ data centers globally, 1000+ servers per center. Crawler: Googlebot crawls 20 billion pages/day. Indexer: 100 trillion words indexed. Searcher: 8.5 billion queries/day (100K/sec). Sharding: Index split into 10,000+ shards. Replication: 3x replication (Master + 2 Slaves). Latency: <200ms for 99% queries. Technology: Custom C++ crawler, Bigtable for storage, MapReduce for indexing, custom query processor. Result: 92% search market share, $200B+ annual revenue from ads. Without distributed architecture, impossible to serve global scale.

---

## 🔧 9. Tech Stack / Tools:

- **Elasticsearch:** Complete distributed search solution. Use for: Full-text search, log analytics, real-time indexing. Features: Auto-sharding, replication, RESTful API. Scale: 100+ nodes, petabyte data.

- **Apache Solr:** Enterprise search platform. Use for: E-commerce search, document management. Features: Faceting, highlighting, spell-check. Similar to Elasticsearch but older.

- **Scrapy (Crawler):** Python web crawling framework. Use for: Custom crawlers, data extraction. Features: Async I/O, middleware, pipelines. Scale: 1000+ pages/sec per server.

- **Apache Nutch (Crawler):** Distributed web crawler. Use for: Large-scale crawling (billions of pages). Integrates with Hadoop for storage.

---

## 📐 10. Architecture/Formula:

**Shard Assignment Formula:**

```
Shard_ID = hash(document_id) % total_shards

Example:
document_id = "doc12345"
hash("doc12345") = 987654321
total_shards = 10

Shard_ID = 987654321 % 10 = 1

Document stored in Shard-1

Benefits:
- Even distribution (hash function uniform)
- Deterministic (same doc always same shard)
- Scalable (add shards, rehash only 1/n docs)
```

**Query Latency Calculation:**

```
Total_Latency = Network_Latency + Shard_Search_Time + Merge_Time

Where:
Network_Latency = RTT (Round Trip Time) to farthest shard
Shard_Search_Time = max(Shard1_time, Shard2_time, ..., ShardN_time)
                    (parallel, so max not sum)
Merge_Time = K-way merge of top-K results from N shards
           = O(N × K × log(K))

Example:
Network_Latency = 5ms
Shard_Search_Time = max(10ms, 12ms, 8ms) = 12ms (3 shards parallel)
Merge_Time = 3 shards × 10 results × log(10) = 3 × 10 × 3.3 = 100 ops ≈ 1ms

Total_Latency = 5 + 12 + 1 = 18ms

Without sharding (sequential):
Total = 10 + 12 + 8 = 30ms (slower)
```

**Replication Factor Decision:**

```
Replication_Factor = Desired_Availability / (1 - Node_Failure_Rate)

Example:
Desired_Availability = 99.99% (4 nines)
Node_Failure_Rate = 1% (1 node fails per 100)

Replication_Factor = 0.9999 / (1 - 0.01) = 0.9999 / 0.99 ≈ 1.01

Minimum: 2x replication (1 Master + 1 Slave)
Recommended: 3x replication (1 Master + 2 Slaves) for safety

Trade-off:
- 2x replication: 2x storage cost, 99.9% availability
- 3x replication: 3x storage cost, 99.99% availability
```

**Crawler Politeness Formula:**

```
Crawl_Delay = max(robots.txt_delay, default_delay)

Where:
robots.txt_delay = Specified by website (e.g., 1 sec)
default_delay = Your crawler's default (e.g., 0.5 sec)

Example:
Website robots.txt: Crawl-delay: 2
Your default: 0.5 sec

Crawl_Delay = max(2, 0.5) = 2 seconds

Respect website's request (avoid ban)
```

---

## 💻 11. Code / Flowchart:

**Flowchart (End-to-End Search System):**

```
INDEXING PIPELINE:

START: Crawler
     |
     v
[URL Frontier]
Pick next URL
     |
     v
[HTTP Fetch]
Download HTML
     |
     v
[Parse HTML]
Extract text + links
     |
     v
[Deduplication]
URL hash check
     |
     +---> Already crawled? → Skip
     |
     +---> New URL? → Continue
     |
     v
[Store Raw Document]
S3/HDFS
     |
     v
[Push to Queue]
Kafka/RabbitMQ
     |
     v
[Indexer Worker]
Pick from queue
     |
     v
[Tokenize + Normalize]
     |
     v
[Update Inverted Index]
     |
     v
[Assign to Shard]
hash(doc_id) % shards
     |
     v
[Persist Index]
Disk (SSD)
     |
     v
   END


QUERY PIPELINE:

START: User query
     |
     v
[Query Coordinator]
Parse "machine learning"
     |
     v
[Spell Check]
"machne" → "machine"
     |
     v
[Tokenize]
["machine", "learning"]
     |
     v
[Route to All Shards]
Parallel requests
     |
     +---> Shard1: Search
     |          ↓
     |     [doc5: 0.9]
     |
     +---> Shard2: Search
     |          ↓
     |     [doc30: 0.95]
     |
     +---> Shard3: Search
     |          ↓
     |     [doc60: 0.85]
     |
     v
[Merge Results]
Min-heap (top-K)
     |
     v
[Ranking]
ML model (optional)
     |
     v
[Return Top 10]
     |
     v
   END
```

**Code (Simplified Distributed Search Coordinator):**

```python
import hashlib
from typing import List, Dict

class SearchCoordinator:
    def __init__(self, shard_nodes: List[str]):
        self.shard_nodes = shard_nodes  # ["shard1:9200", "shard2:9200", ...]
        self.num_shards = len(shard_nodes)
    
    def get_shard(self, doc_id: str) -> str:
        """Determine which shard contains this document"""
        hash_val = int(hashlib.md5(doc_id.encode()).hexdigest(), 16)
        shard_id = hash_val % self.num_shards
        return self.shard_nodes[shard_id]
    
    def search(self, query: str, top_k: int = 10) -> List[Dict]:
        """Distributed search across all shards"""
        # Tokenize query
        terms = query.lower().split()
        
        # Send query to all shards in parallel (simplified - use threading)
        all_results = []
        for shard in self.shard_nodes:
            results = self._search_shard(shard, terms, top_k)
            all_results.extend(results)
        
        # Merge results (sort by score, take top-K)
        all_results.sort(key=lambda x: x['score'], reverse=True)
        return all_results[:top_k]
    
    def _search_shard(self, shard: str, terms: List[str], top_k: int) -> List[Dict]:
        """Search single shard (mock implementation)"""
        # In production: HTTP request to shard's search API
        # Here: Mock results
        return [
            {'doc_id': f'{shard}_doc1', 'score': 0.9, 'title': 'Result 1'},
            {'doc_id': f'{shard}_doc2', 'score': 0.8, 'title': 'Result 2'}
        ]

# Usage
coordinator = SearchCoordinator(['shard1:9200', 'shard2:9200', 'shard3:9200'])

# Index: Determine shard for document
doc_shard = coordinator.get_shard('doc12345')
print(f"Document stored in: {doc_shard}")

# Search: Query all shards
results = coordinator.search('machine learning', top_k=10)
print(f"Found {len(results)} results")
```

---

## 📈 12. Trade-offs:

- **Gain:** Horizontal scaling (add servers → more capacity), high availability (replication) | **Loss:** Complexity (distributed system debugging hard), network overhead (inter-shard communication)

- **Gain:** Parallel search (10 shards → 10x faster), fault tolerance (replica serves if master down) | **Loss:** Storage cost (3x replication = 3x storage), consistency challenges (replica lag)

- **Gain:** Fresh data (crawler updates continuously), comprehensive coverage (billions of pages) | **Loss:** Crawling cost (bandwidth, compute), politeness delays (slow crawling)

- **When to use:** Large datasets (>1M documents), high traffic (>100 queries/sec), need high availability (99.9%+) | **When to skip:** Small datasets (<10K docs - single server sufficient), low traffic (<10 queries/sec), simple exact match (SQL enough)

---

## 🐞 13. Common Mistakes:

- **Mistake:** Not implementing crawler politeness (robots.txt ignore)
  - **Why wrong:** Website ban kar dega (IP block), legal issues (ToS violation)
  - **What happens:** Crawler blocked, incomplete data, potential lawsuit
  - **Fix:** Respect robots.txt, implement crawl delays (1-2 sec per domain), user-agent identify

- **Mistake:** Synchronous shard queries (sequential instead of parallel)
  - **Why wrong:** 10 shards × 10ms each = 100ms total (slow)
  - **What happens:** High latency, poor UX, can't handle traffic
  - **Fix:** Parallel requests (threading/async), max latency = slowest shard (10ms not 100ms)

- **Mistake:** No replica for shards (single point of failure)
  - **Why wrong:** Shard crash → Partial results (missing documents) → Bad UX
  - **What happens:** Downtime, data loss, angry users
  - **Fix:** 2-3x replication (Master + Slaves), auto-failover (Elasticsearch built-in)

- **Mistake:** Uniform shard distribution without considering data skew
  - **Why wrong:** Hash-based sharding → Shard1 has 10M docs, Shard2 has 1M docs (imbalance)
  - **What happens:** Shard1 slow (hotspot), uneven load, poor performance
  - **Fix:** Monitor shard sizes, rebalance periodically, use consistent hashing with virtual nodes

---

## ✅ 14. Zaroori Notes for Interview:

**Must Mention Points:**
1. **Start with 3 components:** "Search system mein 3 main components hain - Crawler (data collection), Indexer (inverted index creation), Searcher (query processing). Yeh distributed hote hain scalability ke liye."

2. **Draw architecture:** Crawler → Document Queue → Indexer → Sharded Index → Query Coordinator → Merge Results. Mention parallel processing.

3. **Explain sharding:** "Index ko multiple shards mein divide karte hain. Formula: shard_id = hash(doc_id) % num_shards. Query time par all shards ko parallel search, results merge."

4. **Common follow-ups:**
   - **"Crawler kaise duplicate URLs avoid karta hai?"** → URL hash store in Bloom Filter (space-efficient), check before crawling. If exists, skip.
   - **"Shard failure handle kaise karoge?"** → Replication (Master + Slave). Master down → Slave promoted. Query coordinator automatically routes to Slave.
   - **"Real-time indexing kaise?"** → In-memory buffer (new docs), har 1 sec flush to disk, merge with main index. Elasticsearch ka approach.
   - **"Results merge kaise karte hain?"** → Min-heap (K-way merge). Har shard top-10 bhejta hai, coordinator min-heap se global top-10 nikalta hai.

5. **Mention scale numbers:** "Google: 20B pages crawled/day, 100T words indexed, 8.5B queries/day, <200ms latency."

6. **Pro tip:** "Interview mein mention karo - Crawler politeness (robots.txt), Shard replication (HA), Parallel search (low latency). Yeh 3 points impress karte hain."

---

## ❓ 15. FAQ & Comparisons (MANDATORY - 5 Questions):

**Q1: Crawler mein URL Frontier kaise implement karein (priority queue)?**
A: **Data Structure:** Min-heap based priority queue. **Priority factors:** (1) PageRank (important sites first), (2) Freshness (news sites frequent), (3) Depth (homepage > deep pages). **Implementation:** Redis Sorted Set (score = priority, value = URL) ya custom heap. **Deduplication:** Bloom Filter for URL hash (space-efficient, false positive OK). **Politeness:** Per-domain queue with delay (same domain URLs 1 sec gap). **Scale:** 1B URLs in frontier → Distributed queue (Kafka) with partitioning by domain.

**Q2: Indexer mein batch vs real-time indexing - Trade-off kya hai?**
A: **Batch Indexing:** Documents ko batch mein process (e.g., 10K docs ek saath), efficient (disk I/O optimize), but delay (1 hour lag). **Real-time Indexing:** Har doc immediately index (1 sec lag), fresh data, but expensive (frequent disk writes). **Hybrid (Best):** In-memory buffer (new docs), har 1-5 sec flush to disk, background merge with main index. Elasticsearch uses this - 1 sec refresh interval (configurable). **Trade-off:** Real-time = Fresh data but high cost, Batch = Cheap but stale data. Hybrid balances both.

**Q3: Shard rebalancing kab aur kaise karein?**
A: **When:** (1) Shard size imbalance (Shard1=10GB, Shard2=1GB), (2) New shards added (scale up), (3) Hot shard (one shard getting 80% queries). **How:** (1) Identify heavy shard, (2) Split into 2 shards (hash range divide), (3) Copy data to new shard, (4) Update routing table, (5) Delete old shard. **Downtime:** Zero-downtime rebalancing - new shard serves while old exists, gradual cutover. **Frequency:** Quarterly or when imbalance >20%. **Elasticsearch:** Auto-rebalancing built-in (shard allocation awareness).

**Q4: Query coordinator failure handle kaise karein?**
A: **Problem:** Coordinator crash → All queries fail (single point of failure). **Solution:** (1) **Multiple Coordinators:** Load balancer ke peeche 10+ coordinator instances, (2) **Stateless:** Coordinator stateless hai (no data store), crash toh new instance spawn, (3) **Health Checks:** LB continuously checks coordinator health (ping every 5 sec), unhealthy remove from pool. **Elasticsearch:** Har node coordinator ban sakta hai (no dedicated coordinator), client kisi bhi node ko query bhej sakta hai. **Result:** 99.99% availability (coordinator failure invisible to users).

**Q5: Distributed search mein consistency kaise maintain karein (replica lag)?**
A: **Problem:** Master indexed new doc, Slave lag (1 sec delay), query Slave ko gaya → Doc missing (inconsistency). **Solutions:** (1) **Read from Master:** Always master se read (consistent but master overload), (2) **Eventual Consistency:** Accept 1 sec lag (most systems - Elasticsearch default), (3) **Quorum Read:** Majority replicas se read (2 out of 3 agree), (4) **Version Vectors:** Track doc version, return latest. **Best:** Eventual consistency for search (1 sec lag acceptable), Strong consistency for critical ops (payments). **Trade-off:** Consistency vs Availability (CAP theorem - search chooses Availability).

---



---

## Topic 14.3: Typeahead / Autocomplete System

---

## 🎯 1. Title / Topic: Typeahead System (Real-time Search Suggestions)

---

## 🐣 2. Samjhane ke liye (Simple Analogy):

Typeahead ek **Smart Assistant** hai jo aapke sentence complete karta hai. Jaise aap "How to cook..." type karte ho, assistant turant suggest karta hai "How to cook pasta", "How to cook rice", "How to cook chicken" (popular queries). Ye **Dictionary** jaisa kaam karta hai - aap "app" type karo, dictionary mein "apple", "application", "appointment" instantly mil jaate hain. Result: User ko pura query type nahi karna padta, 50% typing save, fast search.

---

## 📖 3. Technical Definition (Interview Answer):

**Typeahead (Autocomplete)** is a real-time suggestion system that predicts and displays query completions as user types, using prefix matching on a pre-computed dataset of popular queries, typically implemented with Trie data structure for O(k) lookup where k is prefix length.

**Key terms:**
- **Prefix Matching:** User types "mac" → Match all queries starting with "mac" (machine, macbook, mac os)
- **Trie (Prefix Tree):** Tree data structure where each node represents a character, efficient for prefix search
- **Top-K Suggestions:** Most popular K queries for given prefix (e.g., top 5)
- **Query Frequency:** How many times query searched (popularity score)
- **Latency:** <100ms response time (real-time feel)

---

## 🧠 4. Zaroorat Kyun Hai? (Why?):

**Main Problem:** Users ko pura query type karna slow hai (10-15 seconds), typos hote hain, exact query yaad nahi rehta. Typeahead se 50% typing save, fast search, better UX.

**Business Impact:** Google study: Typeahead increases search engagement by 30%, reduces typos by 40%, improves user satisfaction. Amazon: Product search with autocomplete increases conversions by 20%.

**Technical Benefits:**
- **Speed:** User 3-4 characters type kare, suggestion mil jaye → Fast search
- **Typo Correction:** "iphone" type karte time "iphon" par suggestion → Typo prevent
- **Discovery:** Users ko popular queries pata chalte hain → Better search terms
- **Reduced Load:** Fewer full searches (users select suggestion) → Server load reduce

---

## 🚫 5. Iske Bina Kya Hoga? (Failure Scenario):

**Scenario: No Autocomplete**
- User: Wants to search "machine learning algorithms"
- Without typeahead: Types full 28 characters (10 seconds), makes typo "algoritms" → No results → Frustrated
- With typeahead: Types "mach" (4 chars, 2 sec) → Sees "machine learning algorithms" → Clicks → Done

**User Impact:** Slow typing, typos, wrong queries, bad results, frustration.

**Real Example:** **Amazon (Pre-2010)** - No autocomplete on mobile → Users typed wrong product names → 30% searches returned no results → Lost sales. After implementing typeahead (2010) → Typos reduced 40%, conversions increased 20%, mobile search engagement up 50%.

---

## ⚙️ 6. Under the Hood (Technical Working):

**Typeahead System Components:**

1. **Data Collection:** User queries log karo (search history)
2. **Aggregation:** Query frequency count (how many times searched)
3. **Trie Building:** Popular queries se Trie data structure banao
4. **Prefix Lookup:** User types "mac" → Trie mein "mac" prefix search → All matching queries
5. **Ranking:** Frequency ke basis par top-K select (most popular first)
6. **Caching:** Popular prefixes cache mein (Redis) → Fast response
7. **Return:** Top 5-10 suggestions user ko

**Trie Data Structure (Core):**

```
ROOT
 |
 +-- m
     |
     +-- a
         |
         +-- c (freq: 1000)
             |
             +-- h (freq: 800)
             |   |
             |   +-- i (freq: 500)
             |       |
             |       +-- n (freq: 500)
             |           |
             |           +-- e (freq: 500) [END: "machine", freq=500]
             |
             +-- b (freq: 300)
                 |
                 +-- o (freq: 300)
                     |
                     +-- o (freq: 300)
                         |
                         +-- k (freq: 300) [END: "macbook", freq=300]

User types: "mac"
Trie traversal: ROOT → m → a → c
Find all END nodes under "c": ["machine" (500), "macbook" (300)]
Sort by frequency: ["machine", "macbook"]
Return top 5
```

**ASCII Diagram (Typeahead Architecture):**

```
[User Types: "mac"]
     |
     v
+------------------+
| Frontend         |
| (Debounce 200ms) | ← Wait 200ms after last keystroke
+------------------+
     |
     | HTTP Request: GET /suggest?q=mac
     v
+------------------+
| API Gateway      |
| (Rate Limit)     |
+------------------+
     |
     v
+------------------+
| Cache Layer      |
| (Redis)          |
| Check: "mac" →   |
+------------------+
     |
     +---> Cache HIT? → Return cached suggestions
     |
     +---> Cache MISS? → Continue
     |
     v
+------------------+
| Trie Service     |
| (In-Memory Trie) |
| Prefix Search    |
+------------------+
     |
     | Traverse: ROOT → m → a → c
     | Find: ["machine":500, "macbook":300, "mac os":200]
     v
+------------------+
| Ranking Service  |
| (Top-K Selection)|
| Sort by freq     |
+------------------+
     |
     | Top 5: ["machine", "macbook", "mac os", "mac mini", "mac pro"]
     v
+------------------+
| Cache Update     |
| Store in Redis   |
| TTL: 1 hour      |
+------------------+
     |
     v
[Return to User]
Suggestions: ["machine", "macbook", "mac os", "mac mini", "mac pro"]

Latency: 
- Cache HIT: 5ms
- Cache MISS: 50ms (Trie lookup + ranking)
```

**Data Collection & Trie Building Pipeline:**

```
USER SEARCHES (Logs):
"machine learning" → 10,000 times
"macbook pro" → 5,000 times
"mac os" → 3,000 times
     |
     v
[Aggregation Job - Daily]
Count frequency per query
     |
     v
[Filter]
Remove: Spam, Adult content, Low frequency (<10)
     |
     v
[Top Queries]
Select top 10M queries (by frequency)
     |
     v
[Trie Builder]
Insert each query into Trie with frequency
     |
     v
[Serialize Trie]
Save to disk (binary format)
     |
     v
[Deploy to Servers]
Load Trie in memory (10GB RAM)
     |
     v
[Serve Suggestions]
Real-time prefix lookup
```

---

## 🛠️ 7. Problems Solved:

- **Fast Typing:** 50% typing saved → User types "mac" instead of "machine learning" (3 vs 16 chars)
- **Typo Prevention:** Suggestions appear before typo → User selects correct query
- **Query Discovery:** Users see popular queries → Better search terms (e.g., "machine learning algorithms" instead of "ml")
- **Mobile UX:** Small keyboard, hard to type → Autocomplete critical (tap suggestion vs type)
- **Reduced Server Load:** Users select suggestions → Fewer full searches → Less backend processing
- **Personalization:** User history based suggestions → Relevant results (e.g., frequent "python" searcher sees "python" first)

---

## 🌍 8. Real-World Example:

**Google Search Autocomplete:** 3.5 billion searches/day, autocomplete on every keystroke. Implementation: Distributed Trie across 1000+ servers, 10 billion queries indexed. Latency: <50ms globally (edge caching). Features: Personalized suggestions (user history), trending queries (real-time events), spell correction. Scale: 100TB+ query logs, 1M updates/hour. Benefit: 30% faster searches, 40% fewer typos, 25% more search engagement. Technology: Custom C++ Trie, Bigtable for storage, Memcached for caching. Without typeahead, Google's UX would be significantly worse.

---

## 🔧 9. Tech Stack / Tools:

- **Redis:** In-memory cache for popular prefixes. Use for: Fast lookup (<5ms), TTL support, sorted sets for ranking. Store: Prefix → Top-K suggestions.

- **Elasticsearch (Completion Suggester):** Built-in autocomplete. Use for: Full-text prefix search, fuzzy matching, easy integration. Features: FST (Finite State Transducer) based, memory efficient.

- **Custom Trie (In-Memory):** Full control, optimized for prefix search. Use for: High performance (<10ms), custom ranking logic. Language: C++/Java for speed.

---

## 📐 10. Architecture/Formula:

**Trie Space Complexity:**

```
Space = Number_of_Nodes × Node_Size

Where:
Number_of_Nodes ≈ Total_Characters_in_All_Queries
Node_Size = 8 bytes (pointer) + 4 bytes (frequency) + 1 byte (char) = 13 bytes

Example:
10M queries, avg length 20 chars
Total_Characters = 10M × 20 = 200M characters
Space = 200M × 13 bytes = 2.6GB

Optimization: Compressed Trie (PATRICIA) → 40% reduction → 1.5GB
```

**Lookup Time Complexity:**

```
Time = O(k) where k = prefix length

Example:
User types "machine" (7 chars)
Trie traversal: 7 nodes (m → a → c → h → i → n → e)
Time: 7 × 10ns (memory access) = 70ns ≈ 0.00007ms

Finding top-K suggestions: O(n log k) where n = matching queries
If 1000 matches, top-10: 1000 × log(10) ≈ 3000 ops ≈ 0.03ms

Total: 0.07ms (negligible)
```

**Ranking Formula (Weighted Score):**

```
Score = (Frequency × 0.6) + (Recency × 0.3) + (Personalization × 0.1)

Where:
Frequency = Query search count (normalized 0-1)
Recency = Time decay factor (recent queries higher)
Personalization = User history match (1 if user searched before, 0 otherwise)

Example:
Query: "machine learning"
Frequency = 10,000 searches → Normalized = 0.8
Recency = Searched 1 day ago → Factor = 0.9
Personalization = User searched before → 1.0

Score = (0.8 × 0.6) + (0.9 × 0.3) + (1.0 × 0.1)
      = 0.48 + 0.27 + 0.1
      = 0.85

Higher score → Higher rank in suggestions
```

**Trie Node Structure:**

```
class TrieNode {
    char character;           // 1 byte
    int frequency;            // 4 bytes (query frequency)
    bool is_end;              // 1 byte (end of query?)
    TrieNode* children[26];   // 26 pointers (a-z) = 208 bytes
    string query;             // Only if is_end=true (variable)
}

Total per node: ~214 bytes (without compression)

Optimization: HashMap for children (sparse) → 50 bytes average
```

---

## 💻 11. Code / Flowchart:

**Flowchart (Typeahead Query Processing):**

```
START: User types "mac"
     |
     v
[Frontend Debounce]
Wait 200ms (no more keystrokes)
     |
     v
[Send Request]
GET /suggest?q=mac
     |
     v
[Check Redis Cache]
Key: "suggest:mac"
     |
     +---> Cache HIT?
     |        |
     |        v
     |     Return cached ["machine", "macbook", ...]
     |     (5ms latency)
     |
     +---> Cache MISS?
     |
     v
[Trie Lookup]
Traverse: ROOT → m → a → c
     |
     v
[Collect All Matches]
DFS from node 'c': ["machine":500, "macbook":300, "mac os":200, ...]
     |
     v
[Rank by Score]
Sort by frequency (or weighted score)
     |
     v
[Select Top-K]
Top 5: ["machine", "macbook", "mac os", "mac mini", "mac pro"]
     |
     v
[Cache Result]
Redis SET "suggest:mac" = [...] (TTL: 1 hour)
     |
     v
[Return to User]
JSON: {"suggestions": ["machine", "macbook", ...]}
     |
     v
   END

Total Latency:
- Cache HIT: 5ms
- Cache MISS: 50ms (Trie + ranking + cache update)
```

**Code (Simple Trie Implementation):**

```python
class TrieNode:
    def __init__(self):
        self.children = {}  # char -> TrieNode
        self.is_end = False
        self.frequency = 0
        self.query = ""

class Typeahead:
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, query: str, frequency: int):
        """Insert query into Trie with frequency"""
        node = self.root
        for char in query.lower():
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        
        node.is_end = True
        node.query = query
        node.frequency = frequency
    
    def search_prefix(self, prefix: str, top_k: int = 5):
        """Find top-K suggestions for prefix"""
        # Traverse to prefix node
        node = self.root
        for char in prefix.lower():
            if char not in node.children:
                return []  # Prefix not found
            node = node.children[char]
        
        # Collect all queries under this prefix
        results = []
        self._dfs(node, results)
        
        # Sort by frequency and return top-K
        results.sort(key=lambda x: x[1], reverse=True)
        return [query for query, freq in results[:top_k]]
    
    def _dfs(self, node: TrieNode, results: list):
        """DFS to collect all queries"""
        if node.is_end:
            results.append((node.query, node.frequency))
        
        for child in node.children.values():
            self._dfs(child, results)

# Usage
typeahead = Typeahead()

# Build Trie (from query logs)
typeahead.insert("machine learning", 10000)
typeahead.insert("macbook pro", 5000)
typeahead.insert("mac os", 3000)
typeahead.insert("mac mini", 1000)

# Search
suggestions = typeahead.search_prefix("mac", top_k=3)
print(suggestions)  # ["machine learning", "macbook pro", "mac os"]
```

---

## 📈 12. Trade-offs:

- **Gain:** Fast suggestions (<50ms), 50% typing saved, better UX | **Loss:** Memory cost (2-10GB Trie in RAM), stale data (Trie rebuilt daily)

- **Gain:** Typo prevention, query discovery, mobile-friendly | **Loss:** Privacy concerns (query logging), bias (popular queries dominate)

- **Gain:** Reduced server load (users select suggestions) | **Loss:** Initial build time (Trie construction 1-2 hours for 10M queries)

- **When to use:** Search engines, e-commerce, any text input with common patterns | **When to skip:** Unique queries (no patterns), privacy-critical apps (no logging), very small datasets (<1000 queries)

---

## 🐞 13. Common Mistakes:

- **Mistake:** No debouncing on frontend (request on every keystroke)
  - **Why wrong:** User types "machine" (7 chars) → 7 requests → Server overload
  - **What happens:** High latency, wasted bandwidth, poor UX
  - **Fix:** Debounce 200-300ms (wait for user to stop typing)

- **Mistake:** Storing full Trie in database (disk-based lookup)
  - **Why wrong:** Disk I/O slow (10-50ms) → Latency too high for real-time
  - **What happens:** Suggestions appear after 1 second (bad UX)
  - **Fix:** Load Trie in memory (RAM), use Redis cache for popular prefixes

- **Mistake:** Not limiting suggestions (returning 100 matches)
  - **Why wrong:** Large response size (10KB+), slow rendering, overwhelming user
  - **What happens:** Network delay, UI lag, confused user
  - **Fix:** Return top 5-10 suggestions only (ranked by relevance)

- **Mistake:** No personalization (same suggestions for all users)
  - **Why wrong:** User who searches "python programming" daily sees "python snake" first (irrelevant)
  - **What happens:** Poor relevance, user ignores suggestions
  - **Fix:** Boost suggestions based on user history (weighted scoring)

---

## ✅ 14. Zaroori Notes for Interview:

**Must Mention Points:**
1. **Start with Trie:** "Typeahead ka core data structure Trie hai. Prefix search O(k) time mein hota hai jahan k = prefix length. Example: 'mac' type kiya toh ROOT → m → a → c traverse, phir saare child queries collect."

2. **Draw Trie structure:** Simple tree with nodes (m → a → c → h → i → n → e), mark end nodes with frequency. Show how "mac" prefix matches multiple queries.

3. **Explain ranking:** "Suggestions ko frequency ke basis par rank karte hain. Most searched queries pehle. Formula: Score = Frequency × 0.6 + Recency × 0.3 + Personalization × 0.1."

4. **Common follow-ups:**
   - **"Trie memory mein fit nahi hota toh?"** → Sharding (prefix-based: a-m → Server1, n-z → Server2) ya Top queries only (10M instead of 1B)
   - **"Real-time trending queries kaise?"** → Separate hot cache (Redis) for trending, updated every 5 min from recent logs
   - **"Fuzzy matching kaise (typos)?"** → Levenshtein distance (edit distance ≤2), ya Elasticsearch Completion Suggester with fuzzy option
   - **"Personalization kaise implement?"** → User history store (last 100 queries), boost matching suggestions in ranking

5. **Mention caching:** "Popular prefixes (a, b, c, ...) Redis mein cache (80-20 rule - 20% prefixes = 80% traffic). TTL 1 hour."

6. **Latency numbers:** "Target <100ms. Cache HIT: 5ms, Cache MISS: 50ms (Trie lookup + ranking)."

7. **Pro tip:** "Interview mein Trie draw karo aur time complexity mention karo - O(k) for lookup, O(n log k) for top-K selection. Interviewer impressed hota hai."

---

## ❓ 15. FAQ & Comparisons (MANDATORY - 5 Questions):

**Q1: Trie vs Database (SQL) for typeahead - Kaunsa better?**
A: **Trie (In-Memory):** O(k) lookup (k=prefix length), <10ms latency, perfect for real-time. **Database (SQL LIKE):** O(n) scan (n=total queries), 50-200ms latency, too slow. **Example:** User types "mac", Trie: 7 node traversals (70ns), SQL: Scan 10M rows with LIKE 'mac%' (100ms). **Result:** Trie 1000x faster. **When SQL OK:** Very small dataset (<10K queries), infrequent searches (<10/sec). **Production:** Always use Trie or Elasticsearch for typeahead.

**Q2: Trie vs Elasticsearch Completion Suggester - Kaunsa use karein?**
A: **Custom Trie:** Full control, optimized for specific use case, <10ms latency, but complex to build. **Elasticsearch:** Built-in, easy integration, fuzzy matching, but 20-50ms latency. **Choice:** Custom Trie for ultra-low latency (<10ms) aur simple prefix match. Elasticsearch for fuzzy search, complex ranking, easy maintenance. **Most companies:** Start with Elasticsearch (faster development), optimize to custom Trie if needed (Google, Amazon use custom).

**Q3: Typeahead mein personalization kaise implement karein?**
A: **Approach:** User history store (Redis/DB - last 100 queries per user). **Ranking adjustment:** Base score (frequency) + Personalization boost. **Formula:** `Final_Score = Base_Score × (1 + 0.5 × User_Match)`. User_Match=1 if user searched this before, else 0. **Example:** "python" query - Base=0.7, User searched "python" 10 times → Final=0.7×1.5=1.05 (boosted). **Privacy:** Hash user_id, store anonymized, GDPR compliant (delete on request). **Scale:** 100M users × 100 queries × 20 bytes = 200GB (manageable).

**Q4: Trending queries (real-time events) kaise handle karein?**
A: **Problem:** Trie daily rebuild → New trending queries (e.g., "world cup 2024") missing for 24 hours. **Solution:** Hot cache (Redis) for trending. **Process:** (1) Stream processing (Kafka) on search logs, (2) Count queries in 5-min windows, (3) Detect spikes (10x normal frequency), (4) Push to Redis hot cache (TTL 1 hour), (5) Typeahead checks hot cache first, then Trie. **Example:** "earthquake california" suddenly 1000x searches → Detected in 5 min → Added to hot cache → Appears in suggestions immediately. **Tools:** Kafka Streams, Flink for real-time aggregation.

**Q5: Typeahead mein offensive/spam queries kaise filter karein?**
A: **3-layer filtering:** (1) **Blacklist:** Explicit offensive words (manual list of 10K terms), (2) **ML Model:** Classify query as spam/offensive (trained on labeled data), (3) **User reports:** Users can report bad suggestions, auto-remove after 10 reports. **Implementation:** Filter during Trie building (offline), not during lookup (too slow). **Example:** Query "how to hack..." → ML model score=0.9 (spam) → Excluded from Trie. **Edge case:** False positives (e.g., "hacking cough remedy") → Manual whitelist. **Google approach:** Combination of all 3 + human reviewers for edge cases.

---



---

## 🎯 Module 14 Complete Summary:

**All Topics Covered:** 3/3 ✅
- ✅ Topic 14.1: Inverted Index - Search Engine Fundamentals (TF-IDF, Tokenization, Stemming)
- ✅ Topic 14.2: Distributed Search Architecture - Crawler, Indexer, Searcher (Sharding, Replication)
- ✅ Topic 14.3: Typeahead/Autocomplete System - Trie Data Structure (Prefix Search, Ranking, Caching)

**Key Takeaways:**
1. **Inverted Index:** Word → Documents mapping, 1000x faster than document scan, TF-IDF scoring for relevance
2. **Distributed Architecture:** Crawler (data collection) → Indexer (Trie building) → Searcher (query processing), sharding for scale
3. **Typeahead:** Trie data structure for O(k) prefix lookup, Redis caching for popular prefixes, personalization for better UX
4. **Production Scale:** Google (100T words indexed, 8.5B queries/day), Elasticsearch (petabyte scale, 10K queries/sec)

**Interview Focus:**
- Draw Inverted Index structure: Term Dictionary → Posting Lists
- Explain TF-IDF formula with example calculation
- Draw distributed architecture: Crawler → Queue → Indexer → Sharded Index → Query Coordinator
- Draw Trie structure for typeahead with frequency at nodes
- Mention real-world: Google (custom Trie), Elasticsearch (Lucene-based), Amazon (autocomplete 20% conversion boost)

**Common Patterns:**
- **Indexing:** Tokenization → Lowercase → Stop words removal → Stemming → Index update
- **Search:** Query parsing → Index lookup → Intersection (AND) → Ranking (TF-IDF/BM25) → Top-K results
- **Typeahead:** Prefix → Trie traversal → Collect matches → Rank by frequency → Cache → Return top-5

**Optimization Techniques:**
- **Compression:** Delta encoding for DocIDs (40-60% space saving)
- **Caching:** Redis for popular prefixes (80-20 rule)
- **Sharding:** Hash-based distribution across nodes
- **Replication:** 2-3x for high availability (99.99% uptime)
- **Debouncing:** 200ms wait before typeahead request (reduce load)

**Progress:** 14/21 Modules Completed 🎉

**Next Module:** Module 15 - Design Notification System (Push, SMS, Email, Priority Queues)

---
