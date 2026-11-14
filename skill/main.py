import os
import json
import time
import urllib.request
import urllib.error

from dotenv import load_dotenv

# --------------------------------
# STEP 1: LOAD ENVIRONMENT VARIABLES
# --------------------------------

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    raise ValueError(
        "GEMINI_API_KEY not found! Check your .env file."
    )


# --------------------------------
# STEP 2: GEMINI API CONFIGURATION
# --------------------------------

model = "gemini-3.5-flash-lite"

url = (
    f"https://generativelanguage.googleapis.com/v1beta/"
    f"models/{model}:generateContent"
)

headers = {
    "Content-Type": "application/json",
    "x-goog-api-key": api_key
}


# --------------------------------
# STEP 3: CREATE REQUEST
# --------------------------------

payload = {
    "contents": [
        {
            "parts": [
                {
                    "text": "What is Artificial Intelligence? Explain in simple words."
                }
            ]
        }
    ]
}

data = json.dumps(payload).encode("utf-8")

req = urllib.request.Request(
    url,
    data=data,
    headers=headers,
    method="POST"
)


# --------------------------------
# STEP 4: CONNECT TO GEMINI API
# --------------------------------

print("\nConnecting to Gemini API...")

for attempt in range(3):

    try:

        with urllib.request.urlopen(
            req, timeout=60
        ) as response:

            result = json.loads(
                response.read().decode("utf-8")
            )

            # Extract AI response
            answer = result["candidates"][0]["content"]["parts"][0]["text"]

            print("\n========== GEMINI RESPONSE ==========\n")
            print(answer)
            print("\n=====================================")

            break

    except urllib.error.HTTPError as e:

        error_message = e.read().decode(
            "utf-8", errors="replace"
        )

        print(f"\nHTTP Error: {e.code}")
        print(error_message)

        if e.code in (429, 500, 502, 503, 504) and attempt < 2:

            wait_time = 2 ** (attempt + 1)

            print(
                f"\nRetrying after {wait_time} seconds..."
            )

            time.sleep(wait_time)

        else:
            print("\nAPI request failed. Please check the error.")
            break

    except urllib.error.URLError as e:

        print("\nConnection Error:", e.reason)
        break

    except (KeyError, IndexError, TypeError) as e:

        print("\nUnexpected API response:", e)
        break

    except TimeoutError:

        print("\nRequest timed out. Please try again.")
        break

    except Exception as e:

        print("\nUnexpected Error:", e)
        breakpython main.py
