from portkey_ai import Portkey
from keys import portkey_api_key, provider_name, api_key1

portkey_client = Portkey(api_key=portkey_api_key, virtual_key=provider_name)
messages = [{"role": "system", "content": "You are a helpful assistant."}]
try:
    while True:
        user_input = input("You: ").strip()
        if user_input.lower() in ("exit", "quit"):
            print("Exiting chat.")
            break

        messages.append({"role": "user", "content": user_input})
        try:
            response = portkey_client.chat.completions.create(
                model="google/gemini-2.5-flash",
                messages=messages,
                cache=False
            )
        except Exception as e:
            print("Error calling the model:", e)
            # remove the last user message if desired, or continue to retain context
            continue

        # extract assistant reply
        try:
            reply = response.choices[0].message.content
        except Exception:
            print("Unexpected response format:", response)
            continue

        print("Assistant:", reply)
        messages.append({"role": "assistant", "content": reply})
except KeyboardInterrupt:
    print("\nChat interrupted. Exiting.")
