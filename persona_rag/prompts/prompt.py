class Prompt:
    template = {
        "cot": """To solve the problem, Please think and reason step by step, then answer.
question:
{question}
        
Generation Format:
Reasoning process:
Answer:
""",
        # TODO
        "user_profile": """Your task is to help the User Profile Agent improve its understanding of user preferences based on ranked document lists and the shared global memory pool.

Question:
{question}
Passages:
{passages}
Global Memory:
{global_memory}

Task Description:
From the provided passages and global memory pool, analyze clues about the user's search preferences. Look for themes, types of documents, and navigation behaviors that reveal user interest. Use these insights to recommend how the User Profile Agent can refine and expand the user profile to deliver better-personalized results.
""",
        "contextual_retrieval": """You are a search technology expert guiding the Contextual Retrieval Agent to deliver context-aware document retrieval.

Question:
{question}
Passages:
{passages}
Global Memory:
{global_memory}

Task Description:
Using the global memory pool and the retrieved passages, identify strategies to refine document retrieval. Highlight how user preferences, immediate needs, and global insights can be leveraged to adjust search queries and prioritize results that align with the user's interests. Ensure the Contextual Retrieval Agent uses this shared information to deliver more relevant and valuable results.
""",
        "live_session": """Your expertise in session analysis is required to assist the Live Session Agent in dynamically adjusting results.

Question:
{question}
Passages:
{passages}
Global Memory:
{global_memory}

Task Description:
Examine the retrieved passages and information in the global memory pool. Determine how the Live Session Agent can use this data to refine its understanding of the user's immediate needs. Suggest ways to dynamically adjust search results or recommend new queries in real-time, ensuring that session adjustments align with user preferences and goals.
""",
        "document_ranking": """Your task is to help the Document Ranking Agent prioritize documents for better ranking.

Question:
{question}
Passages:
{passages}
Global Memory:
{global_memory}

Task Description:
Analyze the retrieved passages and global memory pool to identify ways to rank documents effectively. Focus on combining historical user preferences, immediate needs, and session behavior to refine ranking algorithms. Your insights should ensure that documents presented by the Document Ranking Agent are prioritized to match user interests and search context.
""",
        "feedback": """You are an expert in feedback collection and analysis, guiding the Feedback Agent to gather and utilize user insights.

Question:
{question}
Passages:
{passages}
Global Memory:
{global_memory}

Task Description:
Using the retrieved passages and global memory pool, identify methods for collecting implicit and explicit user feedback. Suggest ways to refine feedback mechanisms to align with user preferences, such as ratings, surveys, or behavioral data. Your recommendations should guide the Feedback Agent in updating other agents' models for more personalized and relevant results.
""",
    }