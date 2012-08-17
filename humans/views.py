from django.shortcuts import render_to_response
from django.template import RequestContext

from humans.models import Snippet

def humans(request):
    snippets = Snippet.objects.all()

    return render_to_response(
        template_name='humans/humans.txt',
        dictionary={'snippets': snippets},
        mimetype='text/plain',
        context_instance=RequestContext(request),
    )

