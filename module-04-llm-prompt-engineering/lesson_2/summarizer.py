from client import get_client

# Initialize the client
client = get_client()

def summarize_text(text: str) -> str:
    """
    Summarize the given text into a short, clear summary.
    """
    
    messages=[
        {"role": "system", "content": "You are a helpful summarization assistant."},
        {"role": "user", "content": f"Summarize the following text:\n\n{text}"}
        ]

    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=messages
        )
        
        summary = response.choices[0].message.content
        return summary
    
    except Exception as e:
        return f"Summarization failed: {e}"

if __name__ == "__main__":
    print("Paste text to summarize (or type a short paragraph):")
    text = input("> ")

    summary = summarize_text(text)

    print("\n--- Summary ---")
    print(summary)
