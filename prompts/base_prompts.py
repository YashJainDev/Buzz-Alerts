from config.settings import *
from .examples import EXAMPLES
def get_meme_trend_prompt():
    prompt_template = f"""
You are a social media trends expert.

Please provide a list of the top *newest* memes currently trending in India (focus on ONLY those relevant within the **last 1-2 months** i.e March-April, 2025).

Instructions:
- Identify 10 distinct meme lines that are **trending**, **recent**, *viral**, and **widely used** across Indian social media (Instagram Reels and Reddit Only), or popular culture.
- **Only select meme phrases that are commonly usable within a sentence or as standalone reactions.** (Reject random slang words, single emoji trends, overly niche references.)
- **Strictly filter out**:
- Reject Any memes that are offensive, insensitive, NSFW, or inappropriate for general audiences.
- Reject Any meme phrases that cannot be naturally used in a push notification title or casual sentence.

For EACH selected phrase, provide a DETAILED and EXPLANATORY context:
- **Meaning & Usage**: How is it used in conversations? What does it imply?
- **Emotion/Situation**: What feelings or situation does it usually represent? (e.g., confusion, excitement, disappointment, irony, absurdity, pride).
- **Nuance**: Why is it funny, relatable, or culturally significant? Write enough detail so even someone unfamiliar can understand its meaning and vibe.

**Important Emphasis**:
- Focus only on **truly trending**, highly relevant memes (last 1-2 months).
- **Auto-reject any meme that doesn't fit notification/title use cases.**
- **Auto-reject any meme that is not trending nowadays.**
- Ensure memes are safe, appropriate, and versatile for broad audiences.

**Output Format**:
Strictly output a JSON object where each key is the meme/catchphrase string, and the corresponding value is its full detailed context (as described above).
Do NOT include any introductory text, comments, or formatting outside the JSON object.

Example (format only):

"Meme Phrase 1": "Full detailed context here...",
"Meme Phrase 2": "Full detailed context here...",
...


    """
    return prompt_template.strip()

def get_meme_notification_prompt(meme_list):
    prompt_template = f"""
You are a creative Indian copywriter specialized in app notifications.

**App Context:** {APP_CONTEXT}

**App Value to Highlight:** {APP_VALUE_REWARDS}

**App Tone:** {APP_TONE}

**Goal:** Generate 10-15 catchy, short push notification titles (each under 100 characters).

**Input Memes/Phrases:** 
{meme_list}

**Instructions:**
- Every title must directly use or be clearly inspired by a meme/phrase.
- Titles must hint at {APP_VALUE_REWARDS} through playful wording or CTAs.
- Structure:
  - Meme reference (direct or indirect).
  - Action or app value hint (deal, reward, shop, discover, etc.).
- Keep tone aligned with {APP_TONE}.
- Use simple *Hinglish*, *casual expressions*, and *emojis* sparingly for Indian audiences.
- Strictly check each title:
  - Clear meme link?
  - Clear call-to-action or value hint?
  - Under 60 characters?
  - Relatable for Indian users?

**Important:** Return **only** the raw list of titles. No extra explanations.

**Good Title Examples:**
{EXAMPLES}

**Now, generate the new list of 10-15 titles based on the memes and these refined instructions..
"""
    return prompt_template.strip()


