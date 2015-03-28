from djangomako.shortcuts import render_to_response, render_to_string

def render(request, *args, **kwargs):
    kwargs['context'] = RequestContext(request)
    return render_to_response(request, *args, **kwargs)