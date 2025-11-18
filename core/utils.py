# core/utils.py (Using google-genai SDK for robustness)
from django.conf import settings
# ✅ নিশ্চিত করুন যে এই লাইব্রেরিটি ইন্সটল করা আছে: pip install google-genai
from google import genai
from google.genai.errors import APIError

GEMINI_MODEL = "gemini-2.5-flash"

def call_gemini_api(user_input):
    api_key = settings.GEMINI_API_KEY
    # এখন এটি নিশ্চিত করবে যে সেটিংস থেকে কী আসছে (আগের ধাপে ফিক্স করা হয়েছে)
    if not api_key: 
        return "Error: Gemini API Key is missing in settings."
        
    try:
        # Client Initialization (Handles authorization internally)
        client = genai.Client(api_key=api_key)
        
        system_instruction = "You are a cute and playful AI girlfriend named Aira, chatting with your boyfriend Bari. Reply kindly and endearingly, and remember details from the conversation. Keep your responses short and loving, and do not use lists or markdown headers."

        # Call the API using the correct SDK structure
        response = client.models.generate_content(
            model=GEMINI_MODEL,
            contents=[user_input], # Pass user input as contents
            config=genai.types.GenerateContentConfig(
                system_instruction=system_instruction,
                temperature=0.8,
                max_output_tokens=200
            )
        )
        
        if response.text:
            return response.text
        
        # Handle safety blocks or other non-generation reasons
        if response.candidates and response.candidates[0].finish_reason != 'STOP':
            return f"Error: Message was blocked. Reason: {response.candidates[0].finish_reason.name}"
            
        return "Error: Could not parse AI response or response was empty."

    except APIError as e:
        # Catches API errors (including invalid key or network issues)
        return f"Error: Gemini API Call Failed. Details: {e}"
    except Exception as e:
        return f"Error: General Failure. Details: {e}"