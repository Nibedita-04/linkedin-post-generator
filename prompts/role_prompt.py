from langchain_core.prompts import ChatPromptTemplate

role_prompt = ChatPromptTemplate.from_messages(
    [
#         (
#             "system",
#             "You analyze professional roles for LinkedIn content personalization."
#         ),
#         (
#             "human",
#             """
# User has described their role below.

# Role Description:
# {user_role}

# From this, extract:
# 1. Primary role (short title)
# 2. Career level (Student / Entry / Mid / Senior)
# 3. Domain or specialization (if any)

# Respond in JSON with keys:
# - primary_role
# - career_level
# - domain
# """
#         )


        ("system", 
         "You are an expert LinkedIn content strategist."),
        (
            "human",
            """
Identify the user's professional role from the input.

Input:
{user_role}

Return a short normalized role name.
"""
        )
    ]
)