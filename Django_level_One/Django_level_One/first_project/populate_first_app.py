
# it configure the setting for the project
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'first_project.settings')


import django
django.setup()

import random
from faker import Faker
from first_app.models import AccessRecord, Webpage, Topic, User




# fake pop script


# faker generation
fakgen = Faker()

topics = ['Search', 'Social', 'Marketplace', 'News', 'Games']


def add_topic():

    # what does it did, it did basically add new topic if topic
    # not present in database and if it is present then it retrieve
    # the existing topic

    # it return touple and we get the firstelement, which is refernce of model
    t = Topic.objects.get_or_create(top_name=random.choice(topics))[0]
    t.save()
    return t


def populate(N=5):

    for entry in range(N):


        #  get the topic
        top = add_topic()

        # it create the fake url
        fake_url = fakgen.url()

         # it create fake date
        fake_date = fakgen.date()

         # it creates the fake company name

        fake_name = fakgen.company()

        # create the new webpage entry
        webpg = Webpage.objects.get_or_create(topic=top, url=fake_url, name=fake_name)[0]

        # create a fake access record for that webpage

        acc_rec = AccessRecord.objects.get_or_create(name=webpg, date=fake_date)[0]



def populateuser(N=5):

    for entry in range(N):
        fake_name = fakgen.name().split()
        fake_first_name = fake_name[0]
        fake_last_name = fake_name[1]
        fake_email = fakgen.email()

        # new entry
        user = User.objects.get_or_create(first_name=fake_first_name,
                                          last_name =fake_last_name,
                                          email=fake_email)[0]

        user.save()
        



# it check the page is called directly of it is import somewhere
if __name__ == '__main__':
    print("populate script!")
    populate(20)
    populateuser(20)
    print("populate complete")
