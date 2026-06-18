from django.shortcuts import render
from .yield_model import predict_yield

def yield_form(request):

    if request.method == "POST":

        area = request.POST['area']
        rainfall = request.POST['rainfall']
        temperature = request.POST['temperature']

        predicted_yield = predict_yield(
            area,
            rainfall,
            temperature
        )

        context = {
            'yield_value': predicted_yield
        }

        return render(
            request,
            'yield_prediction/yield_result.html',
            context
        )

    return render(
        request,
        'yield_prediction/yield_form.html'
    )