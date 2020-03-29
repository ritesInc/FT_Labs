from django.core.management.base import BaseCommand, CommandError
from . import filler

def set_user_data():
    blog_data = Blog.objects.all()
    for data in blog_data:
        data.date = datetime.now()
        data.save()

class Command(BaseCommand):
    help = "Provides User details and their Activity periods"

    def handle(self, **options):
        filler.set_model_data()
