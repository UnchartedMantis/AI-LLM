import praw
import re
import openai
import os
from dotenv import load_dotenv

# Load API keys
load_dotenv()
REDDIT_CLIENT_ID = os.getenv("REDDIT_CLIENT_ID")
REDDIT_SECRET = os.getenv("REDDIT_SECRET")
REDDIT_USER_AGENT = os.getenv("REDDIT_USER_AGENT")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
openai.api_key = OPENAI_API_KEY

# Initialize Reddit API
reddit = praw.Reddit(
    client_id=REDDIT_CLIENT_ID,
    client_secret=REDDIT_SECRET,
    user_agent=REDDIT_USER_AGENT,
)

def extract_username(url):
    match = re.search(r'reddit.com/user/([A-Za-z0-9_-]+)/?', url)
    return match.group(1) if match else None

def scrape_user_data(username, limit=30):
    user = reddit.redditor(username)
    posts = []     # ✅ Use list, not set
    comments = []  # ✅ Use list, not set

    try:
        for submission in user.submissions.new(limit=limit):
            posts.append({
                "title": submission.title,
                "body": submission.selftext,
                "subreddit": str(submission.subreddit),
                "url": f"https://www.reddit.com{submission.permalink}"
            })

        for comment in user.comments.new(limit=limit):
            comments.append({
                "body": comment.body,
                "subreddit": str(comment.subreddit),
                "url": f"https://www.reddit.com{comment.permalink}"
            })
    except Exception as e:
        print("Error:", e)

    return posts, comments

def generate_persona(posts, comments):
    content = "USER POSTS:\n"
    for post in posts:
        content += f"- [{post['title']}]({post['url']}): {post['body'][:300]}...\n"

    content += "\nUSER COMMENTS:\n"
    for comment in comments:
        content += f"- [{comment['subreddit']}]({comment['url']}): {comment['body'][:300]}...\n"

    prompt = f"""
    Based on the following Reddit user's posts and comments, create a detailed user persona like the one in this image: 
    [https://www.redditusercontent.com/user_persona_example] (assume it looks like the uploaded image with sections like motivations, frustrations, personality, etc.).
    
    Cite specific posts or comments for each characteristic.

    CONTENT:
    {content}
    """

    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.7,
        max_tokens=1800
    )

    return response.choices[0].message.content

def save_to_file(data, filename="user_persona.txt"):
    with open(filename, "w", encoding="utf-8") as f:
        f.write(data)
    print(f"Persona saved to {filename}")

if __name__ == "__main__":
    url = input("Enter Reddit profile URL: ")
    username = extract_username(url)
    
    if not username:
        print("Invalid Reddit URL.")
        exit()

    print(f"Scraping data for user: {username}...")
    posts, comments = scrape_user_data(username)

    print("Generating user persona using LLM...")
    persona = generate_persona(posts, comments)

    save_to_file(persona)
