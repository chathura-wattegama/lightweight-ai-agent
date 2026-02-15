import requests
import json

# ==== SETUP ====
API_KEY = "YOUR_API_KEY_HERE"  # Replace with your OpenAI API key
MODEL = "gpt-4o-mini"

print("Lightweight AI Agent Started. Type 'exit' to quit.\n")

while True:
    user_input = input("You: ")

    if user_input.lower() == "exit":
        print("Agent shutting down.")
        break

    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {API_KEY}"
    }

    data = {
        "model": MODEL,
        "messages": [
            {"role": "system", "content": "You are a concise, helpful AI assistant."},
            {"role": "user", "content": user_input}
        ]
    }

    try:
        response = requests.post(
            "https://api.openai.com/v1/chat/completions",
            headers=headers,
            data=json.dumps(data)
        )

        result = response.json()
        reply = result["choices"][0]["message"]["content"]
        print("\nAgent:", reply, "\n")

    except Exception as e:
        print("Error:", e)