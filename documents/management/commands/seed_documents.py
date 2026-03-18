from django.core.management.base import BaseCommand
from faker import Faker
import random
from documents.models import Document

fake = Faker()

DOC_TYPES = ['Policy', 'Research', 'Guidelines', 'Report', 'Form']

TOPICS = [
    'leave application', 'infectious disease', 'data collection',
    'health research', 'laboratory analysis', 'HR policy',
    'staff welfare', 'disease prevention', 'data quality',
    'field research', 'medical protocol', 'annual report',
    'budget guidelines', 'procurement policy', 'training manual',
]

class Command(BaseCommand):
    help = 'Seed 300 fake documents'

    def handle(self, *args, **kwargs):
        self.stdout.write('Creating 300 documents...')

        for i in range(300):
            topic = random.choice(TOPICS)
            Document.objects.create(
                title=f"{fake.bs().title()} - {topic.title()}",
                doc_type=random.choice(DOC_TYPES),
                content=f"{fake.paragraph(nb_sentences=5)} "
                        f"This document covers {topic}. "
                        f"{fake.paragraph(nb_sentences=5)}"
            )

        self.stdout.write(self.style.SUCCESS('Successfully created 300 documents!'))
