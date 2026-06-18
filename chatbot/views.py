from django.shortcuts import render
from .chatbot_model import get_answer


def chatbot_page(request):

    if request.method == "POST":

        question = request.POST['question']

        answer = get_answer(question)

        context = {
            'question': question,
            'answer': answer
        }

        return render(
            request,
            'chatbot/chatbot_result.html',
            context
        )

    return render(
        request, 'chatbot/chatbot.html'
    )