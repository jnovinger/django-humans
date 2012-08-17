from django.shortcuts import render_to_response
from django.template import RequestContext

from humans.models import HumanGroup, Snippet

def humans(request):
    snippets = Snippet.objects.all()
    groups = HumanGroup.objects.all()

    return render_to_response(
        template_name='humans/humans.txt',
        dictionary={
            'snippets': snippets,
            'groups': groups,
        },
        mimetype='text/plain',
        context_instance=RequestContext(request),
    )

