import openai

# Replace this with your actual API key
openai.api_key = 'your-openai-api-key'

# Choose a fictional character
character = "Sherlock Holmes"

# Create a prompt template
def generate_prompt(user_input):
    return f"""You are now {character}, the famous fictional character. Respond to the user as {character} would, using their tone, personality, and speaking style.

User: {user_input}
{character}:"""

# Run a loop to interact
print(f"Chat with {character}. Type 'exit' to quit.\n")

while True:
    user_input = input("You: ")
    if user_input.lower() == 'exit':
        break

    prompt = generate_prompt(user_input)

    response = openai.Completion.create(
        engine="text-davinci-003",  # or use "gpt-3.5-turbo-instruct" if available
        prompt=prompt,
        max_tokens=150,
        temperature=0.8
    )

    reply = response.choices[0].text.strip()
    print(f"{character}: {reply}\n")
