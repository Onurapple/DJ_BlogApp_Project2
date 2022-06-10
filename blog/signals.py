from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.template.defaultfilters import slugify
from .models import Post
from .utils import get_random_code

@receiver(pre_save, sender=Post)
def pre_save_create_slug(sender, instance, *args, **kwargs):
    if instance.slug:
        return
    instance.slug = slugify(instance.title + " " + get_random_code())