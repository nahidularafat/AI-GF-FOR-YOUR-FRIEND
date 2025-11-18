# core/views.py
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from .utils import call_gemini_api
from .models import Conversation

def chat_page(request):
    # Only send the last 10 messages for simplicity
    messages = Conversation.objects.order_by('-timestamp')[:10]
    return render(request, "core/chat.html", {"messages": reversed(messages)})

@csrf_exempt
def get_response(request):
    if request.method == "POST":
        user_input = request.POST.get("message")
        
        # Call the corrected Gemini API function
        ai_response = call_gemini_api(user_input)
        
        # Save conversation (even if there's an error message)
        Conversation.objects.create(user_message=user_input, ai_message=ai_response)
        
        return JsonResponse({"response": ai_response})
    return JsonResponse({"response": "Invalid request"})