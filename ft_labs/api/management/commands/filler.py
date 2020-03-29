import os
import django
import random
import string
from api.models import User, ActivityPeriod
from faker import Faker
os.environ.setdefault('DJANGO_SETTING_MODULE', 'PRO.settings')


django.setup()
fake = Faker()

def randomString(string_length=9):
    letters = string.ascii_uppercase
    return ''.join(random.choice(letters) for i in range(string_length))


def set_model_data(members=2, activity_period_num=3):
    for i in range(members):
        member_id = randomString()
        real_name = fake.name()
        tz = fake.timezone()
        try:
            user_obj = User.objects.get_or_create(id=member_id, real_name=real_name, tz=tz)[0]

            for j in range(activity_period_num):
                start_time = fake.date(pattern="%b %d %Y  %I:%M%p")
                end_time = fake.date(pattern="%b %d %Y %I:%M%p")
                activity_obj = ActivityPeriod.objects.get_or_create(user=user_obj, start_time=start_time, end_time=end_time)[0]
        except Exception as e:
            print(e)
