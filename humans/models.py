from django.contrib.auth.models import User
from django.db import models


class BaseMixin(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class OrderedMixin(models.Model):
    display_order = models.IntegerField(unique=True)

    class Meta:
        abstract = True

class BaseHumanMixin(BaseMixin, OrderedMixin):
    class Meta:
        abstract = True


class HumanGroup(BaseHumanMixin):
    label = models.CharField(max_length=100)

    def __unicode__(self):
        return self.label

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

    def render_handle(self):
        """ This is where we should hook the template system """
        pass


class Human(BaseHumanMixin):
    role = models.CharField(max_length=100)
    group = models.ForeignKey(HumanGroup)

    name = models.CharField(max_length=255, blank=True)
    user = models.OneToOneField(User, related_name='human')
    handles = models.ManyToManyField(Handle)

    def __unicode__(self):
        if self.user:
            return self.user.get_full_name() or self.user.username
        elif self.name:
            return self.name
        else:
            return 'anonymous'

    def render_handles(self):
        pass


class Snippet(BaseHumanMixin):
    """ Used to hold chunks of non-HTML text to be displayed. """
    text = models.TextField()

    def __unicode__(self):
        return self.text
