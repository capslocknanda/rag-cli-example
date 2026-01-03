## Assignment Overview

Please design and implement a **minimal LLM-based Knowledge Q&A system** that simulates an enterprise internal knowledge use case.

---

### Part 1: System Design (Most Important)

Please provide a short design document (2–3 pages) that covers:

* **A high-level system architecture** (ingestion, retrieval, generation, evaluation/logging)
* **Key design decisions and trade-offs**, including:
* Why you would use (or not use) RAG in this scenario
* How you choose retrieval top-K and why
* LLM decoding choices (e.g., determinism vs. sampling) and when they matter
* Which parts of the system should be deterministic and why


* **Failure modes and debugging strategies:**
* How you would debug incorrect or unstable answers
* How you would observe cost, latency, and system behavior over time



---

### Part 2: Minimal Working Implementation

Please implement a small working prototype that demonstrates the core flow:

* **LLM:** Any LLM of your choice (hosted or open-source)
* **Vector Store:** Any vector store of your choice
* **Dataset:** A small document set (approximately 10–30 documents is sufficient)
* **Interface:** A simple interface (CLI, notebook, or script is fine — no UI required)

**The implementation should demonstrate:**

1. A user query being answered
2. Visibility into retrieved context
3. The ability to re-run or replay a query

---

### Part 3: Evaluation & Reflection

Please include brief written answers to the following:

1. How do you determine whether this system is **“working well”**?
2. If you had two more weeks, what would you **improve first**, and why?
3. What is something you would **explicitly avoid** doing in a production system, and why?

---

Would you like me to help you draft the high-level system architecture or suggest a tech stack for Part 2?