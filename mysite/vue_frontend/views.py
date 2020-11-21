from django.shortcuts import render

def test_vue(request):
    return render(request, "frontend/hiya.html")
