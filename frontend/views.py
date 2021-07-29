from django.shortcuts import render

def index (request):
    """
    the frontend page for the farm project
    """
    return render(request, 'main/index.html')
