from prompts.base_prompts import *
from utils.api_handler import *
from config.settings import MODEL,TEMP
from utils.text_utils import clean_text
from utils.loader import *

# Step 1: Fetching memes
stop_spinner = loading_animation("🔍 Fetching trending memes")
response = get_gemini_response(prompt=get_meme_trend_prompt() , model=MODEL , temp=TEMP)
stop_spinner()
print("\n✅ Memes fetched successfully.\n")

# Step 2: Generating titles
stop_spinner2 = loading_animation("✨ Generating notification titles")
meme_list = clean_text(response.text)
prompt = get_meme_notification_prompt(meme_list)
notification_titles = generate_notification_titles(prompt,MODEL,TEMP)
stop_spinner2()
print("\n✅ Titles generated successfully.\n")
print(notification_titles.text)