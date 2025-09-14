🤖 Chat Auto Reply Bot

This Python script automates real-time replies in a chat interface (like WhatsApp Web or any other chat window) using OpenRouter's GPT-3.5 Turbo model.

✨ It reads the latest chat message, checks if it was sent by the other person, generates a smart and friendly one-line reply using AI, and sends it automatically!

💡 Key Features

🔍 Monitors the chat interface using screen coordinates

📋 Copies the latest message from the screen

🧠 Sends it to the OpenRouter AI (GPT-3.5-Turbo) and gets a one-line, human-like reply

⌨️ Auto-pastes and sends the reply back

🚫 Avoids self-replies and duplicate responses

✨ Works like an invisible smart chatbot assistant

🧠 How It Works
1. Copy Chat Message

Using pyautogui, the script selects a region of the chat window, copies the latest message, and extracts the sender and message content.

pyautogui.moveTo(...)  # Drag-select chat area
pyautogui.hotkey('ctrl', 'c')  # Copy text
copied_text = pyperclip.paste()

2. Parse and Clean Message

Extracts only the last line from the copied chat using regex:

match = re.match(r'\[\d{1,2}:\d{2}\s[APM]{2},.*?\]\s(.*?):\s(.*)', last_line)


Also removes timestamps and sender info to build a clean prompt for AI:

cleaned_text = clean_chat(copied_text)

3. Send to OpenRouter AI

Uses OpenRouter’s GPT API to get a casual, friendly reply:

payload = {
    "model": "openai/gpt-3.5-turbo",
    "messages": [{"role": "user", "content": prompt}]
}
response = requests.post(...)


Example prompt:

A casual chat between two friends. Respond naturally in 1 line like a human would.
[Conversation...]
Reply in a single friendly sentence.

4. Reply Automatically

If the message is new and not from yourself, it pastes the AI response and hits Enter.

pyperclip.copy(ai_reply)
pyautogui.hotkey('ctrl', 'v')
pyautogui.press('enter')


📄 License

MIT License — use it freely, modify it openly.


ALSO CONTAINS A "CURSUR DETECTOR" using method that clearly tells the location of your live cursur 