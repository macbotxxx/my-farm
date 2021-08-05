from testimonials.models import ClientTestimonies, FAQ
from django.shortcuts import render


def index (request):
    """
    the frontend page for the farm project
    """

    feedback = ClientTestimonies.objects.all()
    faqs = FAQ.objects.all().order_by("-id")[:4]

    context = {
        'feedback': feedback,
        'faqs': faqs,
    }

    return render(request, 'main/index.html', context)
