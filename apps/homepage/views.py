#from common.views.generic import TemplateView
#from user.forms import LeadSubmissionForm
#from simplepages.models import Carousel
from django.shortcuts import render

# class HomepageView(TemplateView):
#     template_name = "homepage.html"

#     def get_context_data(self):
#         carousel = Carousel.objects.get_or_none(page='homepage')
#         return {
#             'lead_form': LeadSubmissionForm(),
#             'carousel': carousel,
#             'carousel_slides': carousel.carouselslide_set.order_by('order'),
#         }

def index(request):
    return render(request, 'homepage/index.html')