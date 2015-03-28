from django.template import RequestContext
from django.views.generic import TemplateView as DjangoTemplateView

class TemplateView(DjangoTemplateView):
    pass
    # def render_to_response(self, context, **kwargs):
    #     import pdb; pdb.set_trace()
    #     return super(TemplateView, self).render_to_response(
    #         context,
    #         context_instance=RequestContext(
    #             self.request,
    #         ),
    #         **kwargs
    #     )