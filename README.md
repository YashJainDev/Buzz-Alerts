# Meme-based Push Notification Generator

This project automatically generates catchy, meme-inspired push notification titles tailored for Indian audiences using the **Gemini API**. It leverages trending memes from Indian social media (Instagram & Reddit) to craft engaging app notifications for social-commerce, food delivery, fashion, and other apps.

## Features
- Fetches the latest trending meme phrases with cultural relevance.
- Generates 10–15 push notification titles inspired by those memes.
- Supports dynamic app context, tone, and value messaging.
- Modular and easy to modify for different use cases.

---

## Project Structure
.
├── config/
│ └── settings.py # Contains your configurations about your app
├── prompts/
│ └── base_prompts.py # contains functions to generate prompts
│ └── examples.py # contains examples ffor better results
├── utils/
│ └── api_handler.py # contains api handling for gemini
│ main.py # Entryu point for the app
├── requirements.txt # Python dependencies
├── README.md # Project documentation

---

## Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/notification-generator.git
cd notification-generator
```
### 2. Create and Activate Virtual Environment (Optional but Recommended)

```bash
python -m venv venv
source venv/bin/activate    # For macOS/Linux
venv\Scripts\activate       # For Windows
```
### 3. Install Dependencies

```bash
pip install -r requirements.txt
```
### 4. Configure Gemini API Key
Create a env file with the following structure:
```bash
GEMINI_API_KEY = "YOUR API KEY"
```
---
## How to Run
Run the generator script to fetch trending memes and generate titles:
```bash
python main.py
```
Output will be printed in the console with a list of 10–15 meme-based push notification titles.

---

## Customization

You can modify:

* `app_context`: The kind of app you're targeting (e.g., food delivery, fashion).

* `app_value_rewards`: The feature or incentive to highlight (e.g., "Get cashback", "Free delivery").

* `app_tone`: The tone of the app (e.g., fun, quirky, youthful).

These values can be changed in `config/settings.py`.