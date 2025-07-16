🧠 Reddit User Persona Generator

This project analyzes a Reddit user's public posts and comments to generate a detailed User Persona — including motivations, interests, frustrations, and behavioral traits — and cites specific posts/comments used to infer each trait.

🚀 Features
Takes a Reddit user profile URL as input

Scrapes latest posts and comments using PRAW

Uses OpenAI GPT-4 to generate a structured persona

Saves output in user_persona.txt

Citations included for each characteristic

🛠️ Tech Stack
Python 3

PRAW – Reddit API wrapper

OpenAI API (GPT-4) – for persona generation

dotenv – to manage API keys

🧱 Project Structure
bash
Copy
Edit
reddit_user_persona/
├── main.py
├── .env
├── user_persona.txt
└── README.md
✅ Setup & Usage
Install dependencies:

bash
Copy
Edit
pip install praw openai python-dotenv
Add API keys in .env:

ini
Copy
Edit
REDDIT_CLIENT_ID=your_id
REDDIT_SECRET=your_secret
REDDIT_USER_AGENT=your_agent
OPENAI_API_KEY=your_openai_key
Run the script:

bash
Copy
Edit
python main.py
Enter a Reddit profile URL, e.g.
https://www.reddit.com/user/kojied/

Check user_persona.txt for the generated persona.

🧠 Sample Output
yaml
Copy
Edit
Name: Alex (u/kojied) | Age: ~30
Location: US | Occupation: Tech Analyst

Motivations:
- Promotes eco-conscious lifestyle (Post in r/ZeroWaste)

Frustrations:
- Dislikes vague mental health advice (Comment in r/selfimprovement)

Personality:
- Reflective, analytical, socially aware
...
✨ How It Works
Scrapes recent Reddit posts & comments

Builds a unified context block

Sends it as a prompt to GPT-4

Extracts persona insights with post/comment citations

📌 Notes
Works with public Reddit profiles only

Designed for ethical research & LLM experimentation

Easy to extend into a web app or Streamlit tool

