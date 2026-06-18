from django.shortcuts import render
from ml_models.fertilizer_model import predict_fertilizer


def fertilizer_form(request):

    if request.method == "POST":

        n = request.POST['nitrogen']
        p = request.POST['phosphorus']
        k = request.POST['potassium']
        crop_name = request.POST['crop_name']

        predicted_fertilizer = predict_fertilizer(
            n,
            p,
            k,
            crop_name
        )

        context = {
            'fertilizer': predicted_fertilizer
        }

        return render(
            request,
            'fertilizer/fertilizer_result.html',
            context
        )

    return render(
        request,
        'fertilizer/fertilizer_form.html'
    )