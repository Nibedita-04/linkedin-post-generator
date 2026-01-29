# LinkedIn Post Generator (AI-Powered)

## Overview

The LinkedIn Post Generator is an AI-powered application that helps users create high-quality, personalized LinkedIn posts based on their role, intent, and post idea. The system uses Large Language Models (LLMs) and LangChain to generate structured, engaging, and professional content through a multi-step reasoning pipeline.

This project is designed to support students, job seekers, professionals, and content creators in improving their LinkedIn presence and personal branding.

---

## Problem Statement

Many professionals struggle to write effective LinkedIn posts due to limited time, writing confidence, or lack of understanding of platform-specific tone and engagement strategies. This project addresses that challenge by automating the post creation process while maintaining personalization, relevance, and professional quality.

---

## Key Features

* Role-based post generation tailored to different professions
* Intent detection to understand the purpose of the post
* Multi-step AI workflow for structured and high-quality content
* Customizable tone, writing style, hashtags, and emojis
* Memory-based personalization to adapt to user preferences over time
* Modular LangChain pipeline for scalability and maintainability

---

## How It Works

The system follows a structured multi-stage pipeline:

1. Understands the user's role
2. Detects the intent of the post (educational, storytelling, hiring, etc.)
3. Plans the structure and key points of the post
4. Generates a polished LinkedIn-ready post
5. Applies tone, formatting, and engagement best practices

This approach improves coherence and quality compared to single-prompt AI generation.

---

## Project Structure

```
LINKEDINPOSTGENERATOR/

chains/
  generator_chain.py      Handles final post generation
  intent_chain.py         Detects post intent
  planner_chain.py        Plans post structure
  role_chain.py           Interprets user role

config/
  llm.py                  LLM configuration and initialization

memory/
  conversational_memory.py  Stores user writing preferences

prompts/
  generator_prompt.py     Instructions for final post writing
  intent_prompt.py        Instructions for intent classification
  planner_prompt.py       Instructions for post planning
  role_prompt.py          Instructions for role understanding

app.py                    Application interface
main.py                   Core pipeline execution
memory_history.json       Stored memory data
.env                      Environment variables and API keys
README.md                 Project documentation
```

---

## Technology Stack

* Python
* LangChain
* Large Language Models (Groq/OpenAI/Local LLMs)
* Prompt Engineering
* Streamlit (optional user interface)
* JSON-based memory storage

---

## Installation

Clone the repository:

```bash
git clone https://github.com/your-username/linkedin-post-generator.git
cd linkedin-post-generator
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Create a `.env` file and add your API keys:

```
OPENAI_API_KEY=your_key_here
```

---

## Running the Project

Run the application:

```bash
python app.py
```

If using Streamlit:

```bash
streamlit run app.py
```

---

## Example Usage

Input:

* Role: Data Analyst
* Idea: Sharing internship experience

Output:
A professional LinkedIn post tailored to analytics, career growth, and learning outcomes.

---

## Use Cases

* Students building personal brand and portfolios
* Job seekers increasing LinkedIn visibility
* Professionals sharing insights and achievements
* Recruiters writing hiring posts
* Content creators generating consistent LinkedIn content

---

## Challenges Addressed

* Reducing AI hallucination through structured chain pipelines
* Improving output consistency using modular prompts
* Managing evolving LangChain APIs and tooling
* Maintaining personalization using memory storage

---

## Future Enhancements

* Engagement prediction and performance scoring
* Trend-based topic recommendations
* Post scheduling automation
* Multi-language support
* Analytics dashboard for post reach and engagement
* Deeper personalization with long-term memory

---

## License

This project is licensed under the MIT License.

---

## Author

Developed by Nibedita Kar
AI and Data Science Enthusiast
Focused on real-world AI applications and automation

---

## If you want, I can also provide

* A more technical README for AI/ML recruiters
* A simplified README for non-technical audiences
* A resume-ready project description
* A polished GitHub profile project summary
* A professional case study write-up for this project

Tell me the style you want and I will refine it further.
