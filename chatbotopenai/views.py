from django.shortcuts import render
from django.http import JsonResponse

import openai

def chatbot_view(request):
    if request.method == 'POST':
        user_query = request.POST.get('user_query', '').strip()
        if not user_query:
            return render(request, 'chatbot.html', {'chatbot_response': 'Please enter a math problem.'})
        
        openai.api_key = "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"

        try:
            # Provide your own custom prompt including the user's query
            custom_prompt = f"act as a math's teacher and provide the answer for basic math's problem and as a result give me only the answer. For example, if the question is '3+5', your response should be '8' don't try to give long answer and like that your response should be obly the answer that's it, and the question is '{user_query}'"
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": "You are a math assistant."},
                    {"role": "user", "content": custom_prompt}
                ]
            )
            chatbot_response = response.choices[0].message["content"].strip()
        except Exception as e:
            return JsonResponse({'error': str(e)})
    else:
        chatbot_response = ""

    return render(request, 'chatbot.html', {'chatbot_response': chatbot_response})
