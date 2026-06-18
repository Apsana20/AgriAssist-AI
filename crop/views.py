from django.shortcuts import render
from ml_models.crop_model import predict_crop


def crop_form(request):

    if request.method == "POST":

        n = request.POST['nitrogen']
        p = request.POST['phosphorus']
        k = request.POST['potassium']
        temp = request.POST['temperature']
        humidity = request.POST['humidity']
        ph = request.POST['ph']
        rainfall = request.POST['rainfall']

        predicted_crop = predict_crop(
            n,
            p,
            k,
            temp,
            humidity,
            ph,
            rainfall
        )

        context = {
            'crop': predicted_crop
        }

        return render(request, 'crop/crop_result.html', context)

    return render(request, 'crop/crop_form.html')