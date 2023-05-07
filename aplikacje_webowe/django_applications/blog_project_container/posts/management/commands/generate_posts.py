from django.contrib.auth.models import User
from django.core.management import BaseCommand

from faker import Faker

from posts.models import Post

fake = Faker("pl_PL")


class Command(BaseCommand):
    help = 'Generates random posts'

    def add_arguments(self, parser):
        parser.add_argument('number_of_posts', type=int)

    def handle(self, *args, **kwargs):
        number_of_posts = kwargs['number_of_posts']

        for i in range(number_of_posts):
            users = User.objects.all()
            title = fake.sentence(nb_words=4)
            content = fake.paragraph(nb_sentences=20)
            author = fake.random_element(elements=users)
            Post.objects.create(title=title, content=content, author=author)
        self.stdout.write(self.style.SUCCESS(f'Successfully generated {number_of_posts} posts'))
