import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'SlangDictionary.settings')

import django
django.setup()

## FAKE POPULATE SCRIPT
import random
from Dictionary.models import Word
from faker import Faker

def add_topic():
	t = Topic.objects.get_or_create(top_name=random.choice(topics))[0]
	t.save()
	return t

def populate(N=5):
	for entry in range(N):

		#GET THE TOPIC FOR THE ENTRY
		#top = add_topic()

		#CREATE THE FAKE DATA FOR THAT ENTRY
		fake_word = Faker().word()
		fake_date = Faker().date()

		#CREATE THE NEW WEBPAGE ENTRY
		wo = Word.objects.get_or_create(word=fake_word, meaning="".join("".join(str([j for i in range(5) for j in Faker().words()]).split("'")).split("]")[0].split("[")[1]), date=fake_date)
		print(wo)
		#CREATE A FAKE ACCESS RECORD FOR THAT WEBPAGE
		#acc_rec = AccessRecord.objects.get_or_create(name=webpg, date=fake_date)[0]

if __name__ == '__main__':
	print("Populating script!")
	populate(50)
	print("Populating complete")
