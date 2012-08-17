import random

from django.contrib.auth.models import User
from django.db import models
from django.template import Context, Template

# Model managers
class SnippetManager(models.Manager):
    def random_snippet(self):
        snippets = self.all()
        if not snippets:
            return Snippet()

        num = len(snippets)
        return snippets[random.randint(0, num - 1)]

# Model mixins
class BaseMixin(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
        ordering = ['modified', 'created',]


class OrderedMixin(models.Model):
    display_order = models.IntegerField(unique=True)

    class Meta:
        abstract = True
        ordering = ['display_order', ]

class BaseHumanMixin(BaseMixin, OrderedMixin):
    class Meta:
        abstract = True


# Begin concrete models
class HumanGroup(BaseHumanMixin):
    label = models.CharField(max_length=100)

    def __unicode__(self):
        return self.label

    def humans(self):
        return self.members.all()


class HandleType(BaseMixin):
    type = models.CharField(max_length=100)

    # Use standard Django template language. You must load tags if you are going to use them.
    template = models.TextField(blank=True)

    def __unicode__(self):
        return self.type


class Handle(BaseMixin):
    type = models.ForeignKey(HandleType)
    handle = models.CharField(max_length=100)

    def __unicode__(self):
        return self.handle

    def render(self):
        """ This is where we should hook the template system """
        template = Template(self.type.template)
        return template.render(Context({'handle':self.handle}))



class Human(BaseHumanMixin):
    role = models.CharField(max_length=100)
    group = models.ForeignKey(HumanGroup, related_name='members')
    location = models.CharField(max_length=255, blank=True)

    # Humans can be linked to Users or stand on their own
    name = models.CharField(max_length=255, blank=True)
    user = models.OneToOneField(User, related_name='human', blank=True, null=True)
    handles = models.ManyToManyField(Handle)

    class Meta:
        ordering = ['display_order',]

    def __unicode__(self):
        """
        If a User is linked, use that, else default to name field, else is anonymous.
        """
        if self.user:
            return self.user.get_full_name() or self.user.username
        elif self.name:
            return self.name
        else:
            return 'anonymous'

    def render_handles(self):
        """ Grab all of the handles, render them, and return them as a list. """
        handles = ''
        for handle in self.handles.all():
            handles += '%s\n' % handle.render()
        return handles

class Snippet(BaseHumanMixin):
    """ Used to hold chunks of non-HTML text to be displayed. """

    title = models.CharField(max_length=100)
    text = models.TextField()

    objects = SnippetManager()

    class Meta:
        ordering = ['display_order',]

    def __unicode__(self):
        return self.title
