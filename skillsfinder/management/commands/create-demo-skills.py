from django.contrib.auth import get_user_model
from django.core.management import BaseCommand
from django.db import transaction
from faker import Faker
from skillsfinder.models import Skill, SkillCategory

User = get_user_model()


class SkilCategory(object):
    pass


class Command(BaseCommand):
    help = """
    Creates sample skills
    """

    def add_arguments(self, parser):
        parser.add_argument('--seed', type=int, default=0, required=False)

    @transaction.atomic()
    def handle(self, *args, seed, **options):
        Faker.seed(seed)
        fake = Faker()

        def get_text(max_nb_chars=20):
            return fake.texts(nb_texts=1, max_nb_chars=max_nb_chars)[0][:-1]

        for category_id in range(5):
            cat = SkillCategory.objects.create(name=get_text())
            for skill_id in range(1, fake.random.randint(5, 25)):
                Skill.objects.create(name=get_text(), category=cat)
