
import re
import json
import os

DATA_JS_PATH = '/var/www/gloto/data.js'
OUTPUT_DIR = '/var/www/gloto/js/locales'

# 1. Read data.js content
with open(DATA_JS_PATH, 'r', encoding='utf-8') as f:
    content = f.read()

# 2. Extract QUESTIONS array
# This is a bit hacky regex parsing, but sufficient for known structure
questions_match = re.search(r'const QUESTIONS = \[(.*?)\];', content, re.DOTALL)
if questions_match:
    questions_str = questions_match.group(1)
    # Convert JS object syntax to Python dictionary logic (approximate)
    # Removing comments
    questions_str = re.sub(r'//.*', '', questions_str)
    # Parse object strings like { category: "School", ... }
    # We will just eval it after some cleanup or use regex to find blocks
    qa_blocks = re.findall(r'\{(.*?)\}', questions_str, re.DOTALL)

# 3. Extract UI_TEXT
ui_match = re.search(r'const UI_TEXT = \{(.*)\};', content, re.DOTALL)
# Extract Category meta
cat_match = re.search(r'const CATEGORY_META = \{(.*)\};', content, re.DOTALL)

# Initialize data structure
lang_data = {}
ALL_LANGS = ['ko', 'vn', 'cn', 'th', 'ph', 'id', 'mn', 'uz', 'ne', 'km', 'si', 'my', 'bn', 'lo', 'ru', 'en', 'jp', 'kz']

for lang in ALL_LANGS:
    lang_data[lang] = {
        'ui': {},
        'content': { 'School': [], 'Travel': [], 'Hospital': [], 'Market': [], 'Restaurant': [], 'Airport': [] }
    }

# Process Questions
for block in qa_blocks:
    # dirty parse: category: "School", difficulty: 1, ko: "...", en: "..."
    cat_m = re.search(r'category:\s*"([^"]+)"', block)
    if not cat_m: continue
    category = cat_m.group(1)
    
    for lang in ALL_LANGS:
        # regex for lang key: ko: "value"
        # Handles quote variations
        l_m = re.search(fr'{lang}:\s*"([^"]+)"', block)
        if l_m:
            text = l_m.group(1)
            lang_data[lang]['content'][category].append(text)

# Process UI Text (Manual mapping based on what we know, or basic extraction)
# Since parsing nested JS objects with regex is hard, I will use a simplified approach
# fetching from the UI_TEXT in data.js is hard. 
# I will Use a fallback: The ko.js is already perfect. 
# For others, I will generate a stub with content populated from QUESTIONS (which is the most important part).
# Users can update UI text later or I can update it if they ask.
# Actually, I really should try to preserve the UI text I wrote.

# Let's try to extract UI text for each lang roughly
params = ['appName', 'appDesc', 'slogan', 'title', 'target', 'start', 'back', 'listening', 'placeholder', 'msgPerfect', 'msgGood', 'msgBad', 'correction', 'listen', 'why', 'aiName', 'selectStep', 'speakStep', 'check', 'nativeLabel', 'selectTarget']

for lang in ALL_LANGS:
    # Find the block for this lang in UI_TEXT
    # 'ko': { ... }
    lang_block_m = re.search(fr"'{lang}':\s*\{(.*?)\}},", content, re.DOTALL)
    if not lang_block_m:
        lang_block_m = re.search(fr"'{lang}':\s*\{(.*?)\}\s*$", content, re.DOTALL) # Last one might not have comma
    
    if lang_block_m:
        lb = lang_block_m.group(1)
        for p in params:
            pm = re.search(fr"{p}:\s*"([^"]+)"", lb)
            if pm:
                lang_data[lang]['ui'][p] = pm.group(1)
    
    # Category Names
    # In data.js, CATEGORY_META had: 'School': { ko: '...', en: '...' }
    # We parse this too.
    cat_names = {}
    if cat_match:
        c_content = cat_match.group(1)
        # find 'School': { ... }
        for cat in ['School', 'Travel', 'Hospital', 'Market', 'Restaurant', 'Airport']:
             cm = re.search(fr"'{cat}':\s*\{(.*?)\}", c_content, re.DOTALL)
             if cm:
                 c_block = cm.group(1)
                 lm = re.search(fr"{lang}:\s*'([^']+)'", c_block) 
                 if not lm: lm = re.search(fr"{lang}:\s*"([^"]+)"", c_block)
                 if lm:
                     lang_data[lang]['ui'][f'cat_{cat}'] = lm.group(1)

# 4. Write Files
for lang, data in lang_data.items():
    if not data['content']['School']: continue # Skip empty
    
    file_path = os.path.join(OUTPUT_DIR, f"{lang}.js")
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write("window.GLOTO = window.GLOTO || {};\n")
        f.write("window.GLOTO.DATA = window.GLOTO.DATA || {};\n\n")
        f.write(f"window.GLOTO.DATA['{lang}'] = ")
        f.write(json.dumps(data, indent=4, ensure_ascii=False))
        f.write(";\n")
    print(f"Generated {file_path}")

