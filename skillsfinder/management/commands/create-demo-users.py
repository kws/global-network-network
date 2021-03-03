from django.contrib.auth import get_user_model
from django.core.management import BaseCommand
from django.db import transaction
from faker import Faker
from skillsfinder.models import Organisation, Profile, Skill

User = get_user_model()

DEFAULT_LOCALES = ['en_US', 'en_GB', 'nl_NL']


class Command(BaseCommand):
    help = """
    Creates sample data
    """

    def add_arguments(self, parser):
        parser.add_argument('--seed', type=int, default=0, required=False)
        parser.add_argument('-n', '--num-profiles', type=int, default=100, required=False)
        parser.add_argument('-o', '--num-orgs', type=int, default=5, required=False)
        parser.add_argument('-l', '--locales', nargs="+", default=DEFAULT_LOCALES,
                            required=False)

    @transaction.atomic()
    def handle(self, *args, locales, num_profiles, num_orgs, seed, **options):
        Faker.seed(seed)

        skills = list(Skill.objects.all())

        for org_id in range(num_orgs):
            faker = Faker()
            local_faker = Faker(faker.random.choice(locales))

            org = Organisation.objects.create(name=local_faker.company())

            staff_count = local_faker.random.randint(1, max(5, (num_profiles - User.objects.count())))
            for staff_id in range(staff_count):
                first_name = local_faker.first_name()
                last_name = local_faker.last_name()
                email = f"{first_name}.{last_name}@example.com".lower()
                user = User.objects.create(
                    username=email,
                    first_name=first_name,
                    last_name=last_name,
                    email=email,
                )
                profile = Profile.objects.create(
                    user=user,
                    organisation=org,
                    title=local_faker.job(),
                    bio=local_faker.paragraph(nb_sentences=2),
                )

                for skill in local_faker.random_elements(elements=skills, unique=False):
                    profile.skills.add(skill)


