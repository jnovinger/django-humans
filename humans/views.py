from django.shortcuts import render_to_response
from django.template import RequestContext

from humans.models import HumanGroup, Snippet

def humans(request):
    snippet = Snippet.objects.random_snippet()
    groups = HumanGroup.objects.exclude(members__isnull=True)

    return render_to_response(
        template_name='humans/humans.txt',
        dictionary={
            'snippet': snippet,
            'groups': groups,
        },
        mimetype='text/plain',
        context_instance=RequestContext(request),
    )

