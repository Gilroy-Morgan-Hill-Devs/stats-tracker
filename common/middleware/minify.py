import re

class MinifyMiddleware(object):

    def process_response(self, request, response):
        response.content = re.sub(r'\s\s+', ' ', response.content)
        return response

    # def process_template_response(self, request, response):
    #     import ipdb; ipdb.set_trace()