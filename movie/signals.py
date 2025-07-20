from django.db.models.signals import pre_save
from django.dispatch import receiver
from .models import Movie

# @receiver(pre_save, sender=Movie)
# def populate_omdb_fields(sender, instance, **kwargs):
#     if instance.pk is None:
#         instance.fetch_omdb_data()