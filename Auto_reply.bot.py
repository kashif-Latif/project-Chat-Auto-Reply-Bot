import pyautogui
import pyperclip
import time
import requests
import json
import re

# .... OpenRouter Setup ....
API_KEY = "API_KEY"
MODEL = "openai/gpt-3.5-turbo"
OPENROUTER_URL = "https://openrouter.ai/api/v1/chat/completions"

headers = {
    "Authorization": f"Bearer {API_KEY}",
    "Content-Type": "application/json",
    "HTTP-Referer": "http://localhost",
    "X-Title": "ChatAutoReplyBot"
}

YOUR_NAME = "me"
last_message_replied_to = ""

def clean_chat(text):
    cleaned = re.sub(r'\[\d{1,2}:\d{2}\s[APM]{2},.*?\]\s.*?:', '', text)
    return ' '.join(cleaned.strip().split())

def get_ai_reply(prompt_text):
    payload = {
        "model": MODEL,
        "messages": [{"role": "user", "content": prompt_text}]
    }
    response = requests.post(OPENROUTER_URL, headers=headers, data=json.dumps(payload))
    if response.status_code == 200:
        return response.json()["choices"][0]["message"]["content"].strip()
    else:
        print(f"API Error {response.status_code}: {response.text}")
        return None


pyautogui.click(1110, 1064)
time.sleep(1)




while True:
    try:
        
        pyautogui.moveTo(723, 262, duration=0.5)
        pyautogui.mouseDown()
        pyautogui.moveTo(1880, 933, duration=1)
        pyautogui.mouseUp()
        time.sleep(0.4)
        pyautogui.hotkey('ctrl', 'c')
        pyautogui.click(1880, 933)  # Deselect.....
        time.sleep(0.4)
        copied_text = pyperclip.paste()

        
        lines = copied_text.strip().splitlines()
        last_line = next((line for line in reversed(lines) if line.strip()), "")
        print("\n--- Debug ---")
        print("Copied chat text:", copied_text)
        print("Last line:", repr(last_line))

        match = re.match(r'\[\d{1,2}:\d{2}\s[APM]{2},.*?\]\s(.*?):\s(.*)', last_line)
        if not match:
            print("Couldn't parse message. Skipping.")
            time.sleep(3)
            continue

        sender = match.group(1).strip()
        message_text = match.group(2).strip()
        print("Parsed sender:", repr(sender))
        print("Parsed message:", repr(message_text))
        print("YOUR_NAME:", repr(YOUR_NAME))
        print("sender.lower() == YOUR_NAME.lower() ?", sender.lower(), YOUR_NAME.lower())

        # Only respond if last message is from opponent AND it's not the same one already replied
        if sender.lower() != YOUR_NAME.lower():
            if message_text != last_message_replied_to:
                print("Replying: New opponent message detected.")
                cleaned_text = clean_chat(copied_text)
                prompt = (
                    "A casual chat between two friends. Respond naturally in 1 line like a human would.\n"
                    f"{cleaned_text}\n"
                    "Reply in a single friendly sentence."
                )
                ai_reply = get_ai_reply(prompt)
                if ai_reply:
                    print("AI Reply:", ai_reply)
                    pyperclip.copy(ai_reply)
                    time.sleep(0.3)
                    pyautogui.click(1144, 996)
                    time.sleep(0.2)
                    pyautogui.hotkey('ctrl', 'v')
                    time.sleep(0.2)
                    pyautogui.press('enter')
                    last_message_replied_to = message_text
                else:
                    print("AI returned no reply.")
            else:
                print("Already replied to this message.")
        else:
            print("Last message is from YOU. No reply should happen.")

        time.sleep(4)

    except KeyboardInterrupt:
        print("Bot stopped by user.")
        break
    except Exception as e:
        print(f"Error: {str(e)}")
        time.sleep(5)
