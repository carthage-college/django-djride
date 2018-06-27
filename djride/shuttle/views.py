from django.shortcuts import render


def map(request):
    return render(
        request, 'shuttle/home.html', {}
    )

