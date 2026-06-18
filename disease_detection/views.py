from django.shortcuts import render


def disease_form(request):

    if request.method == "POST":

        context = {
            'disease_name': 'Bacterial Blight',
            'recommendation': 'Apply Copper Oxychloride'
        }

        return render(
            request,
            'disease_detection/disease_result.html',
            context
        )

    return render(
        request,
        'disease_detection/disease_form.html'
    )