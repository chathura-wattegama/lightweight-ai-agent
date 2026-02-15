import requests
import json
import os

# ==== CONFIG ====
API_KEY = os.getenv("OPENAI_API_KEY")  # Must set in Termux shell
MODEL = "gpt-4o-mini"

if not API_KEY:
    print("Error: OPENAI_API_KEY not found. Run 'export OPENAI_API_KEY=sk-XXXX' in Termux.")
    exit(1)

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

        if "error" in result:
            print("\nAgent Error:", result["error"]["message"], "\n")
        elif "choices" in result and len(result["choices"]) > 0:
            reply = result["choices"][0]["message"]["content"]
            print("\nAgent:", reply, "\n")
        else:
            print("\nAgent: No response received. Check API key or network.\n")

    except Exception as e:
        print("Request Exception:", e)
