from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder


query_analyzer_prompt = ChatPromptTemplate.from_messages([
    ("user", (
        "### ROLE\n"
        "You are an expert Query Optimizer for a RAG system.\n\n"
        "### TASK\n"
        "Analyze the User Query and break it into a JSON list of independent, atomic sub-questions "
        "needed to retrieve full context from a vector database.\n\n"
        "### RULES\n"
        "1. Decompose comparisons (A vs B) into separate searches for A and B.\n"
        "2. If the query is simple, return a single-item list.\n"
        "3. Ensure questions are self-contained (no pronouns like 'it' or 'they').\n"
        "4. FOLLOW THE GIVEN SCHEMA: {given_schema}, FOR GENERATING THE RESPONSE.\n\n"
        "### EXAMPLES\n"
        "Input: 'Difference between ClassSwift and TeamOne?'\n"
        "Output: [\"What is ClassSwift and its features?\", \"What is TeamOne and its features?\"]\n\n"
        "### INPUT QUERY\n"
        "User Query: {user_query}\n\n"
        "### RESPONSE (JSON LIST)"
    ))
])


question_generator_prompt = ChatPromptTemplate.from_messages([
    ("user", (
        "### INSTRUCTION\n"
        "You are a Support Assistant. Your goal is to provide a factual answer based ONLY on the provided Context. "
        "If the information is missing, admit you do not know. Do not hallucinate.\n\n"
        "### CONTEXT FROM DATABASE\n"
        "{context}\n\n"
        "### CONVERSATION HISTORY"
    )),
    MessagesPlaceholder(variable_name="chat_history"),
    ("user", (
        "### USER QUESTION\n"
        "{user_query}\n\n"
        "### FINAL ANSWER REQUIREMENTS\n"
        "- Be direct and concise.\n"
        "- Use bullet points for features and feature-based comparisons.\n"
        "- CITATIONS: At the end of your response, provide a 'Sources' section.\n"
        "- LINKS: Extract the 'Source' paths/URLs from the context and list them as clickable Markdown links.\n"
        "- If a source is a file path, display just the file name as the link text.\n"
        "- If unsure, respond with: 'I'm sorry, I don't have enough information to answer that.'\n"
        "- Do not mention 'the context' in your prose.\n"
    ))
])