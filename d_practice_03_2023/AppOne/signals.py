from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver
from .models import User,Blog
from django.utils.text import slugify
@receiver(post_save,sender=Blog)
def post_save_blog_slug(sender,instance,created,**kwargs):
    if created:
        if instance.slug == "":
            base_slug = slugify(instance.title)
            slug = base_slug
            n = 1
            while Blog.objects.filter(slug=slug).exists():
                slug = '{}-{}'.format(base_slug,n)
                n += 1
            instance.slug = slug
            instance.save()

@receiver(pre_save,sender=User)
def pre_save_user_code(sender,instance,**kwargs):
    if instance.user_code == "":
        # print(instance.email)
        instance.user_code = "A5896"
        instance.save()
    
