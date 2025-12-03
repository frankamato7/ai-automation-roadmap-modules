# Module 4 – Prompt Engineering + LLM Fundamentals

## Goals
- Learn core prompt engineering techniques
- Understand roles, structure, constraints, and formatting levers
- Build a reusable prompt template library
- Use the OpenAI API effectively
- Build small, reliable LLM-powered tools

## Lessons & Highlights

### Lesson 1 – Prompt Engineering Fundamentals (12/02/25)
- Reviewed the three core prompt levers: role, structure, constraints
- Created a structured prompt template library under lesson_1/:
  - system_prompts/
  - task_prompts/
  - format_prompts/
  - constraint_prompts/
- Built four foundational templates:
  - Expert system role prompt
  - Key-insights extraction prompt
  - Bullet-point formatting prompt
  - Word-limit + language-restriction constraint prompt
- Refined each template for clarity, boundaries, and reliability
- Established production-style template structure for future LLM tools

### Lesson 2 - OpenAI API Basics + Summarizer Tool (12/03/25)
- Installed and configured the OpenAI Python SDK
- Created .env for secure key storage
- Built a warm-up script to test client connectivity
- Implemented client.py as a reusable OpenAI wrapper
- Built summarizer.py using prompt engineering fundamentals
- Added CLI usage and robust API error handling