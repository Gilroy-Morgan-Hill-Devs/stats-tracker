from django.views.generic.base import TemplateView


class Homepage(TemplateView):
    template_name = 'homepage/templates/homepage.html'

    def get_context_data(self, *args, **kwargs):
        return super(Homepage, self).get_context_data(*args, **kwargs)
