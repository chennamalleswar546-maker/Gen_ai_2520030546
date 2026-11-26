import os
from dotenv import load_dotenv
from google import genai

# Step 1: Load environment variables
load_dotenv()

# Step 2: Get Gemini API key
api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    raise ValueError("GEMINI_API_KEY not found in .env file")

# Step 3: Connect to Gemini
client = genai.Client(api_key=api_key)

print("Connecting to Gemini...")
print("Waiting for response...\n")

try:
    # Step 4: Send prompt to Gemini
    response = client.models.generate_content(
        model="gemini-3.6-flash",
        contents="Explain Artificial Intelligence in simple words."
    )

    # Step 5: Display response
    print("Gemini Response:\n")
    print(response.text)

    print("\nResponse completed successfully!")

except Exception as e:
    print("\nGEMINI API ERROR:")
    print("Error type:", type(e).__name__)
    print("Error message:", str(e))
